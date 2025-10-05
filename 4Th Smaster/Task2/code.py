import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# When loading test.csv, force PassengerId to string
test = pd.read_csv('test.csv', dtype={'PassengerId': str})
train = pd.read_csv('train.csv', dtype={'PassengerId': str})

assert 'PassengerId' in train.columns, "train.csv missing PassengerId"
assert 'PassengerId' in test.columns, "test.csv missing PassengerId"
assert 'Transported' in train.columns, "train.csv missing Transported"

train['is_train'] = 1
test['is_train'] = 0
test['Transported'] = np.nan
full = pd.concat([train, test], sort=False)

if 'Cabin' in full.columns:
    full[['Deck', 'Cabin_num', 'Side']] = full['Cabin'].str.split('/', expand=True)

for col in full.select_dtypes(include='object').columns:
    full[col] = full[col].fillna(full[col].mode()[0])
for col in full.select_dtypes(include=np.number).columns:
    full[col] = full[col].fillna(full[col].median())

cat_cols = [col for col in full.select_dtypes(include='object').columns if col != 'PassengerId']
for col in cat_cols:
    le = LabelEncoder()
    full[col] = le.fit_transform(full[col])

train = full[full['is_train'] == 1].drop(['is_train'], axis=1)
test = full[full['is_train'] == 0].drop(['is_train', 'Transported'], axis=1)

X = train.drop(['PassengerId', 'Transported'], axis=1)
y = train['Transported'].astype(int)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_val)
print("Validation accuracy:", accuracy_score(y_val, y_pred))

clf.fit(X, y)

X_test = test.drop(['PassengerId'], axis=1)
test_preds = clf.predict(X_test)

submission = pd.DataFrame({
    'PassengerId': test['PassengerId'],
    'Transported': test_preds.astype(bool)
})
submission.to_csv('submission.csv', index=False)
print("Submission file 'submission.csv' created.")
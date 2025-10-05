import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

test_ids = test["Id"]

y = train["SalePrice"]
X = train.drop(["SalePrice"], axis=1)
X_test = test.copy()

all_data = pd.concat([X, X_test], sort=False).reset_index(drop=True)

all_data.drop("Id", axis=1, inplace=True)

for col in ["Alley","PoolQC","Fence","MiscFeature","FireplaceQu",
            "GarageType","GarageFinish","GarageQual","GarageCond",
            "BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinType2",
            "MasVnrType"]:
    if col in all_data.columns:
        all_data[col] = all_data[col].fillna("None")

for col in all_data.select_dtypes(include=[np.number]).columns:
    all_data[col] = all_data[col].fillna(all_data[col].median())

all_data = pd.get_dummies(all_data)

X = all_data.iloc[:len(train), :]
X_test = all_data.iloc[len(train):, :]

kf = KFold(n_splits=5, shuffle=True, random_state=42)
test_preds = np.zeros(X_test.shape[0])

for train_idx, val_idx in kf.split(X):
    X_tr, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_tr, y_val = y.iloc[train_idx], y.iloc[val_idx]
    model = LinearRegression()
    model.fit(X_tr, y_tr)
    test_preds += model.predict(X_test) / kf.n_splits

submission = pd.DataFrame({"Id": test_ids, "SalePrice": test_preds})
submission.to_csv("submission.csv", index=False)
print("submission.csv is ready!")
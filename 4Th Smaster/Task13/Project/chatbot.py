import re
import random



def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text



qa_data = {
    ("hello", "hi", "hey", "salam"): [
        "Hello! Welcome to our Gym 😊 How can I help you?",
        "Hi there! Ready to get fit today? 💪",
        "Hey buddy! Need any gym info?"
    ],
    ("timing", "time", "open", "hours"): [
        "Our gym is open from 6 AM to 10 PM daily ⏱️",
        "Timings: 6:00 AM – 10:00 PM, 7 days a week!"
    ],
    ("membership", "price", "fee", "charges", "cost"): [
        "Membership Fees:\n• Monthly: 2500 PKR\n• Quarterly: 6500 PKR\n• Annual: 18000 PKR",
        "Affordable plans! Monthly 2500, Annual 18000 PKR."
    ],
    ("diet", "food", "meal", "nutrition"): [
        "We provide Weight Loss, Muscle Gain, and Balanced Meal Plans 🥗",
        "Our trainer will give you custom diet plans!"
    ],
    ("workout", "exercise", "training", "routine"): [
        "We offer cardio, strength training & bodybuilding workouts 💪",
        "Custom workout plans for every fitness level!"
    ],
    ("trainer", "coach", "instructor"): [
        "We have certified trainers with 5+ years of experience.",
        "Our coaches are professional and friendly!"
    ],
    ("location", "address", "where"): [
        "We are located at Main City Road, near Mall Plaza.",
        "Visit us at Main Road beside Mall Plaza."
    ],
    ("join", "register", "signup"): [
        "Bring CNIC + 1st month fee. Registration takes only 5 minutes!",
        "Just come with CNIC and fee—simple joining process!"
    ],
    ("bye", "goodbye", "exit"): [
        "Goodbye! Stay strong 💪",
        "Take care! Keep training hard 🔥"
    ],
}



def get_response(message):
    msg = preprocess(message)
    for keywords, responses in qa_data.items():
        if any(keyword in msg for keyword in keywords):
            return random.choice(responses)
    return random.choice([
        "Sorry, I didn't understand. Try asking about gym timings, membership, or workouts 🙂",
        "I couldn’t get that. Please ask something gym-related."
    ])

knowledge_base = {
    "helo": "Hello! Welcome to our Hotel Managment System. How can I assist you today?",
    "hi": "Hi! How can I help you?",
    "hey": "Hey there! Feel free to ask anything about our hotel.",
    "good morning": "Good Morning! How may I help you regarding hotel services?",
    "good evening": "Good Evening! How can I assist you today?",
    "greetings": "Greetings! How can I help you with hotel information?",

    "room types": "We offer Single, Double, Deluxe, Executive, and Suite rooms.",
    "rooms": "We have Single, Double, Deluxe, Executive, and Suite rooms available.",
    "room price": "Prices start at PKR 6000 (Single), PKR 8500 (Deluxe), PKR 14000 (Suite).",
    "price": "Room prices depend on type: Single (6000), Deluxe (8500), Suite (14000).",
    "booking": "You can book online, by phone, or directly at our reception.",
    "reservation": "Room reservation can be done online, via call, or at reception.",

    "check in": "Our check-in time is 2:00 PM. Early check-in depends on availability.",
    "check out": "Our check-out time is 12:00 PM. Late check-out may include extra charges.",
    "early check in": "Early check-in is subject to room availability.",
    "late check out": "Late check-out may include additional cost depending on extra hours.",

    "facilities": "We offer free Wi-Fi, breakfast, pool, gym, parking, and 24/7 room service.",
    "services": "Our services include Wi-Fi, daily cleaning, laundry, breakfast, parking & more.",
    "wifi": "Yes, we provide free high-speed Wi-Fi in all rooms and public areas.",
    "internet": "Free high-speed Wi-Fi is available throughout the hotel.",
    "breakfast": "Breakfast is complimentary and served from 7AM to 10:30AM.",
    "restaurant": "Our restaurant offers Pakistani & Continental dishes from 7AM to 11PM.",
    "gym": "Our gym is open 24/7 with modern equipment.",
    "pool": "The swimming pool is open from 8AM to 8PM for all guests.",
    "parking": "Free parking is available for all guests.",
    "laundry": "Laundry service is available from 9AM to 7PM.",

    "cancellation": "Free cancellation is available up to 24 hours before check-in.",
    "refund": "Refunds are processed within 5-7 business days after cancellation.",
    "pets": "Sorry, pets are not allowed inside the hotel premises.",
    "smoking": "Smoking is strictly prohibited inside rooms.",

    "location": "We are located in the city center, near business and shopping areas.",
    "address": "Our hotel is located near the main city center, easy to access from any route.",

    "default": "I'm sorry, I don't have information about that. Please ask any hotel-related question."
}



def get_reply(message):
    msg = message.lower()
    for keyword in knowledge_base:
        if keyword in msg:
            return knowledge_base[keyword]
    return knowledge_base["default"]
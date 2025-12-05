responses = {
      "hi": "Hello! How can I assist you today?",
    "hello": "Hello! How can I help you?",
    "hey": "Hi there! How may I assist you?",
    "assalamualaikum": "Wa Alaikum Assalam! How can I help you?",
    "salam": "Wa Alaikum Assalam! How may I assist you?",

    "room": "we have single, double, deluxe, and suite rooms availbele.",
    "price": "our room rates are: single - pkr 6000, double - pkr 9000, deluxe -pkr 12000, and suite - pkr 20000.",
    "cost": "Our room rates are: Single – PKR 6000, Double – PKR 9000, Deluxe – PKR 12000, and Suite – PKR 20000.",
     "amenities": "We offer Free WiFi, Complimentary Breakfast, Swimming Pool, Gym, and 24/7 Room Service.",
    "facility": "We offer Free WiFi, Complimentary Breakfast, Swimming Pool, Gym, and 24/7 Room Service.",
    "book": "Sure! To proceed with the booking, please share your name, check-in/check-out dates, and preferred room type.",
    "booking": "Sure! To proceed with the booking, please share your name, check-in/check-out dates, and preferred room type.",
}

def get_reply(message):
    msg = message.lower()

    for keyword, reply in responses.items():
        if keyword in msg:
            return reply
        
    return "I can help you with room details, prices, amenities, or booking information. How may I assist you?"

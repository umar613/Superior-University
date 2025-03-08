#  task 1 Code for LUHN Algorithm
def luhn_check(card_number):
    card_number=card_number.replace(" ", "").replace("-", "")
    digits=[int(d) for d in card_number]
    digits.reverse()
    
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total=sum(digits)
    return total % 10==0

card_number="4532 1488 0343 6467"
if luhn_check(card_number):
    print(f"{card_number} is valid.")
else:
    print(f"{card_number} is invalid.")



# task 2 Write a Python Program to Remove Punctuations from the Given String
import string

def remove_punctuation(input_string):
    translator=str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

input_string="Hello, world! This is a test string: does it work?"
cleaned_string=remove_punctuation(input_string)
print("Original String:", input_string)
print("String without Punctuation:", cleaned_string)



# task 3 Write a Python Program to Sort the Sentence in Alphabetical Order
def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

sentence = "muneer is the bigest bad man"
sorted_sentence = sort_sentence(sentence)
print("Original Sentence:", sentence)
print("Sorted Sentence:", sorted_sentence)
import string
import random

letter_lower = string.ascii_lowercase

letter_lower_list = list(letter_lower) #26 elementów
letter_upper_list = list(letter_lower.upper()) #26 elementów
special_signs = ["!","#","$","*"] #4 elementy
numbers_list = [] #10 elementów

for number in range(0,10):
    numbers_list.append(str(number))

char_list = letter_lower_list + letter_upper_list + numbers_list + special_signs

length = input("Ile znaków ma mieć hasło?\n")

while length.isnumeric() == False:
    print("Musisz podać liczbę!")
    length = input("Ile znaków ma mieć hasło?\n")
else:
    password = "".join(random.sample(char_list, int(length))) # to generuje hasło w którym nie powtarzają się znaki
    print(f"Twoje hasło to: {password}")

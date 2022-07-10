import string
import random

letter_lower = string.ascii_lowercase

letter_lower_list = list(letter_lower) #26 elementów
letter_upper_list = list(letter_lower.upper()) #26 elementów
special_signs = ["!","#","$","*"] #4 elementy
numbers_list = [] #10 elementów

for number in range(0,10):
    numbers_list.append(str(number))
char_list = []

length = input("Ile znaków ma mieć hasło?\n")
while length.isnumeric() == False:
    print("Musisz podać liczbę!")
    length = input("Ile znaków ma mieć hasło?\n")
else:
    lower = input("Czy mają być małe litery?\n")
    if lower == 'tak' or lower == 't' or lower == 'yes' or lower == 'y':
        char_list += letter_lower_list
    else:
        pass
    
    upper = input("Czy mają być duże litery?\n")
    if upper == 'tak' or upper == 't' or upper == 'yes' or upper == 'y':
        char_list += letter_upper_list
    else:
        pass

    numbers = input("Czy mają być cyfry?\n")
    if numbers == 'tak' or numbers == 't' or numbers == 'yes' or numbers == 'y':
        char_list += numbers_list
    else:
        pass

    special = input("Czy mają być znaki specjalne?\n")
    if special == 'tak' or special == 't' or special == 'yes' or special == 'y':
        char_list += special_signs
    else:
        pass
    
    option = input("Czy znaki mogą się powtarzać?\n")
    if option == 'tak' or option == 't' or option == 'yes' or option == 'y':
            password = "".join(random.choices(char_list, k = int(length))) #generuje hasła z możliwością powtarzania znaków
            print(f"Twoje hasło to: {password}")
    else:
        if int(length) > len(char_list):
            print("Hasło jest za długie względem ilości wybranych znaków!")
            len = int(len(char_list))+1
            print(f"Jeśli chcesz kontynuować podaj wartość mniejszą niż {len}")
        else:
            password = "".join(random.sample(char_list, int(length))) #generuje hasło bez powtarzania znaków 
            print(f"Twoje hasło to: {password}")

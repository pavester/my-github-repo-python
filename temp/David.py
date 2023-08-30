
# importy
import random

# uvítání
oddelovac = "-" * 47

print("***********************************************")
print("***************** BULLS & COWS ****************")
print("***********************************************")
print()

print("Hi there!")
print(oddelovac)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(oddelovac)
print("Enter a number: ")
print(oddelovac)

# generátor tajného čísla
digits = "0123456789"
last3 = random.sample(digits, 3)
first = random.choice([d for d in digits[1:] if d not in last3])
number = first+"".join(last3)

# vstup uživatele / upozornění na nesprávný vstup / algoritmus hry / počítání pokusů
bulls = 0
cows = 0
score = 0

while bulls < 4:
    bulls, cows = 0, 0
    user_num = input(">>> ")

    # upozornění
    if not user_num.isdigit():
        print("The number is not numeric. Try again.")
        print(oddelovac)
    elif len(user_num) != 4:
        print("The number must have exactly 4 digits. Try again.")
        print(oddelovac)
    elif user_num.startswith("0"):
        print("The number starts with zero. Try again.")
        print(oddelovac)
    elif len(user_num) > len(set(user_num)):
        print("The number contains duplicity. Try again.")
        print(oddelovac)

    # porovnání vygenerovaného čísla a zadaného čísla
    else:
        for i in range(len(number)):
            if user_num[i] in number and user_num[i] != number[i]:
                cows += 1
            if user_num[i] in number and user_num[i] == number[i]:
                bulls += 1

        # vypsání průběžného výsledku hádání / rozlišení množného a jednotného čísla
        if cows == 1:
            print(cows, "cow")
        else:
            print(cows, "cows")
        if bulls == 1:
            print(bulls, "bull")
        else:
            print(bulls, "bulls")
        print(oddelovac)

        score += 1

# vyhodnocení výsledku
if score == 1:
    rating = "impossible. You have a super power"
elif score < 6:
    rating = "amazing"
elif score < 11:
    rating = "average"
else:
    rating = "not so good"

# vypsání výsledku
print(f"Congratulations! The secret number was {number}")
print(f"You found the number in {score} regular guesses.")
print(f"That is {rating}.")
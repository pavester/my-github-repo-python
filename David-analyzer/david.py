"""
projekt_1.py: První projekt do Engeto Online Python Akademie

author: David Šnajdr
email: d.snajdr@email.cz
discord: David Š.#7349
"""

# texty
from task_template import TEXTS

# uživatelé a hesla
users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz"  : "pass123"}

# přihlašovací údaje
print("****************************************")
print("************ TEXT ANALYZER *************")
print("****************************************")
print()
username = input("Username: ")
password = input("Password: ")

# kontrola přihlašovacích údajů
oddelovac = "-" * 40

if users.get(username) == password:
    print(oddelovac)
    print(f"Welcome to the app, {username}!")
    print(f"We have exactly 3 texts to be analyzed.")
    print(oddelovac)
else:
    print("Invalid username or password. Terminating the program.")
    quit()

# výběr textu a kontrola správnosti vstupu
text_num = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac)

if text_num.isnumeric() and int(text_num) in range (1, 4):
     text_num = int(text_num) - 1
else:
    print("You need to enter a NUMBER between 1-3.")
    print("Terminating the program.")
    quit()

# výpočty a proměnné
num_words = TEXTS[text_num].split()
counts = {"title" : 0, "upper" : 0, "lower" : 0}
numeric = list()
graph = {}

for word in TEXTS[text_num].split():
    word = word.strip(",.:;")
    if len(word) not in graph:
        graph[len(word)] = 1
    else:
        graph[len(word)] += 1

    if word.istitle():
        counts["title"] = counts["title"] + 1
    elif word.isupper():
        counts["upper"] = counts["upper"] + 1
    elif word.islower():
        counts["lower"] = counts["lower"] + 1
    elif word.isnumeric():
        numeric.append(int(word))

print(f'There are {len(num_words)} words in the selected text.')
print(f'There are {counts["title"]} titlecase words.')
print(f'There are {counts["upper"]} uppercase words.')
print(f'There are {counts["lower"]} lowercase words.')
print(f'There are {len(numeric)} numeric strings.')
print(f'The sum of all the numbers is {sum(numeric)}')
print(oddelovac)

# graf
print(f'LEN|    OCCURENCES    |NR.')
print(oddelovac)

for key, value in sorted(graph.items()):
    print(f'{key:3}|{"*" * value:17} |{value}')
print(oddelovac)
print("Have a nice day. See you next time!")






















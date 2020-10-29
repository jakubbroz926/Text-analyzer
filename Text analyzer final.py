from copy import deepcopy
print("-" * 40)
print("Welcome to the app. Please log in:")
prjmeno = input("USERNAME")
heslo = input("PASSWORD")
uzivatelé = {"bob": "123","ann": "pass123","mike": "password123","liz": "pass123"}
if uzivatelé.get(prjmeno) != heslo:
    print("ERROR")
    quit()

print("-" * 40)
#TEXTY
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
print("We have 3 texts to be analyzed.")
VOLBA = int(input("Enter a number btw 1 and 3 to select:"))
text=TEXTS[VOLBA-1]
newtext = text.split()
newtext2 = deepcopy(newtext)
newtext3 = deepcopy(newtext)
number_of_letters = len(newtext)
print("-" * 40)
print("There are {} words in the selected text.".format(number_of_letters))
title = 0
upper = 0
lower = 0
numeric = 0
letter = ""
while newtext:
    letter = newtext.pop()
    if letter.istitle():
        title += 1
    elif letter.isupper():
        upper += 1
    elif letter.islower():
        lower += 1
    elif letter.isnumeric():
        numeric += 1
print("There are {} titlecase words\n"
      "There are {} upper words\nThere are {} lowercase words"
      "\nThere are {} numeric strings".format(title,upper,lower,numeric))
print("-" * 40)
word = ""
delky_slov = {}
i = 1
while len(newtext2) > 0:
    word = newtext2.pop().strip(".,-")
    delka_slovo = len(word)
    if delka_slovo not in delky_slov:
        delky_slov.setdefault(delka_slovo, i)
    elif delka_slovo in delky_slov:
        value = delky_slov.get(delka_slovo)
        delky_slov[delka_slovo] = value + 1
while len(delky_slov) > 0:
    if i not in delky_slov.keys():
        i += 1
    elif i in delky_slov.keys():
        print(i,"*" * delky_slov.get(i), delky_slov.get(i))
        delky_slov.pop(i)
print("-" * 40)
word1 = ""
součet = 0
while len(newtext3) > 0:
    word1 = newtext3.pop()
    if word1.isnumeric():
        actual_number = int(word1)
        součet = součet + actual_number
print("If we summed all the numbers in this text we would get:",součet)
print("-" * 40)

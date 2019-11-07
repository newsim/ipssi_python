#!/usr/bin/python3

print("hello world")
# mettez bien des epsaces et pas des tab
a=1
if a == 0:
    print("toto")
else:
    print('a ne vaut pas 0')

print("fin")


# un entier 
entier = 1

# float 
fl = 1.5

#string 

string = "chaine1"
string = 'chaine1'
string = """chaine1"""

string = " ila va dire \"coucou\" assf"
string = """il va dire "coucou" assf"""

# les commentaires 

"""
les commentaires multilgnes 
sont avec des " " " 
"""


stringadd = "aa" + "bb"

stringadd = "aa" "bb"
print(stringadd)

string = """ coucou
salut
hello"""

if a == 0:
    string = ("coucou\n"
              "salut\n"
              "hello")

#nomenclature google

alphabet = "abcdefghijklmnopqrstuvwxyz"

if 'a' in alphabet:
    print("j'ai trouve a")

alist = list()
alist = []
alist = ["a", "b"]

alist = ["0", "1", "2", "3", "4"]

#une lkist de int
alist = [1, 2, 3, 4]
for x in alist:
    print(x)
print(alist)

# fonction qsui genere 15 chiffres de 0 14 
alist = range(15)
print(alist)
for x in alist:
    print(x)

for char in alphabet:
    print(char, end="\n")
    #print char

alist = []
print(alist)
alist.append("hello")
print(alist)
alist.append("hello")
print(alist)
alist.append("hello")
print(alist)
alist.append("hello")
print(alist)
alist.pop()
print(alist)
blist = ["salut", "salut"]
print (alist + blist)

adict = dict()
adict = {}
adict = { "fr": "salut", "en": "hello"}
print (adict)

print (adict["fr"])

lang = "en"
print(adict[lang])
trad = { "fr": "salut",
        "en": "hello"}

for key in trad:
    print(key)
    print(trad[key])

trad_fr = {"bjou": "salut",
        "aie": "j'ai mal"}
trad_en = {"bjou": "hello",
        "aie": "it hurts"}

# un idoc dans un dico 

trad = {"fr": trad_fr,
        "en": trad_en}
lang= "fr"
print(trad[lang]['aie'])
lang = "en"
print(trad[lang]['aie'])

alist = [trad_fr, trad_en]
print(alist)

# list comprehension 
alist = ["0", "1", "2", "3", "4"]

list_comp = [x for x in alist]
print(list_comp)
list_comp = alist
print(list_comp)

list_comp = [x + "aa" for x in alist]
print(list_comp)

list_comp = []
for x in alist:
    list_comp.append(x + "aa")
print(list_comp)

trad = {"fr": "salut",
        "en": "hello"}
alist = [key for key in trad]
print(alist)


# recuperer ma liste de langue 



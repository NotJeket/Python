import re

#add your own varayety of spices see what comes out
string= "Cel mai mult imi plac condimentele iuti, dau un gust mai bun la 50 de feluri de mancare!!"

uppercase_characters = re.findall(r"[A-Z]",string)
lowercase_characters = re.findall(r"[a-z]", string)
numerical_characters = re.findall(r"[0-9]", string)
special_characters = re.findall(r"[, .!?]", string)

print("Ai" ,len(uppercase_characters), "caractere de tipar")
print("Ai" ,len(lowercase_characters), "caractere normale")
print("Ai" ,len(numerical_characters), "numere")
print("Ai" ,len(special_characters), "caractere speciale")
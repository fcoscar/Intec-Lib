import VowelCounter as counter
ext = ""
print('PRESS 0 TO TERMINATE')
while ext != '0':
    ext = input("Palabra o Frase: ")
    print(counter.count_vowels(ext))



#indexing
'''print("Hello World!")
text = "Hello World!"
print(text[11])

word =input("word: ")
print(word[len (word) - 1]) #accessing using len function'''

#slicing
''' text = "Hello World"
 print(text[-8:-6])
 print(text[0:2], text [6:8])
name = "virus"
print(name"your name is " + name)
print(f"{0} {1}".format(text[0:2], text[6:8])) #format other ways to manipulate '''

#string methods

''' word ="hello woRld"
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.title())
print(word.replace("h", "x"))
print(word.find("e"))
print(word.isalpha())
print(word.isnumeric())
print(word.isalnum()) '''

txt = "summer bootcamp"
print(txt.title())
print(f"{txt[0:14].capitalize()+ txt[-1].capitalize()}")
print(txt[-8:-4].replace("b","L"))
print(txt[11:15].replace("p","E"))
print(f"{txt[12]}{txt[5]}".upper())

x = txt.replace(" ", "")
print(x.isalpha())

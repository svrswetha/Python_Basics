a = "swetha is a nice girl"

print(a[0])

print(a[1])
print(a[-1])

a = "swetha"
b= "sujeet"

c=a+b
print(c)

a = 3.14

print(a)

b = str(a)

print(b)

print(str.capitalize("swetha"))
print(str.find('swetha', 'we',0,6))

f = open("alice_in_wonderland.txt","r")
text = f.read()

print(len(text))

print(text[0])

print(text[1])
print(text[-1])

every_word = text.split()

for e in every_word:
    print(e)
    upper = e.capitalize()
    print(upper)


every_sentence = text.split(".")

for es in every_sentence:
    print(es)

lowercase = text.lower()
print(lowercase)

uppercase = text.upper()
print(uppercase)

print(text.find('THE'))

print(text.count('THE'))

print(text.replace("Alice", "Bob"))
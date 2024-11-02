v = ["a" , "e", "i", "o", "u", "A", "E", "I", "O", "U"]

h = 0
n = 0
ask = input("Enter A sentence to count the vowels of: ")

print(len(ask))

for i in ask:
    if i in v:
        n = n + 1
    else:
        h = h+1
        x = len(ask) - 1
        j = h - x


print("Number of vowels: ", n)
print("Number of consanants: ", h)
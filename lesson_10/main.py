file = open("text.txt", "r")
data = file.read()
file.close()
print(data)

print("-----------------------------------------------------------------------------------------------")

file = open("text.txt", "r")
data = file.readline()
while data:
    print(data.strip())
    data = file.readline()
print(data)
file.close()

print("-----------------------------------------------------------------------------------------------")

file = open("text.txt", "r")
data = file.readlines()
for line in data:
    print(line.strip())
file.close()

print("-----------------------------------------------------------------------------------------------")

file = open("text2.txt", "w")
file.write("Angelina, Hello!")
file.close()














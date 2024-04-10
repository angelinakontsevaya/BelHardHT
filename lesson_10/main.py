import json

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
file.write("Angelina,Hi!")
file.close()

with open("text2.txt", "r") as file:
    content = file.read()
    print(content)

print("-----------------------------------------------------------------------------------------------")

data = {"name": "Angelina", "age": 25}
with open("test_json.json", "w") as file:
    json.dump(data, file)

print("-----------------------------------------------------------------------------------------------")

data = {"name": "Angelina", "age": 25}
data_str = json.dumps(data)
print(data_str)
print(type(data_str))

print("-----------------------------------------------------------------------------------------------")

json_new = {"name": "Alex", "age": 28}
with open("text3.json", "w") as file:
    json.dump(json_new, file)

print("-----------------------------------------------------------------------------------------------")

with open("text3.json", "r") as file:
    json_file = json.load(file)
    print(json_file)





import json

print("Input your file path.")
file_path = input()

with open (file_path, "r") as file:
    print(file.readlines())


with open (file_path, "r") as file:
    attributes = json.load(file)

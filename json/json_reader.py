import json

users = {}
with open("users.json") as f:
    users = json.load(f)
print(users["username"])
print(users["password"])

users["password"] = "ice-god1234"
with open("users.json", "w") as f:
    json.dump(users, f)
print("The new password is: " + users["password"])
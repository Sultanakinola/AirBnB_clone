#!/usr/bin/python3
a = "User.all()"
parts = a.split(".")
parts[-1] = parts[-1].replace(")", "").replace("(", "")
print(parts[0])
print(parts[1])

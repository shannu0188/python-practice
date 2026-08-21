str = "python"

print(str[0:3])
print(str[:])
print(str[::2])
print(str[2:5])
print(str[::-1])

sliced = str[0:3]
print(id(str) == id(sliced))

print("line 1\nline 2")
print("name:\t onedrive")
print(r"C:\onedrive\documents\github\python")
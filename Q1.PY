user_input = input("enter a string that contains both letters and numbers :e.g.Py2th0on3: ")
print(user_input)
letters = []
numbers = []
for char in user_input:
    if char.isdigit():
        numbers.append(int(char))
    else:
        letters.append(char)
print(letters)
print(sum(numbers))
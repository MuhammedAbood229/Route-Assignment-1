"""
Ask the user to input two separate lists of names (comma-separated). 
Create a third list that contains only the names that appear in both lists. 
• Example Input: List 1: "Ali, Ben, Sara", List 2: "Ben, Joy, Ali" 
• Example Output: Common names: ['Ali', 'Ben'] 
"""
list_1 = []
list_2 = []
common = []
flag = True
char = print("Enter 2 list of names: : ")
while flag:
    name_1 = input("enter name to added in list 1? ")
    name_2 = input("enter name to added in list 2? ")
    list_1.append(name_1)
    list_2.append(name_2)
    char = input("do you want to enter another name in list: y or n: ")
    if char == "n":
        flag = False

#catch common
for name1 in list_1:
    for name2 in list_2:
        if name1 == name2 and name_1 not in common:
            common.append(name1)

print(f"Common names: {common}")
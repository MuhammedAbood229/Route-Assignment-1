"""
7. Ask for a multi-digit number. 
Sum its digits. 
If the result is more than one digit, keep summing the digits until you get a single-digit result. 
• Example Input: 98 
• Example Output: Digital Root: 8 (9+8=17, 1+7=8) 
"""

num = input("Enter Multi digit Number: ")
while len(num) > 1:
    sum = 0
    for i in num:
        sum += int(i)

    num = str(sum) #to check str length again

print(num) 
    


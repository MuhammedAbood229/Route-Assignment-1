"""
9. Ask the user for a number $n$. 
Calculate the factorial (n!) using a loop, 
and then check if the resulting factorial is divisible by the sum of numbers from 1 to $n$. 
• Example Input: 4 
• Example Output: Factorial is 24, Sum is 10. 24 is not divisible by 10. """


n = int(input("Enter number: "))
factorial = 1
sum = 0
for i in range(1, n+1):
    factorial *= i
    sum += i

if factorial % sum == 0:
    print(f"Factorial is {factorial}, Sum is {sum}. {factorial} is divisible by {sum}.")
else:
    print(f"Factorial is {factorial}, Sum is {sum}. {factorial} is not divisible by {sum}.")

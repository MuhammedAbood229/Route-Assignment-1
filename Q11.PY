"""
11.
Check if a full sentence is a palindrome, ignoring spaces and capitalization. 
• Example Input: "Race car" 
• Example Output: True """


sentence = input("Enter a sentence: ")

sentence = sentence.lower().replace(" ", "")

if sentence == sentence[::-1]:
    print(True)
else:
    print(False)
"""
6. Ask the user for two words of the same length. 
Create a new string by interleaving their characters (one from the first word, one from the second).
• Example Input: word1 = "abc", word2 = "xyz" 
• Example Output: "axbycz" 
"""
word1 = input("Enter first word: ")
word2 = input("Enter Second word: ")
interleaving_word = ""

if len(word1) == len(word2):
    for i in range(len(word1)):
        interleaving_word +=word1[i]
        interleaving_word += word2[i]
    print(interleaving_word)
else:
    print("words must be at the same length!!")

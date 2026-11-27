"""
8. Given a list of numbers with many duplicates, 
return a list of tuples showing each unique element and its frequency (how many times it appeared). 
• Example Input: [1, 1, 2, 3, 3, 3, 4] 
• Example Output: [(1, 2), (2, 1), (3, 3), (4, 1)] 
"""

list1 = [1, 1, 2, 3, 3, 3, 4]
list2 = []
for i in range(len(list1)):
    counter = 0
    if (list1[i] not in list1[:i] ): # to prevent duplicates, as it might appeared before so we will not count it again..
        for j in range(len(list1)):
            if list1[i] == list1[j]:
                counter+=1
        list2.append((list1[i],counter)) #tuple 

print(list2)
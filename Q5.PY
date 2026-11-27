"""
5. Create a dictionary where keys are student names and values are lists of 3 test scores. 
Write a program that calculates the average for each student. 
If the average is > 90, print the student's name followed by "Honor Roll." 
• Example Input: {'Sam': [95, 90, 92]} 
• Example Output: Sam: Average 92.3 - Honor Roll """

student_scores = {
    "a": [97,95,80],
    "b": [40,92,60],
    "c": [70,93,90]
}

for key,value in student_scores.items():
    student_average = sum(student_scores[key]) / len(student_scores[key])
    if student_average > 90:
        print(f" {key}: Average {student_average} - Honor Roll")
    else:
        print(f" {key}: Average {student_average}")
        
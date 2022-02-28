'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Example:
     marks key: value pairs are
    'alpha': [20,30,40]
    'beta': [30,50,70]
    query_name = 'beta'
The query_name is 'beta'. beta's average score is (20+50+70)/3 = 50.
Input Format:
             The first line contains the integer n, the number of students' records. The next n lines contain the names 
             and marks obtained by a student, each value separated by a space. The final line contains query_name, 
             the name of a student to query
Constraints:
            0<=n<=10
            0<=marks[i]<=100
            length of marks array=3

Output Format:
             Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
marks=0
for i in student_marks[query_name]:
    marks=marks+i
    avg=marks/3
print("%.2f"%avg)

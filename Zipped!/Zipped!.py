#Zipped!


# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = list(map(int, input().split()))

marks=[]
for i in range(x):
    marks.append(map(float, input().split()))

student_marks = zip(*marks)

average_marks = lambda tu: sum(tu) / x

for tu in student_marks:
    print(average_marks(tu))

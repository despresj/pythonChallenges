def fancyfn(query_name, n):
    marks = student_marks[query_name]
    sumMarks = sum(marks)
    avg = sumMarks/n
    round(avg, 2)
    print(avg)
    
len(student_marks)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

fancyfn(query_name, n)

x = round(5, 2)
print(x)

"{:.2f}".format(x)
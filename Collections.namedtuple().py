from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    columns = input().split()
    Student = namedtuple('Student', columns)
    total_marks = 0
    
    for _ in range(n):
        data = input().split()
        student = Student(*data)
        total_marks += int(student.MARKS)
    
    print(f"{total_marks / n:.2f}")


student_tuples = [('john', 'A', 15),
   ('jane', 'B', 12),
   ('dave', 'B', 10),]

sorted(student_tuples, key=lambda student: student[2])

print(student_tuples)


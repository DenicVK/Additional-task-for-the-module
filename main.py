grades = [[5, 3, 2, 5], [4, 4, 5, 3], [4, 3, 5, 3], [5, 5, 5, 5, 4], [4, 3, 4, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
GPA_studens=dict()
GPA_studens.update({students[4]:sum(grades[0])/len(grades[0]),
                     students[1]:sum(grades[1])/len(grades[1]),
                     students[0]:sum(grades[2])/len(grades[2]),
                     students[3]:sum(grades[3])/len(grades[3]),
                     students[2]:sum(grades[4])/len(grades[4])})
print(GPA_studens)

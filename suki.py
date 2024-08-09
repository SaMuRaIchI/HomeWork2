#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#input_grades = input("Введите оченки через запятую: ")
#grades_list = input_grades.split(',')
#grades = [int(grade.strip()) for grade in grades_list ]
#total_sum = sum(grades)
#total_count = len(grades)
#averege_grade = total_sum/total_count
#print('Сумма оченок: ', total_sum)
#print('Количество оченок:',total_count)
#print('Средний бал:',averege_grade)
                                                 # Тут я не понял как мне с именами соеденить


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
all_students=dict()
all_students.update({students[4]:sum(grades[0])/len(grades[0]),
                     students[1]:sum(grades[1])/len(grades[1]),
                     students[0]:sum(grades[2])/len(grades[2]),
                     students[3]:sum(grades[3])/len(grades[3]),
                     students[2]:sum(grades[4])/len(grades[4])})
print(all_students)
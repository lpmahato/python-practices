# writing a file
import csv

with open('./File_Handling/employees.csv', 'w') as file:
    write_obj = csv.writer(file)
    write_obj.writerow(['Empno', 'Ename', 'Salary'])
    write_obj.writerow([101, 'Adam', 1200.00])
    print(write_obj)





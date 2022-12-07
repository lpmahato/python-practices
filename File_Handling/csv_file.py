# Reading data from a csv file
import csv

with open('./File_Handling/data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    print('read: ', csv_reader)
    for i in csv_reader:
        print('\t'.join(i))


# Writing data to a csv file
with open('./File_Handling/employees.csv', 'w') as file:
    write_obj = csv.writer(file)
    write_obj.writerow(['Empno', 'Ename', 'Salary'])
    write_obj.writerow([101, 'Adam', 1200.00])
    print(write_obj)
# writing a file
import os

# Create empty file
file = open('./File_Handling/sample.txt', 'w')
file.close()
#--------------------------------------------------
# Create file with data
with open('./File_Handling/sample.txt', 'w') as file:
    file.write('This is a sample file.\n')
    file.write('This is a new line')

#--------------------------------------------------
#--------------------------------------------------
# Reading file
file = open('./File_Handling/sample.txt', 'r')
print(file.read())
file.close()

#--------------------------------------------------
try:
    file = open('./File_Handling/data.txt', 'r')
    contents = file.read()
    print(contents)
except Exception as e:
    print(str(e))
finally:
    file.close()
    print(file.closed)
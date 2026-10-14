# Task 1
with open('Week 9/file lab/file lab.txt','r') as file:
    contents=file.read()
    print(contents)

# Task 2
with open('Week 9/file lab/New File lab.txt','w') as file:
    file.write(':)')
    print(file)

# Task 3
with open('Week 9/file lab/file lab.txt','a') as file:
    file.write(':).\n')
    print(file)
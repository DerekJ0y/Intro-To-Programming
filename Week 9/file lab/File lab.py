# Task 1
with open('Week 9/file lab/file lab.txt','r') as file1:
    contents1=file1.read()
    print(contents1)

# Task 2
with open('Week 9/file lab/New File lab.txt','w') as file2:
    file2.write(':)')

# Task 3
with open('Week 9/file lab/file lab.txt','a') as file3:
    file3.write('\n:)')
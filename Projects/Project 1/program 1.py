# budget calculator
income=float(input('what is your average monthly income: ')) #asking for user imput for there monthly income, there rent, there grocery bill, other daily exspences, and what percent they want to put in saving and them giving them a total on there remaining balence 
save_percent= float(input('what persent of your income do you want to save: '))
amount_saved=income/save_percent
rent=float(input('how much is your monthly rent: '))
grocery_bill=float(input('what is your average grocery bill: '))
other_expences=float(input('what is your average other expences like phone bill: '))

sum=((((income-amount_saved)-rent)-grocery_bill)-other_expences)
print(sum)
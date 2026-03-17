#1
joiner = 'Thirty','Days','of','Python'
result = ' '.join(joiner)
print(result)
#2
joiner_2 = 'Coding','for','all'
result_2 = ' '.join(joiner_2)
print(result_2)
#3
company = "coding for all"
#4
print(company)
#5
print(len(company))
#6
print(company.lower())
#7
print(company.upper())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[0:1])
#10
print("coding" in company)
#11
print(company.replace("coding","python"))
#12
#unclear weather I must declare a new string but I will
company_2 = "python for everyone"
print(company_2.replace('everyone',"all"))
#13
print(company.split(" "))
#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
#15
print(company[0:1])
#16
print(company[-1::1])
#17
print(company[9:10])
#18
acronym = "".join(word[0].upper() for word in company_2.split())
print(acronym)
#19
acronym_2 = "".join(word[0].upper() for word in company.split())
print(acronym_2)
#20
Q20 = "c"
print(company.rindex(Q20))
#21
Q21 = "f"
print(company.rindex(Q21))
#22
Q22 = "l"
print(company.rfind(Q22))
#23
Q23 = 'You cannot end a sentence with because because because is a conjunction'
print(Q23.find('because'))
#24
Q24 = 'You cannot end a sentence with because because because is a conjunction'
print(Q24.rindex("because"))
#25
print(Q24.replace('because because because',""))
#26
print(Q23.find('because'))
#27
#This is a repeat question
print(Q24.replace('because because because',""))
#28
print(company.startswith('Coding'))
#29
print(company.startswith('coding'))
#30
company_expanded = '\t coding for all \t'
print(company_expanded.expandtabs(10))
#31
#Question unclear assuming question is going over example 
challenge = '30DaysOfPython'
print(challenge.isidentifier()) 
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())
print('therefore thirty_days_of_python will apear true since it doesnt contain a number')
#32
python_libraries = ('Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon')
print(python_libraries[1:5])
#33
print('I am enjoying this challenge.\nI just wonder what is next.')
#34
tab_escape = 'name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(tab_escape.expandtabs(10))
#35
Q35 = 'radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.'
print(Q35)
#36
A = 8
B = 6
print('{} + {} = {}'.format(A,B , A + B))
print('{} - {} = {}'.format(A,B , A - B))
print('{} * {} = {}'.format(A,B , A * B))
print('{} / {} = {}'.format(A,B , A / B))
print('{} % {} = {}'.format(A,B , A % B))
print('{} // {} = {}'.format(A,B , A // B))
print('{} ** {} = {}'.format(A,B , A ** B))
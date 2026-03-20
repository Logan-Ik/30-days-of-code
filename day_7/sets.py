# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(it_companies)
#1
print(len(it_companies))
#2
new_company = "Twitter"
it_companies.update(new_company)
print(it_companies)
#3
multiple_tech_companies = 'Nvidia','Accenture', 'IBM', 'Oracle', 'SAP'
it_companies.update(multiple_tech_companies) 
print(it_companies)
#4
it_companies.pop()
print(it_companies)
#5
"""
remove produces errors when an item that isnt there is marked for removal
while discard doesnt produce any errors 
Remove is great for checking
"""

#Excercise level 2

#1
A.update(B)
print(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.update(B))
print(B.update(A))
print(A.symmetric_difference(B))
del A,B

#Excercise level 3

#1
print(len(age))
age = set(age)
print(len(age))

#2
"""
The diffrences between a string, list, tuple and set:
String: a string is a sequence of characters which is ordered, immutable and a use case
list: a list is an ordered, mutable collection that allows duplicate elements.   
Tuple: a tuple is an ordered, immutable collection that allows duplicates 
Set:This is data which is mutable aside from its elements. It doesnt allow Duplicates or indexing. 
It is not ordered the same way as a list string or tuple and it uses these brackets{} 
"""

#3
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Count:", len(unique_words))
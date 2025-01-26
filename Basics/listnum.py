#lists
num=[1,20,35,46,75,86]
print(max(num))
print(min(num))

#Dictionary

students = {'bob' : 12, 'alex' :13}
print(students['alex'])

print(students.keys)
print(students.values)

students['alex']=15
del students['bob']
print(students)
print(len(students))

#tuples are immutable cannot be modified, if we modify beyond that then it shows error
tuples = ('orange', 'mango')

#tuples are used to protect data it contains
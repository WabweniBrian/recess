#declaring a list
students = ['Frank', "martha", "Daphne", "edigar"]
print (students)

students = ['Frank', "martha", "Daphne", "edigar", "Daphne", "martha"]
print(students)
#length
print(len(students))
#type
print (type(students))

#accessing the items items
print(students[2])
print (students[-1])
print (students[-3])

students[1] = 'omaley'
print(students)
#add an item at the end
students.append('Jennifer')
print(students)

print(students[3:5])
print(students[:])

print(students[:5])

print(students[2:])

students.insert(3, 'Brian')
print(students)
#removing an item
students.remove("Daphne")
print(students)
#removing an item using an index
students.pop(3)
print(students)

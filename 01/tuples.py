#store items in a single list
#are ordered and unchangeable

phones = ("Samsung", "iphone", "tecno", "Samsung")
print(phones)

#using len on the tuple
print(len(phones))#output 4

#accessing items in the tuple
print(phones)
#accessing items at index 1
print(phones[1])
#accessing items at index 3
print(phones[3])
#accessing the second item from the back
print (phones[-2])
#accessing all the items
print(phones[:])
#accessing all items starting from the second one
print(phones[1:])
#accessing all items to the 3rd item exclusive
print(phones[:2])


#adding two tuples
fruits = ("oranges", "lemons", "aples")
more_fruits = ("banana", "pineapple", "watermelon")

fruits += more_fruits
print(fruits)
#using a for loop to print a tuple
for y in phones:
    print(y)


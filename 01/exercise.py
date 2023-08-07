#tuples

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

#sets
#exercise find the length of the set, datatype, accessing items in the set, add items, adding two sets together

#find the length of the set
fruits= {"oranges", "lemons", "aples", "berries", "cherries"}
print(len(fruits))

#find dataType
print(type(fruits))

#access elements in the set
for y in fruits:
    print(y)
# or
print("banana" in fruits)


#adding items
fruits.add("passion fruits")
print(fruits)

#adding two sets together
carset1 = {"toyota", "ford", "benz"}
carset2 = {"Volvo", "BMW", "Audi"}

cars = carset1 | carset2
print(cars)
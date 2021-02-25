name = input("enter your name:")
age = int(input("enter age:"))

print("hello my name is " + name + "and i am " + str(age) + " years old")
print("hello my name is", name, "and i am", age, "years old")
print("hello my name is %s and i am %d years old" % (name, age))
print("hell0 my name is {} and i am {} years old".format(name, age))
print(f"hello my name is {name} and i am {age} years old")


'''
  6. Solve each of the following problems using Python Scripts.
   Make sure you use appropriate variable names and comments.
   When there is a final answer have Python print it to the screen.
    A person’s body mass index (BMI) is defined as: BMI=mass in kg / (height in m)2
'''

mass = float(input("enter the mass of person in kg: "))
height = float(input("enter the height of a person in meter: "))
BMI = (mass / (height * height))
print(f"The BMI index of a person is {BMI}")


'''
4. Given three integers, print the smallest one. (Three integers should be user input)
'''

first_num = int(input("enter the first value: "))
second_num = int(input("enter the second value: "))
third_num = int(input("enter the third value: "))
if first_num<second_num and first_num<third_num:
    print(first_num,"is smaller number than",second_num,"and",third_num)
elif second_num < first_num and second_num<third_num:
    print(second_num, "is smaller than",first_num,"and",third_num)
else:
    print(third_num,"is smaller number than",first_num,"and",second_num)



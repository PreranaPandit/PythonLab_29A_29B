'''
 10. Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

second = int(input("Enter the value for seconds: "))

day = (((second//60)//60)//24)
print(f"Total day for given seconds: {day}")

hour = ((second//60)//60)
print(f"Total hours for given seconds: {hour}")

minute = (second // 60)
print(f"Total minute for given seconds: {minute}")
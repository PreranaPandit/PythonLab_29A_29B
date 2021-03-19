'''
2.  WAP which accepts marks of four subjects and display total marks, percentage and grade.
 Hint: more than 70% –> distinction,
 more than 60% –> first,
 more than 40% –> pass,
 less than 40% –> fail
'''

p=float(input("enter marks for physics: "))
c=float(input("enter marks for chemistry: "))
b=float(input("enter marks for biology: "))
m=float(input("enter marks for maths: "))

totalmarks=p+c+b+m
print("Total score is ",totalmarks)

percentage=(totalmarks/400)*100
print("total percent is ",percentage,"%")

if percentage>70:
    print("he got distinction ")
elif percentage>60:
    print("he got first division")
elif percentage>40:
    print("he passed the exam")
else:
    print("he is failed")
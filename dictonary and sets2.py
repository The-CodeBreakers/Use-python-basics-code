number=[]
for i in range(8):
    
    num=int(input("Enter the number = "))
    number.append(num)
    
unque_number=set(number)

print("Unque_number ")

for num in unque_number:
    print(num)
bill = []
num = 0
sum = 0

while (True):
    
    a = input("Enter the number is")
    if a == "y":
        break
    else:
        sum = sum+ int(a)
        print(sum)
        bill.append(a)
for i in range(len(bill)):
    print(i)
    
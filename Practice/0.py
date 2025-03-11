n = [1,2,3,4,[7,6]]
# print(n[4][1])
print("before")
for i in n:
    print(i)
print("after")
i = 0
for i in range(4):
    print(n[i])
    i+=1
    if i== 4:
        for j in n[4]:
            print(j)

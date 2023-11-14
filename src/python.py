a=int(input("Enter the base value: "))
b=int(input("Enter the expo value: "))
i=1
expo=1
while i<=b:
    expo=expo*a
    i+=1
print(a,"^",b,"=",expo)
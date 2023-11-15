x=int(input("Enter the value1 = "))
y=int(input("Enter the value2 = "))
i=1
hcf=1
while i<=x or i<=y:
    if x%i==0 and y%i==0:
        hcf=i
    i+=1
print(hcf)
lcm=hcf*(x//hcf)*(y//hcf)
print()

#Above code is completed

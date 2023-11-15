num=int(input("Enter the integers: "))
even_sum=0
odd_sum=0
for i in range(1,num+1):
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
print("sum of even integers: ",even_sum)
print("sum of odd integers : ",odd_sum)
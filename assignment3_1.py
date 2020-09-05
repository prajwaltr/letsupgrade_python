lower=1042000
upper=7026488265
for num in range(lower,upper+1):
   l=len(str(num))
   temp = num
   sum=0
   while temp>0:
       x=temp%10
       sum+=x**l
       temp//=10  #temp =temp//10 [ex-> 121//10=12]
   if num == sum:
      print("the first armstrong number is" , num)
      break

for num in range(1,200):
   if(num<=1):
      continue
   for i in range(2,num):
       if(num%i==0):
            break
   else:
        print(num)

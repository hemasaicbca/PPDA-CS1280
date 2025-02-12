n= int(input("Enter the maximum number of letters in the middle row:"))
for i in range(1,n+1,2) 
   print("".join(chr(65+j)for j in range(i))) 
   for i in range(n-2,0,-2): 
      print("".join(chr(65+j)for j in range(i)))

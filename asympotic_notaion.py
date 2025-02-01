def printnumber(number):
  literation=0
  print("The total number ",number)
  literation+=1
  print("The literation is: ",literation)
  
printnumber(20)
printnumber(5)
#time complexity = O(1)
#best case scenario

def Ontime(n):
  iteration1=0
  for i in range(1,n+1):
    iteration1 += 1
  print("Iteration", iteration1)

Ontime(4)
Ontime(8)
#time complexity = O(n)
#Average Case scenario

def test(n):
  iteration=0
  for i in range(n):
    for j in range(n):
      print("*", end="")
      iteration+=1
    print(" ")
  print("The number of iterations for n is: ", iteration)
      
test(5)
test(3)
#the time complexity is O(n^2).
#worst case scenario
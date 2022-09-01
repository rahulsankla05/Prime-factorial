#  "Brute Force Approach for Prime fac of a number"
N=int(input("Number:"))   # I/P a number
for i in range(2,N):    # run a loop from 2-->N-1
    if N%i==0:     #if N is completely divided by i
        coun=0     # consider coun integer as a exponent value of divisor
        while N%i==0:  # run a while loop if number is divisible 
            N=N//i     # divide num 
            coun+=1   # increamen coun value +1 each 
        print(i,"^",coun)
if N>1:  # if N==prime number 
    print(N,"^",1)
# T.C: O(N)
# S.C: O(1)

# //Optimised way//   
#  // Prime fac of number\\
N=int(input("Number:"))
for i in range(2,int(N**(0.5))+1):
    if N%i==0:     
        coun=0     
        while N%i==0:   
            N=N//i     # divide num 
            coun+=1   # increamen coun value +1 each 
        print(i,"^",coun)

if N>1:   # if N==prime number
    print(N,"&",1) 
# T.C: O(Root N)
# S.C: O(1)

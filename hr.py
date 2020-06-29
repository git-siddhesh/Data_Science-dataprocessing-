#print("Enter the no of test cases\n")
T = int(input())
for i in range(0,T):
    #print("Enter the no of checkpoints\n")
    N = int(input())
    tcost = 0
    c = []  
    l =[]
    #print("Enter cost the liter req\n")
    s=input().split()
    t=input().split()
    for j in range(0,N):
        c.append(int(s[j]))
    m=c[0]
    for j in range(1,N):
         m = min(c[j],m)
         c[j] = m
    for j in range(0,N):
        l.append(int(t[j]))
    #C = list(map(int,input("\nEnter the numbers : ").strip().split()))
    #L = list(map(int,input("\nEnter the numbers : ").strip().split()))
    for j in range(0,N):
        tcost+=c[j]*l[j]
    print(tcost)
    
num=int(input("Enter no of production-"))
p=[]
new_p=[]
flag,count=0,0
for i in range(num):
    p.append(input("Enter production "))
for i in range(num):
    if p[i][0]==p[i][2]:
        flag+=1
        if(flag==1):
            print("Recursion-")
            for j in range(num):
                if(p[i][0]==p[j][0] and p[i][2:]!=p[j][2:]):
                    count+=2
                    x1=(p[i][0],"=",p[j][2:],p[i][0],"'")
                    new_p.append(x1)
                    x2=(p[i][0],"'=",p[i][3:],p[i][0],"'")
                    new_p.append(x2)
            flag=0
    else:
        count+=1
        new_p.append(p[i][:])
for i in range(count):
    print("".join(new_p[i]))
        


    

n=int(input("enter number of sub:"))
marks=[]
for i in range(0,n):
    a=int(input("enter marks:"))
    marks.append(a)
    avg=sum(marks)/n
    print(avg)


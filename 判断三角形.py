a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and c+b>a:
    print("三边可以组成三角形")
else:
    print("不成立")
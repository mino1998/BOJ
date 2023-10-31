import sys

def input():
    return sys.stdin.readline().rstrip()
def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)
n=int(input())
li=list(map(int, input().split()))
outputs=list()
gcd=li[0]
for i in range(n):
    gcd=GCD(gcd,li[i])
x=1
while x*x<=gcd:
    if gcd%x==0:
        outputs.append(x)
        if x*x !=gcd:
            outputs.append(gcd//x)
    x+=1
outputs.sort()
print(*outputs)
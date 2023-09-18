a, b = map(int, input().split())
cooking = int(input())

if(b + cooking >= 60):
    hour = (b + cooking)//60
    b= (b + cooking)%60
    a += hour
    if(a >= 24):
        a = a%24

else:
    b = b + cooking
    if(a >= 24):
        a = a%24

print(a ,b)
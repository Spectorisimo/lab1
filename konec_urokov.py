n=int(input())
time = 9*60
for i in range(1,n+1):
    if i==n:
        time+=45
    elif i%2==0:
        time+=60
    else:
        time+=50
print(time//60,time%60)
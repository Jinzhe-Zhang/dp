import re
import random
def cfun(d):
    return str(eval('cans'+d.group(1)))#39
def sfun(d):
    return " ".join(str(eval('random.sample(range('+d.group(1)+','+d.group(2)+'),'+d.group(3)+')')))#100
def rfun(d):
    return str(eval('random.randrange('+d.group(1)+')'))#56
def gefun(d):
    return (d.group(2)*eval(d.group(1)))[:-1]#46
def fun(d):
    d=re.sub('c(\\[[0-9]+\\]\\[[0-9]+\\])',cfun,d)#50
    d=re.sub('s\\(([0-9]+),([0-9]+),([0-9]+)\\)',sfun,d)#56
    d=re.sub('r\\((.*?)\\)',rfun,d)#35
    d=re.sub('([0-9]+)ge(.*?)',gefun,d)#40
    cans[-1].append(eval(d))#28
    return str(cans[-1][-1])
def funn(d):
    d=re.sub('c(\\[[0-9]+\\]\\[[0-9]+\\])',cfun,d)
    d=re.sub('s\\(([0-9]+),([0-9]+),([0-9]+)\\)',sfun,d)
    d=re.sub('r\\((.*?)\\)',rfun,d)
    d=re.sub('([0-9]+)ge(.*?)',gefun,d)
    return d#去掉一行，改return
shujin=[]
wj1=input("file")
wj2=wj1+'p'
wj1=open(wj1+".py").read()#26
wj1=re.sub('print *?\\((.*?)\\)','dpbl1.extend([\g<1>])',wj1)#61
wj1=wj1.replace("input()","next(canshu1)")#42
wj2=open(wj2+".py").read()#26
wj2=re.sub('print *?\\((.*?)\\)','dpbl2.extend([\g<1>])',wj2)#61
wj2=wj2.replace("input()","next(canshu2)")#42
while True:
    shujin.append(input().split())#34
    if not shujin[-1]:
        shujin.pop()
        break
for _ in range(99):
    dpbl1=[]
    dpbl2=[]
    canshu=[]
    cans=[]
    for shuj in shujin:
        for _ in range(eval(funn(shuj[0]))):#44
            cans.append([])#27
            canshu.append(" ".join(map(fun,shuj[1:])))#54
    canshu1=iter(canshu)#24
    canshu2=iter(canshu)
    exec(wj1)
    exec(wj2)
    if dpbl1!=dpbl2:
        print("Error","\n".join(canshu),dpbl1,dpbl2)#52
        break
    print (".",end="")#22

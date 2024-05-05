import matplotlib.pyplot as py
x=[1,2,3,4,5]
y=[3,4,5,5,3]
lx=len(x)
ly=len(y)
ki=[]
z={}
sum=[]
for k in range(0,lx): 
    summation=0
    for n in range(len(x)):
        if n+k<len(y):
            summation+=x[n]*y[n+k]
    sum.append(summation)
    ki.append(k)
    z[k]=summation
print(z)
py.plot(sum,ki)
py.show()
num=[]

num1=[1,2,3,"abc"]

num2=(1,2,3,"abc")

num2=list(num2)
#%%
L=[3,6,9,12,15,18,21,24,27,30]
del L[2]
del L[3]
print(L)

#%%
[1,3.5,"咩噗"]==["咩噗",3.5,1]
[1,2,3]==[3,2,1]

#%%
print(3 in [1,2,3,4,5])

print("咩噗"in ["動不動咩噗","女神回歸加油"])

print("動不動咩噗"in ["動不動咩噗","女神回歸加油"])
#%%
L=[5,10,15,20,25,30,35,40,45]
L[1:5]
L[2:-2]
#%%
listc=[i for i in range(10)]
print(listc)

listc2=[j+3 for j in range(10)]
print(listc2)
#%%
print(sum([1,3,5,7,9]))       
#%%
num1=[1,3,5,7,9]
num2=[2,5,8,11,14]
num1.append(11)
print(num1)
num1.extend(num2)
print(num1)
num1.count(11)
num1.index(9)
num1.insert(3,999)
print(num1)
num1.pop()
print(num1)
num1.remove(5)
print(num1)
num1.reverse()
print(num1) 
num.pop(5)
print(num1)
#%%
a=(3,5,2,6)
b=()
c=(2,[4,6],(10,11,12))
d=a[1]
e=a[1:3]
f=c[1][1]
#%%
S1={1,2,3,4,5}
S2={3,4,5,6,7}
print(S1-S2)
#%%
A={1,5,3,7,9,5,9,7,3}
print(len(A))
print(max(A))
print(min(A))
print(sum(A))
#%%
X={"A":512,"B":305}
Y={"B":305,"A":512}
print(X==Y)
print(X)
print(Y)
#%%
A={"one":1,"two":2,"three":3}
del A["one"]
print(A)
#%%
A={"one":1,"two":2,"three":3}
X=A["one"]
print(X)

A["two"]=200
print(A["two"])
#%%
dic={"X":123,"Y":456,"Z":789}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())













                                                                                                                                         
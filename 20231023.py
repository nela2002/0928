def sayhello(num):
    print("hello!")
    print("hello!")
    print("hello!")
    
sayhello(1.5>2)
#print("Time 1")
#sayhello()
#print("Time 2")
#sayhello()
#print("Time 3")
#%%
def CtoF1(degreeC):
    degreeF = degreeC * 1.8 + 32
    print("攝氏",degreeC, "度可以轉換成華氏", degreeF,"度")
temperatureC = eval(input("請輸入攝氏溫度:"))
CtoF1(temperatureC)
#%%
def teaTime(dessert,drink = "紅茶"):
    print("我的甜點:",dessert,";飲料:",drink, sep="")
teaTime("舒芙蕾","百香果汁")
teaTime("銅鑼燒")
teaTime(drink = "鮮奶茶", dessert = "水煎包")
teaTime("鬆餅", drink = "義美奶茶")
#%%
def cal(x,y):
    div = x // y
    mod = x % y
    return div,mod
a,b = cal(120, 7)
print("120除以7的商數為", a,"，餘數為", b)
c,d = cal(250, 15)
print("250除以15的商數為", c, "，餘數為", d)
#%%
score = eval(input("請輸入數學分數(0~100):"))
if score >= 60:
    print("及格!")
else:
    print("不及格!")
#%%
score = eval(input("請輸入數學分數(0~100):"))
if score>= 90:
    print("優等")
elif score >= 80:
    print("甲等")
elif score >= 70:
    print("乙等")
elif score >= 60:
    print("丙等")
else:
    print("不及格")
















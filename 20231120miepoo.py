with open("nela.txt","w") as file:
    file.write("nelaaaaaa\n")
    file.write("abcdefg\n")
    file.write("20231120")
#%%
file= open("data.txt")
data=file.read()
print(data)
file.close()


#%%
import calendar
print(calendar.month(2002,5))

import calendar as cal
print(cal.month(2002,5))

from calendar import month
print(month(2002,5))
#%%
X= eval(input("請輸入被除數X:"))
Y= eval(input("請輸入除數Y:"))
Z=X/Y
print("X除以Y的結果等於",Z)
#%%
   try:
    a=0
    b.split()
    b=0
except:
    c=0
   a
   
   b
#%%
try:
    X= eval(input("請輸入被除數X:"))
    Y= eval(input("請輸入除數Y:"))
    Z=X/Y
except ZeroDivisionError:
    print("除數不得為0")
except Exception as e1:
    print(e1.args)
else:
    print("沒有捕捉到例外!X除以Y的結果等於",Z)
finally:
    print("離開try...except區塊")















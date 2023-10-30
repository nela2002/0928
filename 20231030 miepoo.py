answer=input("請輸入「快樂」的英文:")
while answer.upper()!="HAPPY":
    answer = input("答錯了，請重新輸入「快樂」的英文:")
else:
    print("答對了!")
#%%
for i in range(5):
    print(iz)

name="Bob"
for i in range(len(name)):
    print(i,name[i])
    
name="Bob"
for i in name:
    print(i)
    #%%
answer = input("請輸入「好」的英文:")

while answer.upper()!="GOOD":
    if answer.upper()=="QUIT":
        print("我不玩了!")
        break
        print("Bye!")
    answer = input("答錯了，請重新輸入「好」的英文:")
else:
    print("答對了!")
#%%
file= open("writedata.txt","w")
file.write("寫入資料到檔案\n")
file.write("ABCDE\n")
file.write("12345")
file.close()
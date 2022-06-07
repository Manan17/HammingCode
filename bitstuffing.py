#Bit stuffing 
flag = "01111110"
data = input("Enter Data: ")
count=-1
for i in flag:
    if i == "1":
        count = count + 1
      

stuffedData = ""
stuffedData2=""

for index,ele in enumerate(data):
   stuffedData = stuffedData + ele
   if((index+1) % count == 0 ):
       stuffedData = stuffedData + "0"       

n=0
for ele in data:
    stuffedData2 = stuffedData2 + ele
    if ele == "1":
       n=n+1
   
    if n % count == 0 and n != 0:
        stuffedData2 = stuffedData2 + "0"
        n = 0

    if ele == "0":
        n = 0

print(stuffedData)
print(stuffedData2)

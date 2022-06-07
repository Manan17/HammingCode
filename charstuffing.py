#Char Stuff
length = int(input("Enter length of the data: "))
start = "STX"
flag = "DLE"
end = "ETX"
data = []
for i in range(length):
    ele = input("Enter element: ")
    data.append(ele)

stuffedData = start + flag

for i in data:
    if i == flag:
        stuffedData = stuffedData +" "+ flag
    stuffedData = stuffedData +" "+ i

stuffedData = stuffedData + " " + flag+ end

print(stuffedData)
    

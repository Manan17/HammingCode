data = input("Enter data: ")
count = 0
packets = []

while count < len(data):    
    length = int(data[count])    
    packet = data[count+1:length+count+1]    
    packets.append(packet)
    count = count + length

for index,ele in enumerate(packets):
    print("Frame No. ",index+1,"element : ",ele)

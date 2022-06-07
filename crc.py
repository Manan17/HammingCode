generatingFn = input("Enter Generating Function: ")
data = input("Enter data: ")

gLen = len(generatingFn)
appendedData = data + '0'*(gLen-1)

def xor(dividend,divisor):
    result = []
    for i in range(1,len(dividend)):
        if dividend[i] == divisor[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

def mod2div():
    global gLen,appendedData,generatingFn 
    tmp = appendedData[0:gLen]     
    while gLen < len(appendedData): 
        if tmp[0] =='1':
            tmp = xor(tmp,generatingFn) + appendedData[gLen]  

        else:
            tmp = xor(tmp,'0'*gLen) + appendedData[gLen]

        gLen+=1

    if tmp[0] =='1':
        tmp = xor(tmp,generatingFn)

    else:
        tmp = xor(tmp,'0'*gLen)

    print(tmp)

mod2div()



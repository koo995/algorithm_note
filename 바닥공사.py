n = int(input())


data = [0]*1000
for i in range(1,n+1):
    if i == 1:
        data[i] = 1
    if i == 2:
        data[i] = 3
    else:
        data[i] += data[i-2] * 2
        data[i] += data[i-1] * 1
    
print(data[n] % 796796)

#이것도 역시 점화식? 을 세워서 하는거 같군...
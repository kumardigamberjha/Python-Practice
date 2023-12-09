# arr= {10,20,30,40,50,60,70,80,90,100}
arr = {1,2,3,7,5}

# N = 15
N = 5

# Converting Set To List
l1 = list(arr)
l1.sort()

outval = 12
start = 0
end = 0
s = 0
for i in range(len(l1)):
    for j in range(i, len(l1)):
        s += l1[j]

        if s == outval:
            end = j + 1
            print(j+1)
            break
 
    if s == outval:
        start = i + 1
        print("i: ", i+1)
        break
    else:
        s = 0
print("S: ", s)
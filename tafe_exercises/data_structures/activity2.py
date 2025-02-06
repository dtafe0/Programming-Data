j = "jabberwocky"
a = "alice"
an = " and "
s = j+an+a
sl = s[len(j):len(s)-len(a)]
print(sl)

numberList = [11, 1, 43, 9, 12, 44, 70, 19, 3, 21]
for passCount in range(len(numberList) - 1, 0, -1):
    for i in range(passCount):
        if numberList[i] > numberList[i + 1]:
            temp = numberList[i]
            numberList[i] = numberList[i + 1]
            numberList[i + 1] = temp    

print(numberList)
print(list(range(9, 0, -1)))


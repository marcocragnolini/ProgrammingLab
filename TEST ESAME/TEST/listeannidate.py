listaannidata = [[1,2,3,4],[4,3,2],[5,6,7,8],[8,7,6,5]]
for item in listaannidata:
    sum = 0
    for i in range(len(item)):
        print(item[i])
        sum = sum + item[i]
    print(sum)

print("______")
num = listaannidata[2]
n = num[3]
print(n)
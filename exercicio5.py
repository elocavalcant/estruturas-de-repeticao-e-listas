numeros=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
print(numeros)

for pares in numeros:
    if pares not in "1,3,5,7,9,11,13,15,17,19":
        print("Pares",pares)

for impares in numeros:
    if impares not in "2,4,6,8,10,12,14,16,18,20":
        print ("ímpares",impares)

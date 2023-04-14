populaçãoA = 80000
populaçaoB = 200000
anos = 0


while populaçãoA <= populaçaoB :
    populaçãoA = populaçãoA + (populaçãoA * 0.03)
    populaçaoB = populaçaoB + (populaçaoB * 0.015)
    anos = anos + 1

print (anos)
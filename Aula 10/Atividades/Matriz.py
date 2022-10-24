# 1 = linha  / c = coluna 
mtz = [
    [78, 90, 100, 98, 7],
    [56, 77, 93, 77, 93],
    [10, 4, 73, 77, 93],
    [78, 98, 100, 77, 93],
    [10, 4, 73, 90, 100]
]

for l in range(len(mtz)):
    
    for c in range(len(mtz[l])):
        
        if l == c:
            print(mtz[l][c])

        if (mtz[l][c] % 2) == 0:
            print(f"{mtz[l][c]} -> É par!")
        else:
            print(f"{mtz[l][c]} -> É impar!!")


from random import shuffle

def perm(bits, lst, inp):
    shfflBts = 0
    for x in lst:
        shfflBts <<= 1
        shfflBts ^= (bits >> (inp - x)) & 1
    return shfflBts

PC1 = [57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18, 10, 2, 
59, 51, 43, 35, 27, 19, 11, 3, 60,
52, 44, 36, 63, 55, 47, 39, 31, 23, 
15, 7, 62, 54, 46, 38, 30, 22, 14, 
6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 
20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3,
28, 15, 6, 21, 10, 23, 19, 12, 
4, 26, 8, 16, 7, 27, 20, 13, 2, 
41, 52, 31, 37, 47, 55, 30, 40,
51, 45, 33, 48, 44, 49, 39, 56, 
34, 53, 46, 42, 50, 36, 29, 32]

key1 = int('1F1F1F1F0E0E0E0E', base = 16)
key2 = int('FE01FE01FE01FE01', base = 16)
key3 = int('FAB9D5B8CAB7CBA6', base = 16)

shift1 = list(range(2, 29)) + [1] + list(range(30, 57)) + [29]
shift2 = list(range(3, 29)) + [1, 2] + list(range(31, 57)) + [29, 30]



def roundKeys(key):
    klst = []
    cd = perm(key, PC1, 64)
    for rnd in range(1, 17):
        if rnd in [4, 7, 8, 9, 11, 15]:
            cd = perm(cd, shift1, 56)
        else:
            cd = perm(cd, shift2, 56)
        klst.append(perm(cd, PC2, 56))
    return klst




keys = roundKeys(key1)
for k in keys:
    print(hex(k))

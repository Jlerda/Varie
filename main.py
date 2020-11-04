from math import trunc

def fib(n):
    part_1 = ((5**0.5)/5)

    part_2 = (((1+5**0.5)/2))**n

    part_3 = (((1-5**0.5)/2))**n


    return trunc(part_1*(part_2 - part_3))

def fib_classic(n):
    seq = [0, 1]
    for i in range(n):
        number = seq[-1] + seq[-2]
        seq.append(number)
    return seq[n]

#print(fib(500))

print(fib_classic(800000))



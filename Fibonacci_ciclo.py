from math import trunc

def fib(n): #Binet valida fino al 71esimo numero poi perde accuratezza a causa dell'approssimazione
    part_1 = ((5**0.5)/5)

    part_2 = (((1+5**0.5)/2))**n

    part_3 = (((1-5**0.5)/2))**n


    return trunc(part_1*(part_2 - part_3))

def fib_classic(n): #Iterativa ciclo for
    seq = [0, 1]
    for i in range(n):
        number = seq[-1] + seq[-2]
        seq.append(number)
    return seq[n]


def fibonacci(n): #Iterativa ciclo while
  seq = [0, 1]
  while n > 1 and len(seq)-1 < n:
    seq.append(seq[-1] + seq[-2])
  return seq[n]


def fibonacci(n): #Ricorsiva
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)



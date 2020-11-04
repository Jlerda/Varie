#Il programma calcola tutti i numeri primi minori o uguali dell'intero inserito

n = int(input("Inserire un numero intero positivo: "))
primi = []
while n != 0:
    counter = 0
    for i in range(n+1):
        if not (i == 0 or i == 1 or i == n):
            if n % i == 0:
                counter += 1
                break
    if counter < 1 and n != 1:
        primi.append(n)
    n -= 1

print(primi)

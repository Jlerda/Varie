anno = int(input("Inserire un anno: "))
if (anno%4 == 0 & anno%100 != 0) | (anno%400 == 0):
    print("L'anno inserito è bisestile")
else:
    print("L'anno non è bisestile")

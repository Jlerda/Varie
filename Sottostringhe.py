#Il programma memorizza e stampa tutte le sottostringhe consecutive della stringa inserita
word = input()
substring = []
for i in range(1, len(word)):
    for j in range(len(word)):
        if len(word[j:j+i]) == i:
            substring.append(word[j:j+i])
print(substring)
print(len(substring))

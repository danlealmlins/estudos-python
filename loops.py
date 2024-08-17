# for variável in sequência:
    # Bloco de Código a repetir
    # instruções

frutas = ["maça", "banana", "laranja"]

for frutas in frutas:
    print(frutas)

# while condição:
    # Bloco de código a repetir
    # instruções

contador = 0 

while contador <= 5:

    print(contador)
    contador += 1


print("Números de 1 a 5 multiplicados por 2 usando for:")
for numero in range(1, 6):
    print(numero * 2)

print("Números de 1 a 5 multiplicados por 2 usando while:")
contador = 1
while contador <=5:
    print(contador * 2)
    contador += 1
# Ao usar loops while é muito importante que seja especificado a condição de saída.


# Controle de Loops
# 1- Break

contador = 0 
while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

# 2- Continue

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
# 3- Pass

for i in range(5):
    pass
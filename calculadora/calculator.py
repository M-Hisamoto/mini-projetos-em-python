a = int(input("digite um número:"))
b = int(input("digite outro número:"))
opec = input("qual operação deseja fazer?")
if opec == "soma":
    print(a+b)
elif opec == "subtração":
    print(a-b)
elif opec == "divisão":
    print(a/b)
elif opec == "multiplicação":
    print(a*b)
elif opec == "exponenciação":
    print(a**b)
elif opec == "porcentagem":
    print(b * (a / 100))
if opec == "par ou ímpar":
    ra = a % 2 
    rb = b % 2 
    if ra == 0 and rb == 0:
        print('os dois números são pares')
    elif ra != 0 and rb == 0:
        print(f'o número {a} é ímpar, e o {b} é par')
    elif ra == 0 and rb != 0:
        print(f'o número {b} é ímpar, e o {a} é par')
    elif ra != 0 and rb != 0:
        print('os dois números são ímpares')
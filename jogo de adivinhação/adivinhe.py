import random
from random import randint
ola = input("olá, quer começar?")
num = random.randint(0,10)
if ola == "não":
    print ("ok, até mais.")
elif ola == "sim":
    print("tudo bem vamos começar.\nTente adivinhar o meu número, ele está entre 0 e 10, você trem três tentativas.\nO meu número é x.")
    x1 = int(input("primeira tentativa:"))
if x1 == num: 
        print("que sorte, de primeira\nvocê me venceu:(")
if x1!=num:
    x2 =int(input("que azar, tente novamente:"))
if x2 == num:
    print("parabéns, você venceu que sortudo")
else:
    x3 = int(input("tá difícil?\nSua última chance:"))
if x3 == num:
    print("parabéns, vc ganhou por pouco.")
else:
    print("HAHAHA, mais sorte da pró ima vez, ganhei mais uma.")
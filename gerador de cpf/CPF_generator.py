import random 
a = random.randint(1,9)
b = random.randint(1,9)
c = random.randint(1,9)
d = random.randint(1,9)
e = random.randint(1,9)
f = random.randint(1,9)
g = random.randint(1,9)
h = random.randint(1,9)
i = random.randint(1,9)

multa = a*10
multb = b*9
multc = c*8
multd = d*7
multe = e*6
multf = f*5
multg = g*4
multh = h*3
multi = i*2
soma1 = (multa+multb+multc+multd+multe+multf+multg+multh+multi)
r1 = soma1%11
if r1 == 0 or r1 == 1:
        d1 = 0
        
else:
        d1 = 11-r1

multb2 = b*10
multc2 = c*9
multd2 = d*8
multe2 = e*7
multf2 = f*6
multg2 = g*5
multh2 = h*4
multi2 = i*3
multj2 = d1*2
soma2 = (multb2+multc2+multd2+multe2+multf2+multg2+multh2+multi2+multj2)
r2 = soma2%11
if r2 == 0 or r2 == 1:
        d2 = 0
        
else:
        d2 = 11-r2

print(a, b, c,".", d, e, f,".", g, h, i, "-", d1, d2)

'''HUMPYANG GAME
P1 = YOU (REAL PLAYER)
C2,C3 = (COMPUTER)
P1 = kulob - USER INPUT,
C2 = hayang - RANDOM,
C3 = kulob -  RANDOM '''

from random import randint

ako = input("type hayang or kulob: ")
Com2 = randint(0,1)
Com3 = randint(0,1)

kulob = 1
hayang = 0

if ako == kulob:
    print("ako:kulob")
elif ako == hayang:
    print("ako:hayang")
if Com2 == kulob:
    print("Com2:kulob")
elif Com2 == hayang:
    print("Com2:hayang")
if Com3 == kulob:
    print("Com3:kulob")
elif Com3 == hayang:
    print("Com3:hayang")

if ako == hayang and Com2 == kulob and Com3 == kulob or ako == kulob and Com2 == hayang and Com3 == hayang :
    print("you win")
elif ako == kulob and Com2 == hayang and Com3 == kulob or ako == hayang and Com2 == kulob and Com3 == hayang:
    print("c2 win")
elif ako == kulob and Com2 == kulob and Com3 == hayang or ako == hayang and Com2 == hayang and Com3 == kulob:
    print("c2 win")
else:
    print("draw")
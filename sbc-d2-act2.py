
from random import randint

P1 = int(input("enter 0 hayang to  1 kulob: "))
c2 = randint(0,1)
c3 = randint(0,1)

if P1 == 1:
    print("P1:kulob")
elif P1 == 0:
    print("P1:hayang")
if c2 == 1:
    print("C2:kulob")
elif c2 == 0:
    print("C2:hayang")
if c3 == 1:
    print("C3:kulob")
elif c3 == 0:
    print("C3:hayang")


if P1 == 0 and c2 == 1 and c3 == 1 or P1 == 1 and c2 == 0 and c3 == 0 :
    print("you win")
elif P1 == 1 and c2 == 0 and c3 == 1 or P1 == 0 and c2 == 1 and c3 == 0:
    print("c2 win")
elif P1 == 1 and c2 == 1 and c3 == 0 or P1 == 0 and c2 == 0 and c3 == 1:
    print("c3 win")
else:
    print("draw")

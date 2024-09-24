#Suite de Syracuse
# :

# Prenez un nombre entier positif n.
 #Si n est pair, divisez-le par 2.
#Si n est impair, multipliez-le par 3 et ajoutez 1.
# Répétez le processus avec le nouveau nombre obtenu.
s0=49
print (s0)
while s0 != 1:
    if s0 % 2 ==0:
        s0=s0//2
        print (s0)
    else :
        s0=s0*3+1
        print(s0)
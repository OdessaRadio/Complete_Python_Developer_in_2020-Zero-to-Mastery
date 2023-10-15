# MRO - Method Resolution Order



class A:
    num = 10

class B(A):
    pass
    num = 20

class C(A):
    pass
    num = 30


class D(B,C): #MRO: D->B->C-A
    pass
''' Depth First Search
   A
  / \
 /   \
B ->  C
\    /
 \  /
   D
'''

class E(C,B): #MRO: D->C->B-A
    pass
''' Depth First Search
   A
  / \
 /   \
B <-  C
\    /
 \  /
   D
'''

print(D.num) 
print(E.num) 
D.__str__

print(D.mro())
print(E.mro())


class X:pass
class Y:pass
class Z:pass

class Q(X,Y):pass
class W(Y,Z):pass
class E(W,Q,Z):pass

print(E.__mro__)
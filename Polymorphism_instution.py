"""

"""
"""
MRO: Meyhod resolution order

# Hybrid inhiritance

  P      Q

X     Y      Z

   A     B
   
      C
eg.

class P:
    pass

class Q:
    pass

class X(P):
    pass

class Y(P,Q):
    pass

class Z(Q):
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class C(A,B):
    pass


print(C.mro())
---------------------------------------------------------------------
-   Encapsulation meanse data hiding
-   eg. class

class sample:
    x = 20
    y = 10

print(x,y)
-------------------------------------------------------------------------
-   like other programing language we dont have aceess modifiers:
    public,private,protected
    
            public  private  protected
        
class       yes     yes        yes
outside     yes     no         yes
subclass    yes     no         yes
package     yes     no         yes

-    so we can implement encapsulation using 
    _ underscore convesion   


----------------------------------------------
Case 1:
class sample:
    x = 10
    y = 20
    z = 30

s = sample()
# we can access x,y,z using object bcz they are public
# so variable or method declare by the user without undderscore prefix
# are public one
--------------------------------------------------------------
for protected use single undescore _
for private use double underscore __
-----------------------------------------------------------------


class sample:
    x = 10   # public
    _y = 20  # protected
    __z = 30 # private

s = sample()
print(dir(s))
# accss x and y
print(s.x,s._y)
# to acess privtae member of a class use name mangling technique
print(s._sample__z)

---------------------------------------------------------------------

class Sample:
    def m1(self):
        print("Public Method")
    def _m1(self):
        print("Protected Method")
    def __m1(self):
        print("Private Method")

s = Sample()
s.m1()
s._m1()
s._Sample__m1()
----------------------------------------------------------------
-   Can we modify public,private,protected values

class sample:
    x = 10  # public
    _y = 20  # protected
    __z = 30  # private

s = sample()
s.x = 11
s._y = 22
print(s.__dict__)  # display info present in the object
print(sample.__dict__) # display info present in class

--------------------------------------------------------------

"""
"""
-    "Polymorphism"

-   poly(many) + morphs(forms)
-   one norm has multiple forms called polymorphism
-   operator are best example of it
eg..  

print(10 + 10)  # addition
print('10' + '10') # concatination
----------------------------------------------------------
Types of Polymorphism:
-   1. Operator level polymorphism   # possible
    2. method level polymorphism   # not possiblee
    3. constructorlevel polymorphism  # not possible
"""

"""
-   if we have same name(mehtod) with a diffrent arguments then it is called method level polymorphism
-   it is also called overloding
"""

"""
Method Overloading
-   when we have with a same name and diffrent arguments types

# method overloading eeg.
class Test:
    def show(self,name):
        pass
    def show(self,name,age):
        pass
    def show(self,name,age,salary):
        #pass
        print(name,age,salary)

T = Test()
T.show('Yogesh',33,10000)   # it will call last show method
"""

# technically method overloading not possoble o=in python




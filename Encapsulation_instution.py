""""

"""

"""
encapsulation meanse data hiding
ex.

class test:
    x = 10
    y = 120
    z = 130
    def sample(self):
        print(x+y+z)

print(x+y+z)  # outside class we cant access
#hence we say class is a example of encapsulation
#which hide members of it

----------------------------------------------------------------------------
-   public, private, protected

class sample:
    x = 100
    print('inside a class',x)
    def m1(self):
        print('indise a method',self.x)
s1 = sample()
s1.m1()
print('outside class',s1.x)
---------------------------------------------------
# protected
class sample:
    _y = 300 # protected
    print('Inside a class',_y)
    def m1(self):
        print('inside a method',self._y)

s1 = sample()
s1.m1()
print('Outside a class',s1._y)

class test:
    print('Inside test class',sample._y)

----------------------------------------------------------------

# private

# private: it is available only within a class
class Bank:
    __password = 1234  # private

b = Bank()
print(b.__password)
print(Bank.__password)
----------------------------------------------------------------


# still if user wants to access private member then use name mangling techniues
class Bank:
    __password = 1234  # password

b = Bank()
#print(b.__password) # this will not work/directly access to to private var. prohabited
print(b._Bank__password)
----------------------------------------------------------------
"""

class Sample:
    def m1(self):
        print('Public Method')

    def _m2(self):
        print('Protected Method')

    def __m3(self):
        print('Private Method')

s = Sample()
s.m1() # public method
s._m2() # protected method
s._Sample__m3()  # private method

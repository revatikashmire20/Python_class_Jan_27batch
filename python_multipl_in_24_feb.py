class A(object):

    def fun(self):
        print("a")

class B(A):

    def fun(self):
        print("b")

class C(A):

    def fun(self):
        print("c")

class D(C,B):    #multiple inheritance

    def fun1(self):
        print("d")

d= D()
d.fun()

#method resolution order
#it will give priority to the near by search

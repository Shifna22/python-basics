class A:
    def show(self):
        print("HY")

class B(A):
    def show(self):
        print("hello")
        super().show()

class C(A):
    def show(self):
        print("wow")
        super().show()

class D(B, C):
    def show(self):
        print("woi")
        super().show()


d = D()
d.show()

print(D.mro())
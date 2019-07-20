from rough.A import A


class B(A):
    def m2(self):
        print("in m2")

    def m3(self):
        b1 = B()
        b1.m1()
        #b1.m2()

class A:
    def a(self):
        a = 1
        return a

    def b(self):
        b = 2
        return b


print("program started")
a1 = A()
x = a1.a()
assert x == 1, "not equal"
y = a1.b()
assert y == 2, " in correct"
print("program ended")

class A:
    def __init__(self, a):
        self.a = a

    def reinit(self):
        self.__init__('reinit')


a = A('a')
print(a.a)
a.reinit()
print(a.a)
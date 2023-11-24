#!/usr/bin/env python


class A:
    def show(self):
        print('A')


class B(A):
    def show(self):
        print('B')


class C(A):
    def show(self):
        print('C')


class D(B, C):
    def show(self):
        print('D')
        # I want to access C 'show()'
        # super(C, self).show() # Wrong! super of C is A!
        super(B, self).show()  # Good


class E(C, B):
    def show(self):
        print('D')


def main():
    d = D()
    d.show()
    print(D.mro())
    # Orders are not the same
    print(E.mro())


if __name__ == '__main__':
    main()

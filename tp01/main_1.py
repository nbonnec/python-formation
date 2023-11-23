b = 'tutu'


def local_variable():
    print(f'b= {b}')
    # b = 43 # Nok. If we uncomment, this b takes priority


def global_variable():
    global b
    b = 'toto'


def test():
    # print(a)  # Nok. It is hoisting. 'a' is not undefined, but has no value
    if True:
        a = 2
    print(a)  # Ok, because the scope is the function


if __name__ == '__main__':
    print('Hello')
    print(my_module.a)  # Ugly!
    print(f'b= {b}')
    local_variable()
    print(f'b= {b}')
    global_variable()
    print(f'b= {b}')

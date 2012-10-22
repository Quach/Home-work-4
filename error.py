# -*- coding: utf-8 -*-
"home work 3"

def my_bind3(func, *params):
    "recurce bind"

    def recurce_func(*params_rec):
        params += params_rec
        if func.func_code.co_argcount == (len(params)):
            return func(*params)
        else:
            return recurce_func
    if func.func_code.co_argcount == len(params):
        return func(*params)
    return recurce_func

def main():
    "main"

    def f(a, b, c):
        return [a, b, c]
  
    assert my_bind3(f, 1, 2, 3) == [1, 2, 3]
    f2 = my_bind3(f, 1)
    assert f2(4, 5) == [1, 4, 5]
    assert f2(6, 7) == [1, 6, 7]
    assert f2(9) == f2
    f3 = f2(9)
    assert f3(10) == [1, 9, 10]
    assert f2(9, None) == [1, 9, None]
    print "Bind 3 OK!"

    print "\nPress any key.."
    raw_input()
    return 0


if __name__ == "__main__":
    exit(main())
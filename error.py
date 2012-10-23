# -*- coding: utf-8 -*-
"home work 3"

def my_bind3(func, *param1, **params):
    "recurce bind"
    #func could be optimaze...

    #make from tuple to list for remember
    temp_param = []
    #write in list first params from my_bind3
    for p in param1:
        temp_param.append(p)

    def recurce_func(*param2, **params_rec):
        #local list
        l_param1 = []
        #local dict
        l_param2 = {}
        
        #get remebbered vals to local list and dict
        l_param2.update(params)
        for p1 in temp_param:
            l_param1.append(p1)

        #get new vals to local list and dict
        l_param2.update(params_rec)
        for p1 in param2:
            l_param1.append(p1)

        #if enough to exec func -> exec func, dom't remember new vals
        if func.func_code.co_argcount == (len(l_param1) + len(l_param2)):
            return func(*l_param1, **l_param2)
        #if not enought - remember new vals
        else:
            #rewrite local list and dict to "global"
            for p1 in l_param1[len(temp_param):]:
                temp_param.append(p1)
            params.update(l_param2)
            return recurce_func

    if func.func_code.co_argcount == (len(params) + len(param1)):
        return func(*param1 , **params)

    return recurce_func


def main():
    "main"

    def f(a, b, c):
        return [a, b, c]
  
    assert my_bind3(f, 1, 2, 3) == [1, 2, 3]
    f2 = my_bind3(f, 1)
    assert f2(4, 5) == [1, 4, 5]
    assert f2(6, 7) == [1, 6, 7]
    f3 = f2(9)
    assert f3(None) == [1, 9, None]
    print "Bind 3 OK!"

    print "\nPress any key.."
    raw_input()
    return 0


if __name__ == "__main__":
    exit(main())
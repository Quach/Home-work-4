# -*- coding: utf-8 -*-
"home work 3"

import time

def map_rq(func, iterator):
    "map rererererecursion"

    res = []
    if len(iterator) == 0:
        return res
    res.append(func(iterator[0]))
    res += map_rq(func, iterator[1:])
    return res

def map_yield(func, iterator):
    "map generator"

    for i in iterator:
        yield func(i)

def map_rq_yield(func, iterator):
    "map rereregenerator"
    
    yield func(iterator[0])

    for x in map_rq_yield(func, iterator[1: ]):
        yield x

def my_filter_rq(func, iterator):
    "fififilter"

    res = []
    if len(iterator) == 0:
        return res
    if func(iterator[0]):
        res.append(iterator[0])
    res += my_filter_rq(func, iterator[1:])
    return res

def gh(param):
	"If more than 3"

	return param > 3

def my_reduce_rq(func, sequence):
    "rerereduce"

    if len(sequence) < 2:
        return None
    if len(sequence) == 2:
        return func(sequence[0], sequence[1])
    temp_sequence = []
    temp_sequence.append(func(sequence[0], sequence[1]))
    temp_sequence += sequence[2:]
    return my_reduce_rq(func, temp_sequence)

def my_sum(a, b):
	return a + b

def my_bind(func, *params1):
    "more params"
    def func1(*params2):
        temp_params = params1 + params2
        return func(*temp_params)
    return func1

def test_bind1_func(*param):
    return param

def my_bind2(func, *param1, **param2):
    "more named params"
    def func1(*param3, **param4):
        temp_params = param1 + param3
        temp_params2 = param2
        for i in param4:
            temp_params2[i] = param4[i]
        return func(*temp_params, **temp_params2)
    return func1

def test_bind2_func(a, b, c, d, e, f, g):
    return [a, b, c, d, e, f, g]

#def my_bind3(func, *params2, **params1):
#    "recurce bind"

#    def recurce_func(*params_rec, **params_rec_2):
#        params2 += params_rec
#        for p in params_rec_2:
#            params1[p] = params_rec_2[p]
#        if func.func_code.co_argcount == (len(temp_param) + len(params1)):
#            return func(*params2, **params1)
#        else:
#            return recurce_func
#    if func.func_code.co_argcount == (len(params2) + len(params1)):
#        return func(*params2, **params1)
#    return recurce_func

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

def time_me(func, stat_dict):
    "function with params"
    stat_dict.setdefault('num_calls', 0)
    stat_dict.setdefault('cum_time', 0)
    def decorator(main_func):
        "decorator"

        def wrapper(*args, **kwargs):
            "rapper function to profilling func"

            stat_dict['num_calls'] += 1
            time_1 = func()
            res = main_func(*args, **kwargs)
            time_2 = func()
            stat_dict['cum_time'] += time_2 - time_1
            return res

        return wrapper

    return decorator

def main():
    "main"

    assert map_rq(lambda x : x ** 2, [1, 2, 3]) == [1, 4, 9]
    gen = map_yield(lambda x : x ** 2, [1, 2, 3])
    print "Map recurse OK!"

    assert next(gen) == 1
    assert next(gen) == 4
    assert next(gen) == 9
    print "Map generator OK!"

    gen1 = map_rq_yield(lambda x : x ** 2, [1, 2, 3])
    assert next(gen1) == 1
    assert next(gen1) == 4
    assert next(gen1) == 9
    print "Map recurse generator OK!"

    assert my_filter_rq(gh, (1, 2, 3, 4, 5, 6)) == [4, 5, 6]
    print "Filter recurse OK!"

    assert my_reduce_rq(my_sum, [1,1,1,1,1,1]) == 6
    print "Reduce recurce OK!"

    f1 = my_bind(my_sum, 1)
    assert f1(2) == 3
    f1 = my_bind(my_reduce_rq, my_sum)
    assert f1([1,1,1,1,1]) == 5
    f1 = my_bind(test_bind1_func, 1,2,3)
    assert f1(4, 5, 6) == (1,2,3,4,5,6)
    assert f1() == (1,2,3)
    assert f1(None) == (1,2,3, None)
    f1 = my_bind(test_bind1_func)
    assert f1(1,2,3,4,5,6) == (1,2,3,4,5,6)
    print "Bind 1 OK!"

    f2 = my_bind2(test_bind2_func, 1,2)
    assert f2(3,4,5,6,7) == [1,2,3,4,5,6,7]
    f2 = my_bind2(test_bind2_func, 1, 2, e = 5, f = 6)
    assert f2(3,4,g=7) == [1,2,3,4,5,6,7]
    print "Bind 2 OK!"

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

    statistics = {}
    @time_me(time.clock, statistics)
    def som_func(param_x, param_y):
        "temp fucntion to profill"
        time.sleep(1.1)

    som_func(1, 2)
    som_func(1, 2)

    assert statistics['num_calls'] == 2
    assert 2.5 > statistics['cum_time'] > 2
    print "Decorator OK!"

    print "\nPress any key.."
    raw_input()
    return 0


if __name__ == "__main__":
    exit(main())
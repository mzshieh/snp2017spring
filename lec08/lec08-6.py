def f(a,b,*args,**kwargs):
    print('type of a is {}'.format(type(a)))
    print('type of b is {}'.format(type(b)))
    print('type of args is {}'.format(type(args)))
    print('type of kwargs is {}'.format(type(kwargs)))
    for item in args:
        print('{} is in args'.format(item))
    for item in kwargs.items():
        print('{} is in kwargs'.format(item))
    print(kwargs['height'])
    print(args[1])

f('ab','cd',1,23,456.7,height=177,weight=111.1)

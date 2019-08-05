import logging



#闭包的理解
def use_logging(func):
    '''
    闭包的调用时机，是在使用闭包decorat一个函数的时候
    '''
    print("%s was decorated." % func.__name__)     #表述闭包时机
    def wrapper(*arg, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*arg, **kwargs)
    return wrapper

@use_logging
def bar():
    print("i am bar")

print("before call decorated function.")
bar()




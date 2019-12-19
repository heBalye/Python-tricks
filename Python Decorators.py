# First class function
# Return a function as a result of a function. Note: not a value of a function of a functionn


def logger(meg):

    def log_message():
        print('Log:', meg)

    return log_message


log_hi = logger('Hi')
log_hi()


def html_tag(tag):

    def wrap_text(msg):
        print(f'<{tag}>{msg}<{tag}>')

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test Headline!')  # it remembers the 'h1' argument: clousure?
print_h1('Another Headline!')
print_p = html_tag('p')
print_p('this is a paragrah')

# Closures


def outer_func(msg):
    message = msg

    def inner_func():
        # message here is a free variable since it is not defined in inner_funct but we still can access it.
        print(message)

    return inner_func


func = outer_func('fun?')
# when we down with outer function, the inner function still remember the arugment within it.
# closure: an inner function remembers and has access to the varbles that created in the local scope in which it was created, even if the outer function is finished executing.
hi_func = outer_func('Hi')
hello_func = outer_func('Hello')
hello_func()

# Decorators
# Easily add functionality to exsiting functions without change the structure of exsiting functions.


def decorator_function(original_function):
    def wrapper_function():
        print('something')
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print('display function ran')


display()
# display = decorator_function(display)

# decorators class version


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method something')
        return self.original_function(*args, **kwargs)


@decorator_class
def display1():
    print('display function ran')

def new_decorator(new_func):
    def wrap_fuction():
        print('start of code')
        new_func()
        print('end of code')
    return wrap_fuction



@new_decorator
def rock():
    print('This is new program')

rock()
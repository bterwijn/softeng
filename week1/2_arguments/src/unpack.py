    
def my_function(arg1, arg2, arg3, arg4):
    print('arguments:', arg1, arg2, arg3, arg4)

my_args = (1, 2)
my_kwargs = {'three': 3, 'four': 4}
my_function(*my_args, *my_kwargs.items())

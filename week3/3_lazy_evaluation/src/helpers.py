def pr(tag, v):
    """ Print 'tag' and 'v' and return 'v' """
    print(tag, v)
    return v

if __name__ == '__main__':
    a = pr('test:', 123)  # prints 'test: 123' and also returns 123
    print('a:', a)
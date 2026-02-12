import products
import memory_graph as mg
import copy

functions1 = [products.assignment1, products.assignment2,
              products.assignment3, products.assignment4]

def x192(functions):
    goods = products.create_products()
    for fun in functions: fun(goods);
    return str(goods)

def x827(goods):
    p = goods.get('cake'); p.ingredients[1][1] = 0.4

def x891(goods):
    p = goods.get('cake_plus'); p.ingredients = copy.deepcopy(p.ingredients); p.ingredients[1][1] = 0.5

def x432(goods):
    p = copy.copy(goods.get('cake')); p.name = 'cake_plus'; p.added_value = 2.2; goods.add(p)

def x627(goods):
    goods.add( products.Product('cinnamon',  calories=20, added_value=0.9) )
    p = copy.copy(goods.get('cake')); p.ingredients = copy.copy(p.ingredients)
    p.name = 'cake_cinnamon' ;p.add_ingredient('cinnamon', 0.2); goods.add(p)
    
functions2 = [x432,
              x627,
              x827,
              x891]

def do_test(n):
    assert x192(functions1[:n]) == x192(functions2[:n])

def test_assignment1():
    do_test(1)
    
def test_assignment2():
    do_test(2)

def test_assignment3():
    do_test(3)

def test_assignment4():
    do_test(4)

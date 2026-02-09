import copy

def assignment1(products):
    """
    Add new product 'cake_plus' to products by copying it from product 'cake' and
    setting 'added_value=2.2' to it.
    """
    cake_plus = copy.copy(products.get('cake'))
    cake_plus.name = 'cake_plus'
    cake_plus.added_value = 2.2
    products.add(cake_plus)

def assignment2(products):
    """
    First add new product 'cinnamon' to products with calories=20, added_value=0.9
    and no ingredients.
    Then add product 'cake_cinnamon' to products by copying it from product 'cake'
    and adding 0.2 of ingredient 'cinnamon' to it.
    """
    # products.add( Product('cinnamon', calories=20, added_value=0.9) )

def assignment3(products):
    """ Reduce the sugar in all cakes to '0.4'. """

def assignment4(products):
    """ Restore the sugar to 0.5 for only 'cake_plus'. """

# ------- do not edit below this line -------

def main():
    products = create_products()

    assignment1(products)
    assignment2(products)
    assignment3(products)
    assignment4(products)

    print(products)

    
def create_products():
    products = Products()
    products.add( Product('egg',    calories=80, added_value=0.3) )
    products.add( Product('flour',  calories=50, added_value=0.9) )

    dough = Product('dough', added_value=1.0)
    dough.add_ingredient('egg', 2)
    dough.add_ingredient('flour', 0.6)
    products.add(dough)

    products.add( Product('sugar',  calories=90, added_value=1.5) )

    cake = Product('cake', added_value=2.0)
    cake.add_ingredient('dough', 2)
    cake.add_ingredient('sugar', 0.05)
    products.add(cake)

    return products


class Product:

    def __init__(self, name, calories=0, added_value=0):
        self.name = name
        self.added_value = added_value
        self.calories = calories

    def add_ingredient(self, name, amount):
        if not hasattr(self, 'ingredients'):
            self.ingredients = []
        self.ingredients.append( [name, amount] )

    def get_ingredients(self):
        if not hasattr(self, 'ingredients'):
            return []
        return self.ingredients

    
class Products:

    def __init__(self):
        self.products: dict[str, Product] = {}  

    def __repr__(self):
        s = ''
        for name in self.products.keys():
            s += f'{name:20} price: {round(self.get_price(name), 2):7} calories: {self.get_calories(name):7}\n'
        return s
        
    def add(self, product):
        self.products[product.name] = product

    def get(self, name):
        return self.products[name]

    def get_calories(self, name):
        """ Computes calories by adding all calories of product and ingredients. """
        product = self.get(name)
        calories = product.calories
        for name, amount in product.get_ingredients():
            calories += self.get_calories(name) * amount
        return calories

    def get_price(self, name):
        """ Computes price by adding all added_value of product and ingredients. """
        product = self.get(name)
        calories = product.added_value
        for name, amount in product.get_ingredients():
            calories += self.get_price(name) * amount
        return calories


if __name__ == '__main__':
    main()

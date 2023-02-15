def get_discount(customer):

    discounts = {'gold': .3,
                 'silver': .2,
                 'bronze': .1}

    discount = discounts.get(customer.loyalty, None)

    if not discount:
        raise ValueError('Could not determine customer discount')

    return discount

class Customer:
    loyalty_levels = {'gold', 'silver', 'bronze'}

    def __init__(self, loyalty, membership = 0):
        self.loyalty = loyalty
        self.membership = membership

    def get_membership(self):
        return self._membership

    def set_membership(self, value):
        if value<0 or value >54:
            raise ValueError('Invalid membership year')

        self._membership= value
    def get_loyalty(self):
        return self._loyalty

    def set_loyalty(self, level):
         if level not in self.loyalty_levels:
             raise ValueError(f"invalid loyalty level of {level}")

         self._loyalty = level

    loyalty = property(fget=get_loyalty, fset=set_loyalty)
    membership = property(fget = get_membership, fset=set_membership)

c = Customer('bronze', 2)
c2 = Customer('gold',3)
print(c2.loyalty)
print(c.__dict__ )
# c3 = Customer('platinum',89)
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)
{'banana', 'orange', 'apple', 'pear'}
>>> 'orange' in basket
True
>>> 'crabgrass' in basket
False
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a
{'c', 'b', 'r', 'a', 'd'}
>>> a - b
{'d', 'b', 'r'}
>>> a | b
{'c', 'm', 'b', 'r', 'z', 'a', 'l', 'd'}
>>> a & b
{'a', 'c'}
>>> a ^ b
{'z', 'm', 'b', 'r', 'l', 'd'}

#cart/context_processors.py
#Context processors can reside anywhere in your code

#a context processor is a function that receives the request object as parameter, and returns
#a dictionary of objects that will be available to all the templates rendered using RequestContext

from .cart import Cart

def cart(request):
    '''instantiate the cart using the request object and make it available for the templates as a variable named cart'''
    return {'cart':Cart(request)}
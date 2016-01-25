#cart/cart.py

from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    '''Cart class manage the shopping cart'''
    def __init__(self,request):
        """initialize the cart"""
        self.session=request.session #store the current session to make it accessible to the other methods of the Cart class
        
        #return the cart dictionary or None
        cart=self.session.get(settings.CART_SESSION_ID) #get the cart value from current session dictionary
        if not cart:
           cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart #A dictionary with product_id as key
        
    def add(self,product,quantity=1, update_quantity=False):
        '''Add a product to the cart or update its quantity.'''
        #convert the product id into string because django uses json to serialize session data
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':str(product.price)}
            
        if update_quantity:
            self.cart[product_id]['quantity']=quantity #update the quantity of the product
        else:
            self.cart[product_id]['quantity']+=quantity #add the current quantity
        self.save()
            
    def save(self):
        #update the session cart
        self.session[settings.CART_SESSION_ID]=self.cart
        #mark the session as "modeified" to make sure it is saved
        self.session.modified=True
        
    def remove(self,product):
        '''remove a product from the cart.'''
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]#remove the specific product
            self.save()#update the cart in the session
            
    def __iter__(self):
        '''iterate over the items in the cart and get the products from the database'''
        product_ids=self.cart.keys()
        #get the product objects and add them to the cart
        products=Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product']=product
            
        for item in self.cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price']*item['quantity']
            yield item
            
    def __len__(self):
        '''count all items in the cart'''
        return sum(item['quantity'] for item in self.cart.values())
        
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
            
            
    def clear(self):
        '''remove cart from session'''
        del self.session[settings.CART_SESSION_ID]
        self.session.modified=True
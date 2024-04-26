from product.models import car_model, Accessary

class Cart():
    
    def __init__(self, request):
        self.session = request.session
        
        car_cart = self.session.get('car_session_key')
        accesary_cart = self.session.get('accesary_session_key')

        if 'car_session_key' not in request.session:
            self.session['car_session_key'] = {}
            car_cart = self.session['car_session_key']
            
        if 'accesary_session_key' not in request.session:
            self.session['accesary_session_key'] = {}
            accesary_cart = self.session['accesary_session_key']
            
        self.car_cart = car_cart
        self.accesary_cart = accesary_cart
        
    def car_add(self, product):
        product_id = str(product.id)
        
        if product_id in self.car_cart:
            pass
        else:
            self.car_cart[product_id] = {'name': str(product.car_name), 'price': str(product.car_price), 'quantity': str(product.car_quantity)}
            
        self.session.modified = True
        
    def accesary_add(self, accesary_product):
        accesary_product_id = str(accesary_product.id)
        
        if accesary_product_id in self.accesary_cart:
            pass
        else:
            self.accesary_cart[accesary_product_id] = {'name': str(accesary_product.accessary_name), 'price': str(accesary_product.accessary_price), 'quantity': str(accesary_product.accessary_quantity)}
            
        self.session.modified = True
        
    def __car__len__(self):
        return len(self.car_cart)
    
    def __accesary_len__(self):
        return len(self.accesary_cart)
    
    def get_car_prods(self):
        car_product_ids = self.car_cart.keys()
        car_products = car_model.objects.filter(id__in=car_product_ids)
        return car_products
    
    def get_accesary_prods(self):
        accesary_product_ids = self.accesary_cart.keys()
        accesary_products = Accessary.objects.filter(id__in=accesary_product_ids)
        return accesary_products
        
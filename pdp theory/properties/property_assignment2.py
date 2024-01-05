class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price>0:
            self._price=new_price
            return new_price
        else:
            print("invalid input")

    #price=property(get_price,set_price)       

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, new_size):
        if new_size>0:
            self._size=new_size
            return new_size
        else:
            print("invalid input")

    #size=property(get_size,set_size)
            
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand,str):
            self._brand=new_brand
            return new_brand
        else:
            print("invalid input")

    #brand=property(get_brand,set_brand)


bounce_ball=BouncyBall(100,10,"A")

print(bounce_ball.price)
print(bounce_ball.size)
print(bounce_ball.brand)

bounce_ball.price=200
bounce_ball.size=20
bounce_ball.brand="B"

print(bounce_ball.price)
print(bounce_ball.size)
print(bounce_ball.brand)

    

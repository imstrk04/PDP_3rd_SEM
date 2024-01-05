
from inventory_management_system.products.base_product import Product
from inventory_management_system.products.electronics import Electronics
from inventory_management_system.products.clothing import Clothing
from inventory_management_system.products.diwali import Diwali
from inventory_management_system.serialization.data_operations import serialize_data, deserialize_data
from string_operations.operations import perform_string_operations



if __name__ == '__main__':
    print("Product Class")
    p = Product("Household", 2500, "Electronics")
    print(p.display_info() + "\n")

    print("Electronics Class")
    e = Electronics("JBL", 1000,"Electronics")
    print(e.display_info() + '\n')

    print("Clothing Class")
    c = Clothing("Jeans", 1500, "Clothing")
    print(c.display_info() + "\n")

    print("Diamond Problem")
    d = Diwali("Alexa", 1200,"Electronics")
    print(d.display_info())
    print("MRO of Diwali class", end = " ")
    print(Diwali.__mro__)

    print("Searialisation:")
    data = []
    p1 = {'name' : "Speakers", 'price' : 2000, "category" : "Electronics"}
    p2 = {'name' : "Keyboard", 'price' : 1500, "category" : "Electronics"}
    p3 = {'name' : "T-Shirt", 'price' : 600,"category" : "Clothing"}
    p4 = {'name' : "Track Pants", 'price' : 600, "category" : "Clothing"}
    p5 = {'name' : "Mouse", 'price' : 700, "category" : "Electronics"}

    data.append(p1)
    data.append(p2)
    data.append(p3)
    data.append(p4)
    data.append(p5)

    serialize_data(data)
    
    deserialize_data()

    perform_string_operations(data)
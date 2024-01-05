import re
from productclass import product
from electronicproduct import electronic_product
from clothingproduct import clothing_product
from combinedproduct import combined_product
from serialisation import save_data,load_data

#object creation
c1=combined_product(name='smartshirt',brand='techbrand',size='medium',qty=1)
c2=combined_product(name='smartshoes',brand='techbrand',size='7',qty=1)
product_list=[c1,c2]


#pickle
save_data(product_list,'product.txt')
loaded_contents=load_data('product.txt')

#displaying the data
for objects in loaded_contents:
    print(objects.display())


#regular_expressions
for item in loaded_contents:
    pattern= re.compile(r'^(Small|Medium|Large|XL)$', re.IGNORECASE)
    if re.search(pattern,item.size):
        print('valid product size')
    else:
        print('invalid product size')

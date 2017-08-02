import matematica

print(matematica.area_quad(5))
print(matematica.area_ret(5,10))
print(matematica.peri_quad(10))

#import universao, nao é bom, é perigoso
#from matematica import *

#o mais correto
from matematica import area_quad
print(area_quad(2))
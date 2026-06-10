# import recipes.flavour # type: ignore

# print(recipes.flavour.elaichi_chai());

# from recipes.flavour import elaichi_chai, ginger_chai # type: ignore
# from recepies.flavour import elaichi_chai, ginger_chai

# print(elaichi_chai())
# print(ginger_chai())

# relative import
from .recepies.flavour import elaichi_chai, ginger_chai # type: ignore

print(elaichi_chai())
print(ginger_chai())

from Imports.utils.discount import *
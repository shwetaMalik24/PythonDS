is_boiling = True
stir_count = 5
print(f"initial value of is_boiling: {is_boiling}")
# true = 1 and false = 0
upcasting = is_boiling + stir_count
print(f"upcasting of is_boiling and stir_count: {upcasting}")
# 0 and none as false and rest everthing as true - 11, shweta
is_milk_there = None
print(f"is milk there:{bool(is_milk_there)}")
water_hot = True
tea_added = True
can_serve = water_hot and tea_added
print(can_serve)
tea = False
coffee = True
drink_available = tea or coffee
print(drink_available)
is_logged_in = False
print(not is_logged_in)

chae_type = "Ginger chai"
customer_name = "Shweta"
#  f formatted string
print(f"Customer {customer_name} ordered {chae_type}")
# 0:7 last c is not included it has to be 0:8
chai_description = "aromatic and bold"
print(f"{chai_description[0:8]}")
# [0:8:2] - every second character from 0 to 7
print(f"every second character [0:8:2]:{chai_description[0:8:2]}")
# [12:] from 12th char till the end of the string
print(f"last word :{chai_description[12:]}")
# reverse a string
print(chai_description[::-1])

# Enoding
label_text = "Chai É Special"

decoded_label = label_text.encode("utf-8")

print(f"label_text: {decoded_label}")
raw_spice_data = bytearray(b"cinnamon")
# Modify the bytearray as repace will always return a new bytearray
raw_spice_data = raw_spice_data.replace(
    b"cinnamon",
    b"cardamom"
) 
print(raw_spice_data.decode("utf-8"))
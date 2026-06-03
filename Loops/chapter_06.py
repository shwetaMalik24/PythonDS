# In this example, we are simulating the process of boiling tea. 
# We start with an initial temperature of 40 degrees and use a while loop to keep increasing the temperature by 15 degrees until it reaches or exceeds 100 degrees. 
# Inside the loop, we print the current temperature at each step. 
# Once the loop is finished, we print a message indicating that the tea is ready to boil.
temperature = 40

while temperature < 100:
    temperature += 15
    print(f"Current temperature: {temperature}")

print("Tea is ready to boil")

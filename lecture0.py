# Ask user for name
name = input("What's your name? ").strip().title()

# # Remove whitespace from str
# name = name.strip()
#
# #Capitalize user's name
# # name = name.capitalize()
# name = name.title()


# name = name.strip().title()

print("Hello,", name)
print("Hello," + name)
print("Hello, ", end="")
print(name)
print("Hello,", name, sep="")

print(f"hello, {name}")

"""
- string
    -  .strip()
    - .capitle
 
"""
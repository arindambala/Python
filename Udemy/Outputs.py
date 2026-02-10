# Day 10 - 100 Days of Code

def format_name(first_name, last_name): # title()
    """A function that takes the first & last name, inputted by a user and returns the appropriate formatted name""" # Docstring
    if first_name == "" or last_name == "":
        return
    
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"\nResult : {formatted_first_name} {formatted_last_name}" # EOF
    # print("This isn't returned!") # Won't be executed

formatted_name = format_name(input("\nThe first name : "), input("\nThe last name : ")) # format_name("ight", "BET")
print(formatted_name)

def add(n1, n2):
    return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# def mul(n1, n2):
#     return n1 * n2

# def div(n1, n2):
#     return n1 / n2

my_favourite_op = add
print(my_favourite_op(2, 3))
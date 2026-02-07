# Day 10 - 100 Days of Code

# Calculator
print(f"\n---- Welcome to the Calculator Application! ----")

def format_name(first_name, last_name): # title()
    if first_name == "" or last_name == "":
        return
    
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"\nResult : {formatted_first_name} {formatted_last_name}" # EOF
    # print("This isn't returned!") # Won't be executed

formatted_name = format_name(input("\nThe first name : "), input("\nThe last name : ")) # format_name("ight", "BET")
print(formatted_name)
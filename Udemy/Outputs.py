# Day 10 - 100 Days of Code

# Calculator
print(f"\n---- Welcome to the Calculator Application! ----")

def format_name(first_name, last_name): # title()
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    
    return f"{formatted_first_name} {formatted_last_name}"

formatted_name = format_name("ight", "BET")
print(formatted_name)
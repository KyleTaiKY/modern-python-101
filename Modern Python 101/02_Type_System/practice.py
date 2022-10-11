"""
Pizza shop
"""

# Variable Declaration

customer: str = "Cece"
pizza_base: str = "Thin"
pizza_size: int = 12
topping: str = "Olives"
extra_cheese: bool = True
price: float = 8.99

# Alternative 1 - using print function

print(f"Received order from: {customer}")
print(f"Pizza base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}")

# Alternative 2 - using formatted string
order_details: str = f"""
Received order from {customer}
Pizza base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}
"""

print(order_details)
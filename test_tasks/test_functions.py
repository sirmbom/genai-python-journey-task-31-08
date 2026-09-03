"""Script-style small functions exercises.

Seven holes: six single-line TODOs and one final small block to print results.
Students may implement multiple small functions here.
"""

# 1) Apply a simple percentage discount to a price
def apply_discount(price: float, discount_percent: float) -> float:
    # TODO: fill this line
    discounted = price - (price * discount_percent / 100)  # TODO: replace None with calculation
    return discounted


# 2) Return a greeting using a template
def greet_user(name: str, template: str = "Hello, {name}!") -> str:
    # TODO: fill this line
    greeting = template.format(name=name)  # TODO: replace None with template.format(name=name)
    return greeting


# 3) Compute simple stats: count, total, average
def compute_stats(numbers: list) -> tuple:
    # TODO: fill this line (count)
    count = len(numbers)
    # TODO: fill this line (total)
    total = sum(numbers)
    # TODO: fill this line (average)
    average = total / count if count > 0 else 0
    return count, total, average


# 4) Small helper: safe division
def safe_div(a, b):
    # TODO: single-line placeholder
    result = a/b 
    if(b !=0):
        result = a/b
    else:
        0
      # TODO: replace None with a/b when b != 0 else 0
    return result


# Final block (1-3 lines): call the functions with sample data and print results.
# TODO: complete the block below
stats = compute_stats([10, 20, 30])  # TODO: set to compute_stats([10, 20, 30])
print("discounted:", apply_discount(200, 15))
print("greeting:", greet_user("Sam", "Hi {name}!"))
print("stats:", stats)

# Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

# First things first, define a weight variable and set it equal to any number.
weight = 41.5

# Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.
# Write a comment that says “Ground Shipping”.
# Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.

# Ground Shipping
# 2 lb or less
if weight <= 2:
    ground_shipping_cost = weight * 1.50 + 20.00
    print("Ground Shipping Price: ", "$", ground_shipping_cost)
# Over 2 lb but less than or equal to 6 lb
elif weight > 2 and weight <= 6:
    ground_shipping_cost = weight * 3.00 + 20.00
    print("Ground Shipping Price: ", "$", ground_shipping_cost)
# Over 6 lb but less than or equal to 10 lb
elif weight > 6 and weight <= 10:
    ground_shipping_cost = weight * 4.00 + 20.00
    print("Ground Shipping Price: ", "$", ground_shipping_cost)
# Over 10 lb
else:
    ground_shipping_cost = weight * 10.00 + 20.00
    print("Ground Shipping Price: ", "$", ground_shipping_cost)

# Ground Shipping Premium:

# We’ll also need to make sure we include the price of premium ground shipping in our code.
# Create a variable for the cost of premium ground shipping.
# Note: This does not need to be an if statement because the price of premium ground shipping does not change with the weight of the package.
premium_price = 125.00
# Print it out for the user just in case they forgot!
print("Premium ground shipping price is: $", premium_price)

# Drone Shipping:

# 2 lb or less
if weight <= 2:
    drone_shipping_cost = weight * 4.50
    print("Drone Shipping Price: ", "$", drone_shipping_cost)
# Over 2 lb but less than or equal to 6 lb
elif weight > 2 and weight <= 6:
    drone_shipping_cost = weight * 9.00
    print("Drone Shipping Price: ", "$", drone_shipping_cost)
# Over 6 lb but less than or equal to 10 lb
elif weight > 6 and weight <= 10:
    drone_shipping_cost = weight * 12.00
    print("Drone Shipping Price: ", "$", drone_shipping_cost)
# Over 10 lb
else:
    drone_shipping_cost = weight * 14.25
    print("Drone Shipping Price: ", "$", drone_shipping_cost)
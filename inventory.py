# Create a script inventory.py. The inventory should be a list of dictionaries. 
# Each dictionary represents a product with keys 'product_id', 'name', 'price', and 'stock'.

#  Creating a list of dictionaries (inventory)
# Populate the inventory with at least 4 products.
inventory = [
    {"product_id": 1, "name": "Laptop", "price": 800, "stock": 5},
    {"product_id": 2, "name": "Mouse", "price": 20, "stock": 50},
    {"product_id": 3, "name": "Keyboard", "price": 40, "stock": 30},
    {"product_id": 4, "name": "Monitor", "price": 150, "stock": 10}
]

#  Function that calculates the total value of all items in stock (price * stock for each item, summed up).
def total_inventory_value():
    total = 0
    for item in inventory:
        total += item["price"] * item["stock"]
    return total

# function that finds and returns the product with the highest price.
def highest_priced_product():
    highest = inventory[0]
    for item in inventory:
        if item["price"] > highest["price"]:
            highest = item
    return highest

# Printing the results in a well-formatted way.
print("Inventory Summary \n")

print("All Products:")
for item in inventory:
    print(f"ID: {item['product_id']}, Name: {item['name']}, Price: ${item['price']}, Stock: {item['stock']}")

print("\nTotal value of all items in stock: $", total_inventory_value())

expensive_item = highest_priced_product()
print(f"\nMost expensive product: {expensive_item['name']} (${expensive_item['price']})")

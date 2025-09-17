# Shopping cart using multiple data structures

cart_items = []
item_quantities = {} # Dictionaries for item_id
user_preferences = set() # set for unique product catagories


# Add item to cart
def add_to_cart(item_id, name, price, catagory, quantity=1):
	item = {'id': item_id, 'name': name, 'price': price, 'catagory': catagory}
	cart_items.append(item)
	item_quantities[item_id] = item_quantities.get(item_id, 0) + quantity
	user_preferences.add(catagory)

#example usage

add_to_cart(101,'laptop',9999.9,'electronics')
add_to_cart(102,'book',100.2,'education')

#output

print(f'Cart: {cart_items}')
print(f'Quantities: {item_quantities}')
print(f'User likes: {user_preferences}')
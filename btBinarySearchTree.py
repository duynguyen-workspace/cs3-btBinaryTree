import json

'''
    Define a Phone class
    @param price: type int, product's price
    @param name: type str, product's name
'''
class Phone:
    def __init__(self, price, name):
        self.price = price
        self.name = name

'''
    Define a Node class
    @param value: an object (with 2 attributes: price and name)
'''
class Node:
    def __init__(self, value: Phone):
        self.key = value
        self.left = None
        self.right = None

# Insert function to BST
def insert(root, value):
    if root == None:
        return Node(value)
    
    if value.price < root.key.price:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root

# Search function in BST
def search(root, value):
    if root == None:
        return "404 not found phone with price \"{}\"!".format(value)
    
    if root.key.price == value:
        return root.key.__dict__
    
    if value < root.key.price:
        return search(root.left, value)
    else:
        return search(root.right, value)

# Inorder traversal for BST
def inorder_traverse(root, inorder_result):
    if root != None:
        # Traverse to left node
        inorder_traverse(root.left, inorder_result)

        # Add node to result list
        inorder_result.append(root.key.__dict__)

        # Traverse to the right node
        inorder_traverse(root.right, inorder_result)

    return inorder_result

# BST toString() method
def tree_to_json(root):
    if root == None:
        return None
    
    key_str = json.dumps(root.key.__dict__)
    return {
        'key': key_str,
        'left': tree_to_json(root.left),
        'right': tree_to_json(root.right)
    }

# -----MAIN PROGRAM-----
phones = [
    {"price": 3000, "name": "iphone 12"},
    {"price": 4000, "name": "iphone 13"}, 
    {"price": 5000, "name": "iphone 14"}, 
    {"price": 1000, "name": "iphone 11"}, 
    {"price": 2000, "name": "iphone 12"},
    {"price": 1500, "name": "iphone 15"},
    {"price": 800, "name": "iphone 8"},
    {"price": 2100, "name": "iphone X"},
]

#* Define binary search tree and insert phone objects to BST
root = None
for p in phones:
    phone = Phone(p["price"], p["name"])
    root = insert(root, phone)

#* Display BST in console
# tree_json = tree_to_json(root)
# print(json.dumps(tree_json, indent=4))
    
#* Find the searching value
# print(search(root, 1000))
# print(search(root, 2000))
# print(search(root, 500))

#* Inorder traversal
result = []
print(inorder_traverse(root, result))
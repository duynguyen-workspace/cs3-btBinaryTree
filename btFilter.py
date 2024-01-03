arr_phones = [
    {"price": 3000, "name": "iphone 12"},
    {"price": 4000, "name": "iphone 13"}, 
    {"price": 5000, "name": "iphone 14"}, 
    {"price": 1000, "name": "iphone 11"}, 
    {"price": 2000, "name": "iphone 12"}
]

arr_result = []

for phone in arr_phones:
    if phone["price"] >= 3000 and phone["price"] <= 5000:
        arr_result.append(phone)
        
print(arr_result)
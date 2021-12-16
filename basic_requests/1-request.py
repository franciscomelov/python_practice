import json
import  requests
from requests.models import Response


BASE_URL = 'https://fakestoreapi.com'

# response = requests.get(f"{BASE_URL}/products")
# print(response.json())
# print(response.status_code)

# ---------------------------

# query_params = {
#     "limit": 1
# }
# response = requests.get(f"{BASE_URL}/products", params=query_params)
# print(response.json())

# ------------------

# # response = requests.get(f"{BASE_URL}/products/18")
# # print(response.json())

# # _______________

# new_product = {
#     "title": 'test product',
#     "price": 13.5,
#     "description": 'lorem ipsum set',
#     "image": 'https://i.pravatar.cc',
#     "category": 'electronic'
# }
# response = requests.post(f"{BASE_URL}/products", json=new_product)

# updated_product = {
#     "title": 'updated_product',
#     "category": 'test'
# }

# response = requests.put(f"{BASE_URL}/products/21", json=updated_product)

# updated_product = {
#     "category": 'electronic'
# }

# response = requests.patch(f"{BASE_URL}/products/21", json=updated_product)


response = requests.delete(f"{BASE_URL}/products/21")
print(response.json())


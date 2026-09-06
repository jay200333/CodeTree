product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
first_product = ("codetree", 50)
second_product = (product_name, product_code)

print(f"product {first_product[1]} is {first_product[0]}")
print(f"product {second_product[1]} is {second_product[0]}")
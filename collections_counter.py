# 1st line - X = no. of shoes
# 2nd line = the space separated list of all the shoe sizes in the shop
# 3rd line - the number of customers
# The next N lines contain the space separated values of the shoe size desired by the customer and x_i, the price of the shoe.

from collections import Counter

shoe_count = int(input())
available_shoes = Counter(map(int, input().split()))
customer_count = int(input())

earning = 0

for i in range(customer_count):
    size, price = map(int, input().split())
    if available_shoes[size]:
        earning += price
        available_shoes[size] -= 1

print(earning)

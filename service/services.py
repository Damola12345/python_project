# python program
# Build a simple service rendering app

# Build a simple
import sys
from db import indexer

print('welcome to services rendering')
request = input('what services do you need: ')
services = ['electrician', 'cleaner', 'carpenter', 'driver', 'chef', 'plumber']

if request.lower() not in services:
    sys.exit(1)

print(f'We have {request} available with different price range !!')
print(f'Here are the list of {request} available and price list')

service = indexer[request.lower()]
# todo: find a better way to store this
users = service.keys()

# Print all users
i = 1
for k, v in service.items():
    print(i, ". ",  k, v)
    i += 1

selected = 0
try:
    selected = int(input("Enter number "))

    if selected <= 0 or selected > len(users):
        print("Selected number not found")
        sys.exit(1)
except ValueError:
    print("Please input a number")
    sys.exit(1)

# take value from from keys
print(f"You selected {list(users)[selected - 1]}")
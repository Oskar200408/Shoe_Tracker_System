import json
import os

def add_shoe():
    brand = input("Enter the brand of the shoe: ")
    model = input("Enter the model of the shoe: ")
    buy_price = float(input("Enter the buy price of the shoe: "))
    listed_price = float(input("Enter the listed price of the shoe: "))
    condition = input("Enter the condition of the shoe: ")
    size = int(input("Enter the size of the shoe: "))
    platform = input("Enter the platform the shoes listed on: ")

    shoes = {
        "Brand": brand,
        "Model": model,
        "Buy Price": buy_price,
        "Listed Price": listed_price,
        "Condition": condition,
        "Size": size,
        "Platform": platform
    }
    return shoes


def view_inventory():
    if not active_inventory:
        print("No shoes in the active inventory.")
        return
    
    display_shoes()

def save_active_inventory(active_inventory):
    with open("active_inventory.json", "w") as file:
        json.dump(active_inventory, file, indent = 2)

def save_sold_inventory(sold_inventory):
    with open("sold_inventory.json", "w") as file:
        json.dump(sold_inventory, file, indent = 2)

def load_active_inventory():
    if os.path.exists ("active_inventory.json"):
        with open ("active_inventory.json", "r") as file:
            return json.load(file)
    else:
        return []

def load_sold_inventory():
    if os.path.exists ("sold_inventory.json"):
        with open("sold_inventory.json", "r") as file:
            return json.load(file)
    else:
        return []



def mark_as_sold():
    if not active_inventory:
        print("No shoes to mark as sold")
        return
    display_shoes()
    shoe_sold = int(input("Please choose the corresponding number to the shoe that was sold: "))
    shoe_sold = shoe_sold - 1

    sold_price = float(input("Enter the price you sold the shoe for: "))
    profit = sold_price - shoe["Buy Price"]

    shoe = active_inventory.pop(shoe_sold)
    shoe["Sold for"] = sold_price
    shoe["Profit"] = profit

    sold_inventory.append(shoe)
    save_active_inventory(active_inventory)
    save_sold_inventory(sold_inventory)
    print(f"Marked {shoe["Brand"]} {shoe["Model"]} as sold for £{sold_price}. Profit on shoe: £{profit}")
    print("-" * 100)

def view_sold_inventory():
    if not sold_inventory:
        print("No shoes sold")
        return
    
    for i, shoe in enumerate(sold_inventory, 1):
        print(f"{i}. {shoe["Brand"]} {shoe["Model"]} - Listed for £{shoe["Listed Price"]} - Listed on: {shoe["Platform"]} - Condition: {shoe["Condition"]} - Size: ({shoe["Size"]}) - Bought at: £{shoe["Buy Price"]} - Sold at £{shoe["Sold for"]} - Total profit of £{shoe["Profit"]}")
        print("-" * 100)

def load_inventories():
    active_inventory = load_active_inventory()
    sold_inventory = load_sold_inventory()


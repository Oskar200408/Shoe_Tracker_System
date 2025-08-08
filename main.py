import json
import os
from inventory import add_shoe, view_inventory, save_active_inventory, save_sold_inventory, load_active_inventory, load_sold_inventory, mark_as_sold, view_sold_inventory, load_inventories
from utilities import display_shoes
from report import view_summary_report



def main():
    while True:
        load_inventories()
        print("1. Add Shoe\n2. View Active Inventory\n3. Mark a Shoe as Sold\n4. View Sold Inventory\n5. View Summary Report\n6. Exit")
        try:
            decision = int(input("Enter the number corresponding to your desired action: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if decision == 1:
            shoe_to_add = add_shoe()
            active_inventory = load_active_inventory()
            active_inventory.append(shoe_to_add)
            save_active_inventory(active_inventory)
        elif decision == 2:
            view_inventory()
        elif decision == 3:
            mark_as_sold()
        elif decision == 4:
            view_sold_inventory()
        elif decision == 5:
            view_summary_report()
        elif decision == 6:
            print("Goodbye")
            save_active_inventory(active_inventory)
            save_sold_inventory(sold_inventory)
            break
        else:
            print("Invalid Choice")


            

if __name__ == "__main__":
    main()

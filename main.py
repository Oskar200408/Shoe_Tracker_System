

def add_shoe():
    #brand = input("Enter the brand of the shoe: ")
    brand = "Nike"
    #model = input("Enter the model of the shoe: ")
    model = "Airmax"
    #buy_price = float(input("Enter the buy price of the shoe: "))
    buy_price = 20
    #listed_price = float(input("Enter the listed price of the shoe: "))
    listed_price = 50
    #condition = input("Enter the condition of the shoe: ")
    condition = "New"
    #size = int(input("Enter the size of the shoe: "))
    size = 9
    #platform = input("Enter the platform the shoes listed on: ")
    platform = "Vinted"

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

    

active_inventory = []
add_shoe()
shoe_to_add = add_shoe()
active_inventory.append(shoe_to_add)
print(active_inventory)




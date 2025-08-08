def display_shoes():
    for i, shoe in enumerate(active_inventory, 1):
        print(f"{i}. {shoe["Brand"]} {shoe["Model"]} - Listed for £{shoe["Listed Price"]} - Listed on: {shoe["Platform"]} - Condition: {shoe["Condition"]} - Size: ({shoe["Size"]}) - Bought at: £{shoe["Buy Price"]}")
        print ("-" * 100)
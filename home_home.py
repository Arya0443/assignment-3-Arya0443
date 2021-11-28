class Home:
    __slots__ = ["garden", "indoor", "bathroom", "total_price"]
    def __init__(self, garden, indoor, bathroom, total_price):
        self.garden = garden
        self.indoor = indoor
        self.bathroom = bathroom
        self.total_price = total_price

class Home_Category:
    __slots__ = ["name", "code", "price", "category"]
    def __init__(self, name, code, price, category):
        self.name = name
        self.code = code
        self.price = price
        self.category = category

home = Home([],[],[],50.0)
garden_items = {"p": ("3 Pack garden flower", 5.0), "l": ("Hanging light wire", 10.0), "b": ("Garden bench", 35.0)}
indoor_items = {"t": ("Small table lamp", 5.0), "f1": ("City picture frame", 7.0), "r": ("Entry rug", 35.0), "f2": ("Flower vase", 14.0)}
bathroom_items = {"m": ("Wall mirror", 15.0), "c": ("Shower curtains", 10.0), "w": ("Wall mount", 7.0)}

def garden_options():
    while True:
        choice = input("\nChoose one type of garden idea (O for options, n for next category): ")
        if choice == "0":
            items_chosen = print_garden_options()
            if items_chosen == [""]:
                print("No Items Chosen")
            elif items_chosen == ["0"]:
                print_garden_options()
            else:
                try:
                    for i in items_chosen:
                        code, name, price = i, garden_items[i][0], garden_items[i][1]
                        item = Home_Category(name, code, price, "garden")
                        home.garden.append(item)
                        home.total_price += price
                        print("One",name,"is added to your home for $",price)
                except:
                    print("Invalid Item code.")
        elif choice =="n":
            break
        else:
            print("Enter valid choice.")

def print_garden_options():
    global garden_items
    print("\nGarden Options:")
    for item_code in garden_items:
        item_name, item_price = garden_items[item_code][0], garden_items[item_code][1]
        print(item_name + " (" + item_code + ") : $" + str(item_price))
    print()
    items_chosen = input("Choose your items (O for options): ")
    items_chosen = items_chosen.split()
    return items_chosen

def indoor_options():
    while True:
        choice = input("\nChoose your indoor living space ideas (O for options, n for next category): ")
        if choice == "0":
            items_chosen = print_indoor_options()
            if items_chosen == "":
                print("No Items Chosen")
            elif items_chosen == ["0"]:
                print_indoor_options()
            else:
                try:
                    for i in items_chosen:
                        code, name, price = i, indoor_items[i][0], indoor_items[i][1]
                        item = Home_Category(name, code, price, "indoor")
                        home.indoor.append(item)
                        home.total_price += price
                        print("One",name,"is added to your home for $",price)
                except:
                    print("Invalid Item code.")
        elif choice =="n":
            break
        else:
            print("Enter valid choice.")

def print_indoor_options():
    global indoor_items
    print("\nIndoor Options:")
    for item_code in indoor_items:
        item_name, item_price = indoor_items[item_code][0], indoor_items[item_code][1]
        print(item_name + " (" + item_code + ") : $" + str(item_price))
    print()
    items_chosen = input("Choose your items (O for options): ")
    items_chosen = items_chosen.split()
    return items_chosen

def main():
    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ...")
    garden_options()
    indoor_options()


if __name__ == "__main__":
    main()

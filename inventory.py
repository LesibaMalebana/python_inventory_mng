
class Shoes():  # class and adn constru

    def __init__(self,country,code,product,cost,quantity):
        self.country =country
        self.code =code
        self.product =product
        self.cost = cost
        self.quantity =quantity

    def get_cost(self): # Get information
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country} , {self.code} ,{self.product},{self.cost} ,{self.quantity}"
    def __repr__(self):
        return f"*{self.country}, {self.code}, {self.product}, {self.cost} ,{self.quantity}"


shoes_types =[]

def read_shoes_data():
    with open("inventory.txt", "r+") as read_shoes:
        f = read_shoes.readlines()
        for i in f[1:]: # Indexing everygint after the 2nd index
            shoe_store = i.strip('\n').split(',')

            temp_shoe = Shoes(shoe_store[0], shoe_store[1], shoe_store[2], shoe_store[3], shoe_store[4])
            shoes_types.append(temp_shoe)
    print("Shoes have been loaded ,Procceed with Operation.")
read_shoes_data()
        # print(shoes_types)
# for i in shoes_types:
#     print(i)

def capture_shoes():
    user_country = input("Please enter shoe country")
    user_code = input("What code is this Shoe")
    user_product = input("What is the product ?")
    user_cost = input("How much are they ?")
    user_quantity = input("How many shoes are in stock ?")

    user_shoe = Shoes(user_country,user_code,user_product,user_cost,user_quantity) # Shoes obj

    shoes_types.append(user_shoe)

def view_all():
    for shoe in shoes_types:
        print(f"""
        Country : {shoe.country}
        Code : {shoe.code}
        Product :{shoe.product}
        Cost :{shoe.cost}
        Quantity :{shoe.quantity} 
        """)

# view_all()
# capture_shoes()
# # print(shoes_types)
# for i in shoes_types:
#     print(i)

def re_stock():
    min_value = int(shoes_types[0].quantity) # setting the first item
    shoe_position = 0
    for count,m in enumerate(shoes_types):
        if int(m.quantity) < int(min_value):
            min_value = int(m.quantity)
            shoe_position = count
    print(shoes_types[shoe_position])
    user_request = input("Do you want to Update Show Quantity Y / N ?").lower()
    if user_request == "y":
        user_new_shoe = input("Please enter the new Shoe quantity")
        shoes_types[shoe_position].quantity = user_new_shoe

#re_stock()

def search_shoe():
    user_request = input(" Please enter a shoe Code E.G SKU44386? ")
    for z in shoes_types:
        if z.code == user_request:
            print(f"""
                   Country : {z.country}
                   Code : {z.code}
                   Product :{z.product}
                   Cost :{z.cost}
                   Quantity :{z.quantity} 
                   """)
# search_shoe()

def value_per_item():
    for i in shoes_types:
        value = int(i.cost) * int(i.quantity)
        print(f"""
                Country : {i.country}
                           Code : {i.code}
                           Product :{i.product}
                           Cost :{i.cost}
                           Quantity :{i.quantity} 
                           Value of item R:{value}
                """)
# value_per_item()
def highest_qty():
    max_value = int(shoes_types[0].quantity)  # setting the first item
    shoe_position = 0
    for count, m in enumerate(shoes_types):
        if int(m.quantity) >= int(max_value):
            max_value = int(m.quantity)
            shoe_position = count
    print(shoes_types[shoe_position])
    print(f"The Shoe {shoes_types[shoe_position].product} is for sale..")

# highest_qty()

while True:
    menu = input("\n R - Read Shoes \n CS - Capture Shoes \n VA - View All \n RS - Re-stock \n SS - Search Shoe \n SP - Shoe Price \n HQ - Highest Quantity \n E - Exit").upper()
    if menu =="R":
        read_shoes_data()
    elif menu == "CS":
        capture_shoes()
    elif menu == "VA":
        view_all()
    elif menu == "RS":
        re_stock()
    elif menu == "SS":
        search_shoe()
    elif menu == "SP":
        value_per_item()
    elif menu == "HQ":
        highest_qty()
    elif menu == "E":
        exit()
    else:
        print("You have choosen an incorrect Choice")



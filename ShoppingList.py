from Product import Product

class ShoppingList:
    def __init__(self):
        self.product_list : dict[str,Product] = {}
        self.bought_product_list: dict[str, Product] = {}

    @staticmethod
    def show_actions():
        print("0: exit shopping list app")
        print("1: add product")
        print("2: remove product")
        print("3: edit product")
        print("4: set as bought")
        print("5: show info about product")
        print("6: show info about shopping list")
        print("7: filter by cost")
        print("8: filter by category")
        print("9: filter by status")

    def chose_actions(self,action:str):
        match action:
            case "0":
                print("exit shopping list app")
            case "1":
                name=str(input("input name: "))
                category=str(input("input category: "))
                quantity=int(input("input quantity: "))
                price_for_one=float(input("input price for one: "))
                product = Product(name,category,quantity,price_for_one)
                self.add(product)
            case "2":
                self.list_names_info()
                name=str(input("input name: "))
                self.remove(name)
            case "3":
                self.list_names_info()
                name = str(input("input name: "))
                self.edit(name)
            case "4":
                self.list_names_info()
                name = str(input("input name: "))
                self.set_bought(name)
            case "5":
                self.list_names_info()
                name = str(input("input name: "))
                self.prod_info(name)
            case "6":
                self.list_info()
            case "7":
                cost = int(input("input cost: "))
                self.cost_filter(cost)
            case "8":
                category = str(input("input category: "))
                self.category_filter(category)
            case "9":
                status = str(input("input status"))
                if status == "Bought" or status == "bought":
                    self.status_filter(True)
                elif status == "Not Bought" or status == "not bought":
                    self.status_filter(False)
                else:
                    print("there is no such status")

    def add(self,product_add:Product):
        self.product_list[product_add.name] = product_add

    def remove(self,product_remove_name:str):
        del self.product_list[product_remove_name]

    def edit(self,product_edit_name:str):
        print("fields to edit in " + product_edit_name)

    def set_bought(self,product_set_name:str):
        self.product_list[product_set_name].status = True
        self.bought_product_list[product_set_name] = self.product_list[product_set_name]

    def prod_info(self,product_info_name):
        print("Fields in product " + product_info_name + " contains values")
        print("Category: " + self.product_list[product_info_name].category)
        print("Quantity: " + str(self.product_list[product_info_name].quantity))
        print("Price for one: " + str(self.product_list[product_info_name].price_for_one))
        print("All cost: " + str(self.product_list[product_info_name].all_cost))
        print("Status: " + self.product_list[product_info_name].showStatus() + "\n")

    def list_info(self):
        print("There are " + str(len(self.product_list)) + " products")
        for prod_key in self.product_list:
            print("Fields in product " + self.product_list[prod_key].name + " contains values")
            print("Category: " + self.product_list[prod_key].category)
            print("Quantity: " + str(self.product_list[prod_key].quantity))
            print("All cost: " + str(self.product_list[prod_key].all_cost))
            print("Status: " + self.product_list[prod_key].showStatus() + "\n")

    def list_names_info(self):
        print("There are " + str(len(self.product_list)) + " products")
        for prod_key in self.product_list:
            print("Product name: " + self.product_list[prod_key].name)

    def cost_filter(self,cost:int):
        print("Filtered products: ")
        for prod_key in self.product_list:
            if self.product_list[prod_key].all_cost <= cost:
                print(self.product_list[prod_key].name)

    def category_filter(self,category:str):
        print("Filtered products: ")
        for prod_key in self.product_list:
            if self.product_list[prod_key].category == category:
                print(self.product_list[prod_key].name)

    def status_filter(self,status:bool):
        print("Filtered products: ")
        for prod_key in self.product_list:
            if self.product_list[prod_key].status == status:
                print(self.product_list[prod_key].name)

    def status_sort(self,sort:bool):
        new_prod_list : dict[str,Product] = {}
        for prod_key in self.product_list:
            if (self.product_list[prod_key].status == True)==sort:
                new_prod_list[prod_key] = self.product_list[prod_key]
                print("added")
        for prod_key in self.product_list:
            if (self.product_list[prod_key].status == False)==sort:
                new_prod_list[prod_key] = self.product_list[prod_key]
                print("added")
        for prod_key in new_prod_list:
            print(prod_key)


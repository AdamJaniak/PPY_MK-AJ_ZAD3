class Product():
    def __init__(self,name,category,quantity,price_for_one):
        self.name : str = name
        self.category : str = category
        self.quantity : int = quantity
        self.price_for_one : float = price_for_one
        self.all_cost : float = quantity*price_for_one
        self.status : bool = False

    def showStatus(self):
        if self.status:
            return "Bought"
        else:
            return "Not Bought"

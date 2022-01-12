from item import Item

class Phone(Item):
    all = []

    def __init__(self, name:str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        #Assign to self object
        self.broken_phones = broken_phones
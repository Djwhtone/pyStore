class Store():
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def __str__(self):
        items_string = ", ".join(self.items)
        return f'Store Name: {self.name} \nItems: {items_string}'



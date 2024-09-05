class Inventory:
    def __init__(self):
        # Initialize an empty inventory
        self.items = {}

    def add_item(self, item_name, quantity=1):
        """Add or update an item in the inventory."""
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity=1):
        """Remove an item from the inventory, or decrease its quantity."""
        if item_name in self.items:
            if self.items[item_name] > quantity:
                self.items[item_name] -= quantity
            elif self.items[item_name] == quantity:
                del self.items[item_name]
            else:
                print(f"Not enough {item_name} to remove.")
        else:
            print(f"{item_name} not found in inventory.")

    def get_items(self):
        return self.items
    
    def get_inventory(self):
        return self.items

    def list_items(self):
        """List all items in the inventory."""
        if self.items:
            print("Inventory:")
            for item_name, quantity in self.items.items():
                print(f"{item_name}: {quantity}")
        else:
            print("Inventory is empty.")

    def has_item(self, item_name, quantity=1):
        """Check if the inventory has enough of a specific item."""
        return self.items.get(item_name, 0) >= quantity
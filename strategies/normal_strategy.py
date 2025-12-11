from item import Item

class NormalItemStrategy:
    def __init__(self, item: Item) -> None:
        self.item = item

    def update(self) -> None:
        self.decrease_quality()
        
        self.item.sell_in -= 1
        
        if self.item.sell_in < 0:
            self.decrease_quality()

    def decrease_quality(self) -> None:
        if self.item.quality > 0:
            self.item.quality -= 1
            
    def increase_quality(self) -> None:
        if self.item.quality < 50:
            self.item.quality += 1
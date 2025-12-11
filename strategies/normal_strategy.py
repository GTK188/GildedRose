from item import Item
from strategies.constants import MAX_QUALITY, MIN_QUALITY

class NormalItemStrategy:
    def __init__(self, item: Item) -> None:
        self.item = item

    def update(self) -> None:
        self.decrease_quality(1)
        
        self.item.sell_in -= 1
        
        if self.item.sell_in < 0:
            self.decrease_quality(1)

    def decrease_quality(self, amount: int = 1) -> None:
        self.item.quality = self.item.quality - amount

        if self.item.quality < MIN_QUALITY:
            self.item.quality = MIN_QUALITY
            
    def increase_quality(self, amount: int = 1) -> None:
        self.item.quality = self.item.quality + amount

        if self.item.quality > MAX_QUALITY:
            self.item.quality = MAX_QUALITY
from strategies.normal_strategy import NormalItemStrategy
from strategies.aged_brie_strategy import AgedBrieStrategy
from strategies.backstage_pass_strategy import BackstagePassStrategy
from strategies.sulfuras_strategy import SulfurasStrategy
from strategies.conjured_strategy import ConjuredStrategy
from item import Item

def get_item_strategy(item: Item) -> NormalItemStrategy:
    match item.name:
        case name if name.startswith("Sulfuras"):
            return SulfurasStrategy(item)
        case "Aged Brie":
            return AgedBrieStrategy(item)
        case name if name.startswith("Backstage passes"):
            return BackstagePassStrategy(item)
        case name if name.startswith("Conjured"):
            return ConjuredStrategy(item)
        case _:
            return NormalItemStrategy(item)
# -*- coding: utf-8 -*-
from item_factory import get_item_strategy
from item import Item
from typing import List

class GildedRose(object):

    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            strategy = get_item_strategy(item)
            strategy.update()
from strategies.normal_strategy import NormalItemStrategy

class AgedBrieStrategy(NormalItemStrategy):
    def update(self) -> None:
        self.increase_quality()
        
        self.item.sell_in -= 1
        
        if self.item.sell_in < 0:
            self.increase_quality()
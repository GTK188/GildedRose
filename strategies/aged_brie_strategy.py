from strategies.normal_strategy import NormalItemStrategy

class AgedBrieStrategy(NormalItemStrategy):
    def update(self) -> None:
        self.item.sell_in -= 1

        amount = 2 if self.item.sell_in < 0 else 1
        
        self.increase_quality(amount)
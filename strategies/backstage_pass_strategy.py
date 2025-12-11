from strategies.normal_strategy import NormalItemStrategy

class BackstagePassStrategy(NormalItemStrategy):
    def update(self) -> None:
        self.increase_quality()

        if self.item.sell_in <= 10:
            self.increase_quality()

        if self.item.sell_in <= 5:
            self.increase_quality()

        self.item.sell_in -= 1

        if self.item.sell_in < 0:
            self.item.quality = 0
from strategies.normal_strategy import NormalItemStrategy
from .constants import CONCERT_LONG_COUNTDOWN, CONCERT_SHORT_COUNTDOWN

class BackstagePassStrategy(NormalItemStrategy):
    def update(self) -> None:
        self.item.sell_in -= 1

        if self.item.sell_in < 0:
            self.item.quality = 0
            return

        if self.item.sell_in < CONCERT_SHORT_COUNTDOWN:
            amount = 3
        elif self.item.sell_in < CONCERT_LONG_COUNTDOWN:
            amount = 2
        else:
            amount = 1

        self.increase_quality(amount)
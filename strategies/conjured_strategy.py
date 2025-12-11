from strategies.normal_strategy import NormalItemStrategy
from strategies.constants import MIN_QUALITY

class ConjuredStrategy(NormalItemStrategy):
    def decrease_quality(self, amount: int = 1) -> None:
        super().decrease_quality(amount * 2)
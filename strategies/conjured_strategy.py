from strategies.normal_strategy import NormalItemStrategy

class ConjuredStrategy(NormalItemStrategy):
    def decrease_quality(self, amount: int = 1) -> None:
        super().decrease_quality(amount * 2)
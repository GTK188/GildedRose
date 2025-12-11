from strategies.normal_strategy import NormalItemStrategy

class ConjuredStrategy(NormalItemStrategy):
    def decrease_quality(self) -> None:
        self.item.quality -= 2
        
        if self.item.quality < 0:
            self.item.quality = 0
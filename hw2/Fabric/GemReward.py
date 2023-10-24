import IGameItem


class GemReward(IGameItem):
    def open(self) -> None:
        print("Открыли сундук с изумрудом")

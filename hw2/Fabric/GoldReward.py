import IGameItem


class GoldReward(IGameItem):
    def open(self) -> None:
        print("Открыли сундку с золотом")

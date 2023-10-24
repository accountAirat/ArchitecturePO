import ItemFabric, IGameItem, GoldReward


class GoldGenerator(ItemFabric):
    def create_item(self) -> IGameItem:
        print("Создали сундук(золото)")
        return GoldReward()

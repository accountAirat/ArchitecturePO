import ItemFabric, IGameItem, GemReward


class GemGenerator(ItemFabric):
    def create_item(self) -> IGameItem:
        print("Cоздали сундук(изумруд)")
        return GemReward()

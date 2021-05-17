class Order:

    def __init__(self, orderId: int):
        self.__order_id: int = orderId

    def getId(self) -> int:
        return self.__orderId

    def getCustomerId(self) -> int:
        return self.__customerId

    def setCustomerId(self, customerId:int) -> None:
        self.__customerID: int =customerId
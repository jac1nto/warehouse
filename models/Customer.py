class Customer:
    def __init__(self, customerId : int, name: str, address: str, website: str):
        self.__customerId:int=customerId
        self.__name:str=name
        self.__address:str=address
        self.__website:str=website

    def getCustomerId(self) -> int:
        return self .__customerId

    def getName(self) -> str:
        return self .__name

    def getAddress(self) -> str:
        return self .__address

    def getWebsite(self) -> str:
        return self .__website



    def setCustomerId(self, customerId:int)-> None:
        self.__customerId: int = customerId

  


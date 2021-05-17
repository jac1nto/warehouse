class Contact:

    def __init__(self,  contactId: int):
        self.__contactId: int = contactId

    def getContactId(self) -> int:
        return self.__contactId
    
    def getFirstName(self) -> str:
        return self.__firstName

    def getLastName(self) -> str:
        return self.__lastName

    def getEmail(self) -> str:
        return self.__email

    def getPhone(self) -> str:
        return self.__phone

    def setPhone(self, phone: str) -> None:
        self.__phone: str = phone

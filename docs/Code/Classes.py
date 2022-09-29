
class Error(Exception):
    pass

class GenericError(Error):
    pass

class Interfaccia:
    def __int__(self, nome = "Interfaccia"):
        self.nome = nome
    def send(self, amount:float, conto:Conto):
        print(f"Invio un bonifico di {amount} al conto {conto.IBAN}")

class Cliente:
    def __init__(self, user: str, pw: str, banca: ePortfolio):
        self.banca = banca
        self.user = user
        self.pw = pw

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def pw(self):
        return self.__pw

    @pw.setter
    def pw(self, pw):
        self.__pw = pw

    def visualizzaEstratto(self, banca: ePortfolio, conto: Conto):
        myconto = banca.lista_conti[conto.IBAN]
        if myconto.checkowner(self):
            estratto = myconto.estrattoconto
            print(estratto)

    def trasferimento(self, token: str, banca: ePortfolio, IBAN: str, amount: float):
        if token == "esterno":
            banca.bonificoesterno(amount)
        elif token == "interno":
            banca.giroconto(IBAN, amount)


class Conto:
    def __init__(self, IBAN: str, balance: float, owner: Cliente):
        self.balance = balance
        self.__IBAN = IBAN
        self.__owner = {}
        self.addowner(owner)

    def getowner(self):
        return self.__owner

    def addowner(self, owner):
        self.getowner()[owner.user] = owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def IBAN(self):
        return self.__IBAN

    def checkowner(self, doc: Cliente):
        if self.__owner == doc:
            return True
        else:
            return False

    def estrattoconto(self):
        estratto = "Transazioni Passate"
        estratto += "----------"
        return estratto


class ePortfolio:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_conti = {} #id : obj conto
        self.lista_clienti = {} #user : obj cliente

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def addConto(self, doc: Conto):
        self.lista_conti[doc.IBAN] = doc

    def delConto(self, doc: Conto):
        self.lista_conti.pop(doc.IBAN)

    def addCliente(self, doc: Cliente):
        self.lista_clienti[doc.user] = doc

    def delCliente(self, doc: Cliente):
        self.lista_clienti.pop(doc.user)

    def giroconto(self, IBAN, amount: float):
        if amount < 0.0:
            raise ValueError("L'ammontare da trasferire deve essere positivo")
            pass
        if IBAN in self.lista_conti.keys():
            target = self.lista_conti[IBAN]
            oldbalance = target.balance
            newbalance = oldbalance + amount
            print(f"Trasferico {amount} sul conto...")
            target.balance = newbalance
        else:
            raise GenericError("Il conto non è interno a ePortfolio")
            pass

    def bonificoesterno(self, amount: float):
        if amount < 0.0:
            raise ValueError("L'ammontare da trasferire deve essere positivo")
            pass
        else:
            print(f"Invio un bonifico di {amount} al di fuori del circuito ePortfolio")



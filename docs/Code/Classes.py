
class Error(Exception):
    pass

class GenericError(Error):
    pass

class Interfaccia:
    def __int__(self, nome = "Interfaccia"):
        self.nome = nome
    def send(self, amount:float):
        print(f"Invio un bonifico di {amount} al conto")

class Cliente:
    def __init__(self, user: str, pw: str, banca):
        self.banca = banca
        self.user = user
        self.pw = pw

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        if not isinstance(user, str):
            raise TypeError("deve essere una stringa")
        if len(user) < 2 or len(user) > 20:
            raise GenericError(" la lunghezza dell'username deve essere fra 2 e 20 caratteri")
        self.__user = user

    @property
    def pw(self):
        return self.__pw

    @pw.setter
    def pw(self, pw):
        if not isinstance(pw, str):
            raise TypeError("la passdword deve essere una stringa")
        if not 6 <= len(pw) <=12:
            raise GenericError("La password deve essere compresa fra 6 e 12 caratteri")
        if pw.isdecimal():
            raise ValueError("la password non può contenere solo numeri")
        if pw.isalpha():
            raise ValueError("la password non può contere solo lettere")
        if pw.isalnum():
            raise ValueError("la password deve contenere almeno un carattere speciale")
        if " " in pw:
            raise ValueError("la password non può contenere spazi")
        self.__pw = pw

    def visualizzaEstratto(self, banca, conto):
        myconto = banca.lista_conti[conto.IBAN]
        if myconto.checkowner(self):
            estratto = myconto.estrattoconto
            print(estratto)

    def trasferimento(self, token: str, banca, IBAN: str, amount: float):
        if token == "esterno":
            banca.bonificoesterno(amount)
        elif token == "interno":
            banca.giroconto(IBAN, amount)
        else:
            raise GenericError("Token non riconosciuto")
            pass


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
            print(f"Trasferisco {amount} sul conto...")
            target.balance = newbalance
        else:
            raise GenericError("Il conto non è interno a ePortfolio")
            pass

    def bonificoesterno(self, amount: float, IBAN: str):
        if amount < 0.0:
            raise ValueError("L'ammontare da trasferire deve essere positivo")
            pass
        else:
            print(f"Invio un bonifico di {amount} all IBAN {IBAN} di fuori del circuito ePortfolio")



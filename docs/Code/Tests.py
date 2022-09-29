from Classes import *

if __name__ == "__main__":
    banca = ePortfolio("ePortfolio")

    #test 01
    try:
        oClient = Cliente(123, "Marco123!", banca)
    except TypeError as exception:
        print("Error: " + str(exception))

    #test 02
    try:
        oClient = Cliente("Marco", "Marco", banca)
    except GenericError as exception:
        print("Error: " + str(exception))

    #test 03
    try:
        oClient = Cliente("Marco", "Marcolinopan", banca)
    except (ValueError) as exception:
        print("Error: " + str(exception))
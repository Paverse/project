dictionary = {"ziemniak":"kg",
              "jajka":"szt",
                "mleko":"l",
                "rower":"szt"
              }
lista = [x for x in dictionary if dictionary[x] == "szt"]
print(lista)
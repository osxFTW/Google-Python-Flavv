my_var = input("nr: ")
try:
    my_int = int(my_var)
    print(my_int)
except ValueError:
    print("Ai introdus un string in locul la int")
    my_int = 3
except Exception as e:
    print("Exceptie generala", type(e).__name__)
else:
    print("A functionat!")
finally:
    print("Se executa oricand")

print(my_int)
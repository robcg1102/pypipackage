def divisaCOnverter(money, valueOfTheMoment):
    if(money == 0 or money == 0.0):
        raise Exception("El valor del dinero introducido es inválido")
    else:
        return round(money * valueOfTheMoment)
    

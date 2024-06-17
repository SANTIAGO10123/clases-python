meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "El significado del XD se refiere a una risa descontrolada, concretamente a carcajadas.",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!)")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("ESTA PALABRA NO EXISTE EN LA BASE DE DATOS!!!")

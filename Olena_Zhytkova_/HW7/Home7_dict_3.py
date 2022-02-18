europe_dict={'Germany':['Berlin','Numberg','Stuttgart','Munchen','Frankfurt','Magdeburg','Bonn','Dresden'],\
    'Italy':['Rome','Bologna','Venezia','Verona','Milano','Turin','Naples','Palermo','Genova'],\
    'France':['Paris','Lyon','Marseille','Toulouse','Nantes','Bordeaux'],\
    'Spain':['Madrid','Barcelona','Valencia','Cordoba','Sevilla'],\
    'Poland':['Warsaw','Krakow','Wroclaw','Poznan','Szczecin','Gdansk'],\
    'Ukraina':['Kyiv','Lviv','Poltava','Odesa','Dnipro','Harkiv','Pivne','Ternopil']}

search=input('Enter the sity: ')
print([key for key,value in europe_dict.items() if search in value])

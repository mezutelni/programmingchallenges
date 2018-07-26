from random import randint
#Stale sylaby sluzace do generowania nickow
sylaby = ("en","le","lo","don","te","per","lni","kan","mit","man","ka","sa","ki","shi"
          ,"mo","hi","yo","wa","ri","ise","ni","bo","me","zu")


#Funkcja generujaca
def random_name_generator(sylaby):
    nick_len = randint(2, 5)
    x = []
    for i in range(0,nick_len):
        x.append( sylaby[randint(0,len(sylaby)-1)])

    #Funkcja join lacze wszystkie wartosci w tablicy w string
    x = "".join(x)
    if len(x) > 6:
        x = x[:5]+" "+x[5:]

    return x

x = random_name_generator(sylaby)
print (x.title())

import random



lista=[]
i=0
while(i<15):
    randomszam:int=int(random.randint(-90,500))
    lista.append(randomszam)
    i+=1

def masodikfeladat():
    print("II/A,B,C")
    i=0
    while i <len(lista):
        if i <15:
            print(f"{lista[i]}", end="*")
        else:
            print(f"{lista[i]}", end="")
        i+=1

def oszthatoak():
    print("II/D,E")
    index = 0
    eredmeny = 0
    while index < len(lista):
        if lista[index] < 10:
            eredmeny += 1
        index += 1
    return eredmeny


def fajlba_kiir():
    f = open("kimutatas.txt","w",encoding="utf-8")
    f.write("II/F\n")
    f.write(f"\tTízzel osztható számok száma:  : {oszthatoak()} ")
    f.close()



def konzolra_kiir():
    print("II/E,F:",oszthatoak())
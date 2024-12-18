def elsofeladat():
    print("I/A")
    muzeumok:str=str(input("Múzeum neve:"))
    nev:str=str(input("Látogató neve:"))
    ertekeles:int=int(input("Értékelés(1-20):"))
    


    print("I/B")
    if ertekeles< 0:
        print("Az értékelés nem lehet negatív vagy 0!")
    elif ertekeles==0:
        print("Az értékelés nem lehet negatív vagy 0!")
    elif ertekeles>20:
        print("20 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")



try:
    broj=float(input("unesite broj izmedu [0.0] i [1.0]"))
    if broj<0.0 and broj > 1.0:
        print("Ocjena mora biti izmedu 0.0 i 1.0")
    elif broj>=0.9:
        print("Ocjena je A")
    elif broj>=0.8:
        print("Ocjena je B")
    elif broj>=0.7:
        print("Ocjena je C")
    elif broj>=0.6:
        print("Ocjena je D")
    elif broj<0.6:
        print("Ocjena je F")        
except ValueError:
    print("Unesite broj za ocjenu")
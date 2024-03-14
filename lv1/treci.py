numbers=[]
while True:
    user_input=input("Unesite broj ili 'Done' za kraj unosa:")
    if user_input.lower()=='done':
        break
    

    try:
        number=float(user_input)
        numbers.append(number)
    except ValueError:
        print("Neispravan unos")

if numbers:
    print("brojevi koji ste unijeli",numbers)
    print("broj unesenih brojeva",len(numbers))
    print("Srednja vrijednost",sum(numbers)/len(numbers))
    print("Minimalna vrijednost",min(numbers))
    print("Maksimalna vrijednost",max(numbers))

    numbers.sort()
    print("Sortirani brojevi", numbers)

else:
    print("Niste unijeli broj")    

file_name = input("Unesite ime datoteke: ")

try:
    with open(file_name, 'r') as file:
        total_confidence = 0
        count = 0
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    confidence = float(line.split(":")[1])
                    total_confidence += confidence
                    count += 1
                except ValueError:
                    print("Neuspješno parsiranje linije:", line)
        
        if count > 0:
            average_confidence = total_confidence / count
            print("Average X-DSPAM-Confidence:", average_confidence)
        else:
            print("Nije pronađena niti jedna linija X-DSPAM-Confidence u datoteci.")

except FileNotFoundError:
    print("Datoteka '{}' nije pronađena.".format(file_name))

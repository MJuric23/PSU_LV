def total_euro(work_hours,euro_h):
    total=work_hours*euro_h
    return total


work_hours=float(input("unesite radne sate:"))
euro_h=float(input("unesite euro/h:"))
total=total_euro(work_hours,euro_h)
print(total)

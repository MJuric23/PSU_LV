import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols = (1, 2, 3, 4, 5, 6), delimiter = ",", skiprows = 1)

mpg = data[:, 0]
hp = data[:, 3]
wt = data[:, 5]

plt.figure(1)
plt.title("Automobili")
plt.scatter(hp, mpg, s = wt*10)
plt.xlabel("hp")
plt.ylabel("mpg")
plt.show()

print("Najmanja potrosnja je: ", np.amin(mpg))
print("Najveca potrosnja je: ", np.amax(mpg))
print("Prosijecna potrosnja je: ", np.mean(mpg))

cyl = data[:, 1]
potr6cl = np.zeros((data.shape[0], 1))

brojac = int(0)
for i in range(0, potr6cl.shape[0]):
    if cyl[i] == 6:
        potr6cl[i] = mpg[i]

print(potr6cl) # izbaciti nule i izracunati bez njih


print("Najmanja potrosnja za 6 cilindra je: ", np.amin(potr6cl))
print("Najveca potrosnja za 6 cilindra je: ", np.amax(potr6cl))
print("Prosijecna potrosnja za 6 cilindra je: ", np.mean(potr6cl)) 
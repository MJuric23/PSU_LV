import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f'Label: {y_train[i]}')
    plt.axis('off')
plt.tight_layout()
plt.show()



# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()
# Kreiranje modela
model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Prikaz strukture modela
model.summary()


# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])



# TODO: provedi treniranje mreze pomocu .fit()

history = model.fit(x_train_s, y_train_s, epochs=10, batch_size=32, validation_split=0.1)



# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje

# Izračun točnosti na skupu podataka za učenje
train_loss, train_acc = model.evaluate(x_train_s, y_train_s, verbose=0)
print(f'Train accuracy: {train_acc:.4f}')

# Izračun točnosti na skupu podataka za testiranje
test_loss, test_acc = model.evaluate(x_test_s, y_test_s, verbose=0)
print(f'Test accuracy: {test_acc:.4f}')


# TODO: Prikazite matricu zabune na skupu podataka za testiranje

# Predikcije na testnom skupu
y_pred = model.predict(x_test_s)
y_pred_classes = np.argmax(y_pred, axis=1)

# Konverzija stvarnih labela u indekse klasa
y_test_classes = np.argmax(y_test_s, axis=1)

# Izračun matrice zabune
conf_matrix = confusion_matrix(y_test_classes, y_pred_classes)

# Prikaz matrice zabune
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()


# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala

# Pronalaženje primjera koje je mreža pogrešno klasificirala
misclassified_idx = np.where(y_pred_classes != y_test_classes)[0]

# Prikaz nekoliko pogrešno klasificiranih primjera
plt.figure(figsize=(10, 10))
for i, idx in enumerate(misclassified_idx[:25]):
    plt.subplot(5, 5, i + 1)
    plt.imshow(x_test[idx].reshape(28, 28), cmap='gray')
    plt.title(f'True: {y_test_classes[idx]}\nPredicted: {y_pred_classes[idx]}')
    plt.axis('off')
plt.tight_layout()
plt.show()


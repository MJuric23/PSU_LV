import numpy as np
import matplotlib.pyplot as plt

def create_checkerboard(square_size, num_squares_height, num_squares_width):
    # Odredimo dimenzije slike
    height = square_size * num_squares_height
    width = square_size * num_squares_width
    
    # Stvaramo crno i bijelo polje
    black_square = np.zeros((square_size, square_size), dtype=np.uint8)
    white_square = np.ones((square_size, square_size), dtype=np.uint8) * 255
    
    # Kreiramo praznu sliku
    img = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(num_squares_height):
        for j in range(num_squares_width):
            # Naizmjenično postavljamo crne i bijele kvadrate
            if (i + j) % 2 == 0:
                img[i*square_size:(i+1)*square_size, j*square_size:(j+1)*square_size] = black_square
            else:
                img[i*square_size:(i+1)*square_size, j*square_size:(j+1)*square_size] = white_square
                
    return img

# Postavke
square_size = 50
num_squares_height = 6
num_squares_width = 8

# Stvaramo sliku
img = create_checkerboard(square_size, num_squares_height, num_squares_width)

# Prikazujemo sliku
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()

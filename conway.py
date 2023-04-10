import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def random_matrix(N):
    return np.where(np.random.rand(N,N)>=0.5, 1, 0)


def sum_cells(mat, i, j):
    N = mat.shape[0]
    sm = mat[i, (j-1)%N] + \
         mat[i, (j+1)%N] + \
         mat[(i-1)%N, j] + \
         mat[(i+1)%N, j] + \
         mat[(i-1)%N, (j-1)%N] + \
         mat[(i-1)%N, (j+1)%N] + \
         mat[(i+1)%N, (j-1)%N] + \
         mat[(i+1)%N, (j+1)%N]
    return sm


def update(ii, img, mat, N):
    new_mat = mat.copy()
    for i in range(N):
        for j in range(N):
            total = sum_cells(mat, i, j)
            if mat[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_mat[i, j] = 0
            else:
                if total == 3:
                    new_mat[i, j] = 1
    img.set_data(new_mat)
    mat[:] = new_mat[:]
    return img,


N = 100
interval= 50
mat = random_matrix(N)

fig, ax = plt.subplots()
img = ax.imshow(mat, cmap='gray')

ani = FuncAnimation(fig, update,
                    fargs=(img, mat, N),
                    frames=10,
                    interval=interval,
                    save_count=50)
plt.show()
                    

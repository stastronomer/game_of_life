import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, h = 50, w = 50):

        '''p: probaility for number of live cases (i.e. 1)
        h, w: dimenstions of the grid
        '''

        np.random.seed(55) #seed for reproducing
        #initialize variables
        self.h = h  
        self.w = w
        self.arr0 = np.random.choice([0, 1], size=(h,w))
        #self.arr0 = np.array([[0,0,0,0,0], [0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
        #print(self.arr0)

        fig, ax = plt.subplots()
        img = ax.imshow(self.arr0, interpolation='nearest', cmap='gray')
        ani = animation.FuncAnimation(fig, self.next_state, fargs=(img, self.arr0), frames = 100, interval=100, save_count=50)
        plt.title("John Conway's Game of Life", fontsize=15, c='r')
        plt.axis('off')
        plt.show()

        #arr_t = self.next_state(self.arr0)
        
        #for i in range(0, max_iter):
        #    plt.imshow(arr_t, interpolation='nearest', cmap='gray')
        #    arr_t = self.next_state(arr_t)
        #    plt.colorbar()
        #    plt.show()



    def neigh(self, arr, i, j):
        self.arrp = arr
        arr = self.arrp
        m, n = arr.shape  # Get the shape of the array
        
        # Ensure that i and j are within valid bounds
        
        if i == 0:
            rows = [m - 1, 0, 1]
        elif i == m - 1:
            rows = [i - 1, i, 0]
        else:
            rows = [i - 1, i, i + 1]

        if j == 0:
            cols = [n - 1, 0, 1]
        elif j == n - 1:
            cols = [j - 1, j, 0]
        else:
            cols = [j - 1, j, j + 1]

        nei = [arr[x, y] for x in rows for y in cols if not (x == i and y == j)]
        

        return nei



    def next_state(self, frnum, img, arr0):
        self.frnum = frnum
        self.arr0 = arr0
        self.img = img
        arr1 = self.arr0.copy()
        for i in range(self.arr0.shape[0]):
            for j in range (self.arr0.shape[1]):
                sub_arr = self.arr0[max(0, i-1):min(self.arr0.shape[0], i+2), max(0, j-1):min(self.arr0.shape[1], j+2)]
                num = np.sum(sub_arr) - arr0[i,j]
        
                if self.arr0[i,j]:
                    if num<2 or num>3:
                        arr1[i,j] = 0
                else:
                    if num == 3:
                        arr1[i,j] = 1
        self.img.set_data(arr1)
        self.arr0[:] = arr1[:]
        return img

    def next_state_tor(self, frnum, img, arr0):
        self.frnum = frnum
        self.arr0 = arr0
        self.img = img
        arr1 = self.arr0.copy()
        for i in range(self.arr0.shape[0]):
            for j in range(self.arr0.shape[1]):
                num = sum(self.neigh(self.arr0, i, j))
            if self.arr0[i,j]:
                if num<2 or num>3:
                    arr1[i,j] = 0
                else:
                    if num == 3:
                        arr1[i,j] = 1
        self.img.set_data(arr1)
        self.arr0[:] = arr1[:]
        return img
        

    def display(self, arr, Toroid=True):

        self.arr = arr
        self.Toroid = Toroid
        if self.Toroid: 
            plt.imshow(self.next_state_tor(self.arr))

        else:
            plt.imshow(self.next_state(self.arr))

        plt.colorbar()
        plt.show()

    


g = GameOfLife()

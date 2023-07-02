import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


import pygame
import random
import time

#Class that deals with the visual elements of the program
class CreateWindow:
    windowH = 0
    windowW = 0
    window_background = 0, 0, 0,

    #constructor
    def __init__ (self, height, width, window_background):
        self.windowH = height
        self.windowW = width
        self.window_background = window_background
        self.window = pygame.display.set_mode((self.windowW, self.windowH))
        self.window.fill(self.window_background)
        pygame.display.set_caption("Sorting Algorithm Visualisation")

    #takes the current state of the array as an input and draws the rectangles that represent the ints in the array
    def draw_rectangles(self, arr):
        RED = 255, 0, 100
        ###################
        PASTEL_RED = 255, 105, 97
        temp_x = 0.1 * self.window.get_width()
        temp_y = 0.20 * self.window.get_height()
        temp_width = 0.8 * self.window.get_width()
        temp_height = 0.75 * self.window.get_height()
        pygame.draw.rect(self.window, PASTEL_RED, (temp_x, temp_y, temp_width, temp_height))
        ###################

        # calculate the width of one rectangle
        rectangle_width = temp_width / len(arr)
        unit_height = temp_height / max(arr)
        
        for i in range(len(arr)):
            rectangle_height = unit_height * arr[i]
            y = self.window.get_height()*0.95 - rectangle_height
            x = round(self.window.get_width() - 0.9*self.window.get_width() + i*rectangle_width)
            pygame.draw.rect(self.window, RED, (x, y, rectangle_width, rectangle_height))
            pygame.display.update()


class Algorithm:
    min = None  #min value of the array
    max = None  #max value of the array
    arr = []  #the array (ini off as empty)

    #constructor
    def __init__(self, min, max):
        self.min = min
        self.max = max

    #creates the array (initially in ascending order)
    def create_list(self):
        for i in  range(self.min, self.max+1):
            self.arr.append(i)
        return self.arr

    #randomises the array and returns it 
    def randomise_list(self, arr):
        random.shuffle(arr)
        return arr

    #bubble sort in ascending order
    def bubble_sort(self, arr, window):

        for i in range(len(arr)):
            swap = False
            for j in range(0, len(arr) - 1 - i):
                if arr[j] > arr[j+1]:
                    swap = True
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    print(arr)
                    window.draw_rectangles(arr)

            if swap == False:
                break



#main class (driver)
def main():
    print ("Hellow World")

    min = 1     #min value of the array
    max = 10    #max value of the array
    arr = []    #array (starts off as empty) 

    #instance of Algorithm class
    algorithm = Algorithm(min, max)
    #append elemnts to the array
    arr = algorithm.create_list()

    #variables for creating the window/visual elements
    windowW = 1000
    windowH = 750
    window_background = (253, 253, 150) #Pastel Yellow
    #instance of CreateWindow class
    window = CreateWindow(windowH, windowW, window_background)

    #variables the store the different states of the program
    running = True
    order = None
    sort = None

    arr = algorithm.randomise_list(arr)
    window.draw_rectangles(arr)

    while running:
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

        algorithm.bubble_sort(arr, window)

    #quit game when you jump out of the loop
    pygame.quit()





if __name__ == "__main__":
    main()
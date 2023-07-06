import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


import pygame
import random
import time
import math

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
        SHADES_OF_RED = [[0,114,187], [0,119,190], [0,127,191] ]
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
        unit_height = math.floor(temp_height / max(arr))
        
        for i in range(len(arr)):
            COLOUR = SHADES_OF_RED[i % 3] 
            rectangle_height = unit_height * arr[i]
            y = math.floor(self.window.get_height()*0.95 - rectangle_height)
            x = math.floor(self.window.get_width() - 0.9*self.window.get_width() + i*rectangle_width)
            pygame.draw.rect(self.window, COLOUR, (x, y, rectangle_width, rectangle_height))
            pygame.display.update()

    #displays and updates the text elements 
    def draw_textbox(self, order, sort): 
        #Text box variables
        text_x = self.window.get_width() * 0.1  
        text_y = self.window.get_height() * 0.02
        text_width = self.window.get_width() * 0.8
        text_height = self.window.get_height() * 0.15
        text_colour = 119, 221, 119
        
        pygame.draw.rect(self.window, text_colour, (text_x, text_y, text_width, text_height))
        
        #the text that contains the information/commands
        pygame.font.init()
        textbox_info_x = self.window.get_width() * 0.06
        textbox_info_y = self.window.get_height() * 0.08
        textbox_info_width = self.window.get_width() * 0.09
        textbox_info_height= self.window.get_height() * 0.12
        textbox_info_rect = pygame.Rect(textbox_info_x, textbox_info_y, textbox_info_width, textbox_info_height)
        text_info_colour = (0, 0, 0)  # Black
        textbox_font = pygame.font.Font(None, round(self.window.get_width() / 55.556))
        text_info = "A - Ascending / D - Descending / R - Randomise / S - Stop / B - Bubble Sort / Q - Quick Sort / M - Merge Sort / I - Insertion Sort / H - Heap Sort"

        text_surface = textbox_font.render(text_info, True, text_info_colour)
        text_rect = text_surface.get_rect(bottomleft=textbox_info_rect.center)
        self.window.blit(text_surface, text_rect)

        #the text that contains the state of the program (i.e Ascdending - Bubble Sort)
        textbox_state_x = self.window.get_width() * 0.5
        textbox_state_y = self.window.get_height() * 0.02
        textbox_state_width = self.window.get_width() * 0.09
        textbox_state_hight = self.window.get_height() * 0.12
        textbox_state_rect = pygame.Rect(textbox_state_x,  textbox_state_y, textbox_state_width, textbox_state_hight)
        #textbox_state_font = pygame.font.Font = (None, round(self.window.get_width() / 50))
        textbox_state_font = pygame.font.Font(None, round(self.window.get_width() / 40))
        #decide on what the text should be
        if order == None and sort == None:
            textbox_state_text = "Choose the Order / Choose a Sorting Algorithm"
        if order != None and sort == None:
            textbox_state_text = order + " / Choose a Sorting Algorithm"
        if order == None and sort != None:
            textbox_state_text = "Choose the order / " + sort
        if order != None and sort != None:
            textbox_state_text = order + " / " + sort
        # textbox_state_text = ""

        textbox_state_surface = textbox_state_font.render(textbox_state_text, True, text_info_colour)
        textbox_state_rect = textbox_state_surface.get_rect(center = textbox_state_rect.center)
        self.window.blit(textbox_state_surface, textbox_state_rect)


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

    #bubble sort 
    def bubble_sort(self, arr, window, order):

        for i in range(len(arr)):
            swap = False
            for j in range(0, len(arr) - 1 - i):
                if arr[j] > arr[j+1]:
                    swap = True
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    #print(arr)
                    window.draw_rectangles(arr)

            if swap == False:
                break

    #quick sort
    #function to find the partition position
    def partition(self, arr, low, high, window, order):
        #rightmost element = pivot
        pivot = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                window.draw_rectangles(arr)

                (arr[i], arr[j]) = (arr[j], arr[i])
                window.draw_rectangles(arr)

        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
        window.draw_rectangles(arr)

        return i + 1

    #quicksort algorithm
    def quick_sort(self, arr, low, high, window, order):
        if low < high:

            #smaller than pivot on left, greater than pivot on right
            pivot = self.partition(arr, low, high, window, order)

            #left of pivot
            self.quick_sort(arr, low, pivot - 1, window, order)

            #right of pivot
            self.quick_sort(arr, pivot + 1, high, window, order)

    #merge sort
    def merge_sort(self, arr, start, length, window, order):
        if length > 1:
            self.merge_sort(arr, start, length//2, window, order)
            self.merge_sort(arr, start+length//2, length - length//2, window, order)
        
        L = arr[start:start+length//2]
        R = arr[start+length//2:start+length]
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[start+k] = L[i]
                window.draw_rectangles(arr)
                i += 1
            else:
                arr[start+k] = R[j]
                window.draw_rectangles(arr)
                j += 1
            k += 1

        while i < len(L):
            arr[start+k] = L[i]
            window.draw_rectangles(arr)
            i += 1
            k += 1

        while j < len(R):
            arr[start+k] = R[j]
            window.draw_rectangles(arr)
            j += 1
            k += 1

        window.draw_rectangles(arr)

    #insertion sort
    def insertion_sort(self, arr, window, order):

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
              
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
                window.draw_rectangles(arr)
            
            #move key after element that is bigger than
            arr[j + 1] = key
            window.draw_rectangles(arr)

    #heap sort
    def heapify(self, arr, n, i, window, order):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          window.draw_rectangles(arr)
          self.heapify(arr, n, largest, window, order)

    def heap_sort(self, arr, window, order):
        #build max 
        for i in range(len(arr)//2, -1, -1):
            self.heapify(arr, len(arr), i, window, order)

        for i in range(len(arr)-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            window.draw_rectangles(arr)

            #heapify root 
            self.heapify(arr, i, 0, window, order)


#main class (driver)
def main():
    print ("Hellow World")

    min = 1     #min value of the array
    max = 50    #max value of the array
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

    # arr = algorithm.randomise_list(arr)
    window.draw_textbox(order, sort)
    window.draw_rectangles(arr)

    while running:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                #r - randomise the list
                if event.key == pygame.K_r:
                    arr = algorithm.randomise_list(arr)
                    window.draw_rectangles(arr)

                #b - bubble sort
                if event.key == pygame.K_b:
                    sort = "Bubble Sort"
                    window.draw_textbox(order, sort)
                    algorithm.bubble_sort(arr, window, order)
                    
                #q - quick sort
                if event.key == pygame.K_q:
                    sort = "Quick Sort"
                    window.draw_textbox(order, sort)
                    algorithm.quick_sort(arr, 0, len(arr)-1, window, order)
                    

                #m - merge sort
                if event.key == pygame.K_m:
                    sort = "Merge Sort"
                    window.draw_textbox(order, sort)
                    algorithm.merge_sort(arr, 0, len(arr), window, order)
                    

                #i - insertion sort
                if event.key == pygame.K_i:
                    sort = "Insertion Sort"
                    window.draw_textbox(order, sort)
                    algorithm.insertion_sort(arr, window, order)
                    

                #h - heap sort
                if event.key == pygame.K_h:
                    sort = "Heap Sort"
                    window.draw_textbox(order, sort)
                    algorithm.heap_sort(arr, window, order)

                #s - stop sorting
                if event.key == pygame.K_b:
                    sorting = None

        pygame.display.update()


    #quit game when you jump out of the loop
    pygame.quit()





if __name__ == "__main__":
    main()
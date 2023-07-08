# Sorting Algorithm Visualisation

## Aims of the project
- Produce a visualiser for the following sorting algorithms: bubble sort, quick sort, merge sort, insertion sort and heap sort.
- Give the user the ability to chose which one of the following sorting algorithms they would like to visualise, and in which order the array is to be sorted.

## Overview of the program
![image](https://github.com/angh-el/SortingAlgorithmVisualisation/assets/123000792/b6e3a992-9bca-4f1e-88ee-d6eb77629acf)

## How it works
- the program is split into 3 classes:
-  Main class: the main loop that takes user inputs then calls other functions
- Algorithm class: the class that deals with the list. Contains functions such as create_list() and randomise_list() but also all the sorting algorithms
- CreateWindow class: the class that deals with the visual elements. It creates the window, but also has functions that update the text box at the top of the screen
and functions that draw recatancgles that represent the current list (this function is called every time there is a mutation in the list and at the end of each algorithms to display the final result)

## How to install and run the program, and other requirements
-  the program is written in python, therefore the installation of python is necessary before running the program
- clone the repository ->
**_git clone https://github.com/angh-el/SortingAlgorithmVisualisation_**
-  navigate to the repository ->
 **_cd SortingAlgorithmVisualisation_**
-  to install pygame ->
**_pip install pygame_**
-  to run the program ->
**_python SortingAlgorithmVisualisation.py_**

## How to use the program
- the program takes char inputs from the user
- ![image](https://github.com/angh-el/SortingAlgorithmVisualisation/assets/123000792/19b86c5b-0073-402e-9531-ec9fe2aa8558)
- **Ascending** or **Descending**: determine the order in which the array is to be sorted
- **Randomise**: randomises the list, as initially the list is presented in sorted order (ascending)
- before: ![image](https://github.com/angh-el/SortingAlgorithmVisualisation/assets/123000792/89161702-1057-46d8-8908-acd59d451465)
- after: ![image](https://github.com/angh-el/SortingAlgorithmVisualisation/assets/123000792/93aab2d5-0f16-4492-874a-53249d602e35)
- it is recommended that the users randomise the list, select the order, then select the sorting algorithm
- randomising the list is not necessary for the program to be executed, however choosing an order and sort is
- the program will only start sorting once the user chooses the type of sort
- the program stores the previous order used, therefore it is not necessary to specify it each time



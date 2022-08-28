# The-Path-Finding-Visulizer

It is Build in python pygame. Implemented Breath first search, A* Search and Depth First Search algorithm for finding path between 2 nodes.
Have first look at it.. Described how to use it below.

![Path Finding Visulizer 28-08-2022 13_38_41](https://user-images.githubusercontent.com/52308072/187064418-25d12cbd-3173-42b0-adcc-b315152ac87a.png)


### Dragging the Nodes.
There are 2 nodes starting node(green) and ending node(red) you can darg them to any position in the grid(graph).

![movenodes](https://user-images.githubusercontent.com/52308072/187064920-46c04ca7-2800-4dc7-8c26-864787f5e194.gif)

### Drawing the obstacles.
You can drag on empty part grid to draw the obstacles between the 2 nodes. 

![DrawObstecls](https://user-images.githubusercontent.com/52308072/187067776-8bce03a2-d01d-4d71-a064-695fe0fa468f.gif)


## Visualizing the Breath First Search.
Press Breath First Search Button to start bfs algorithm visulization. When algorithm starts instruction regarding nodes in algorithm appers at bottom of screen

![bfs](https://user-images.githubusercontent.com/52308072/187067818-1aa90971-bf1a-4518-9a43-5d8a14f52ec3.gif)

## Visualizing the Depth First Search

![dfs](https://user-images.githubusercontent.com/52308072/187067968-c59ac1de-eab2-49dc-9751-9f4fe90c04ef.gif)

## Visualizing the A* Search

![astart](https://user-images.githubusercontent.com/52308072/187068358-5025bb0a-5329-41d7-a27c-8ffd9b5f540e.gif)


### Drawing the maze
You can get random maze of obstacles between the nodes. By clicking on Horizental Maze, Vartical Maze, and Random Maze.

![Maze](https://user-images.githubusercontent.com/52308072/187068451-b65849c5-ec48-49b9-acc2-1531091b8b1b.gif)

### Reset and Stop
Reset and stop button will set nodes to their initial state and clear the grid completely. It can also stop alogrithms while running.

![reset](https://user-images.githubusercontent.com/52308072/187068498-611c79fb-4fbe-4c6e-b492-c53e2a7dfdf9.png)

### Speed
You can change the speed of visualization using following buttons. By default it is set to fast.

![speed](https://user-images.githubusercontent.com/52308072/187068569-ecce4cb4-021b-4cca-9d17-c997b1da0cc4.png)

So this is the basic illustration of The Path Finding Visulizer.

## How to run it on your PC.
Make sure you are running atleast python 3.7.0.

Install using pip:
```
pip install pygame
```
Then clone this repository.
```
git clone https://github.com/sahil1699/The-Path-Finding-Visulizer.git
```

## Start Project
In your terminal move to the directory where you have cloned this project.
And then type :
```
python main.py
```

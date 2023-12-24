# The Path Finding Visualizer

This project, developed in Python using the Pygame library, serves as a visual tool for exploring pathfinding algorithms. It features three prominent algorithms: Breadth-First Search, A* Search, and Depth-First Search, all designed to find the optimal path between two nodes. Below, we'll provide an overview of how to use this project effectively.

![Breadth-First Search](https://user-images.githubusercontent.com/52308072/187073176-7a02e06c-6fc2-44e6-8d05-b042397d9b54.gif)

### Node Manipulation

The visualizer starts with two nodes, a starting node (green) and an ending node (red). You can drag these nodes to any position on the grid.

![Node Manipulation](https://user-images.githubusercontent.com/52308072/187064920-46c04ca7-2800-4dc7-8c26-864787f5e194.gif)

### Creating Obstacles

To introduce obstacles between the starting and ending nodes, simply click and drag on the empty grid cells.

![Drawing Obstacles](https://user-images.githubusercontent.com/52308072/187067776-8bce03a2-d01d-4d71-a064-695fe0fa468f.gif)

## Visualizing Algorithms

#### Breadth-First Search

Press the "Breadth First Search" button to initiate a visualization of the BFS algorithm. As the algorithm runs, you'll receive instructions about the nodes involved at the bottom of the screen.

![Breadth-First Search](https://user-images.githubusercontent.com/52308072/187073176-7a02e06c-6fc2-44e6-8d05-b042397d9b54.gif)

#### A* Search

Similarly, you can visualize the A* algorithm by clicking the "A* Search" button. Just like with BFS, you'll receive step-by-step instructions as the algorithm progresses.

![A* Search](https://user-images.githubusercontent.com/52308072/187068358-5025bb0a-5329-41d7-a27c-8ffd9b5f540e.gif)

#### Depth First Search

To visualize the DFS algorithm, press the "Depth First Search" button. As before, you'll see guidance on the algorithm's progress at the bottom of the screen.

![Depth First Search](https://user-images.githubusercontent.com/52308072/187067968-c59ac1de-eab2-49dc-9751-9f4fe90c04ef.gif)

### Generating Mazes

You can create random mazes of obstacles between the nodes by selecting "Horizontal Maze," "Vertical Maze," or "Random Maze."

![Maze Generation](https://user-images.githubusercontent.com/52308072/187068451-b65849c5-ec48-49b9-acc2-1531091b8b1b.gif)

### Reset and Stop

The "Reset" button restores the nodes to their initial positions and clears the grid. It can also halt algorithms that are currently running.

![Reset and Stop](https://user-images.githubusercontent.com/52308072/187068498-611c79fb-4fbe-4c6e-b492-c53e2a7dfdf9.png)

### Adjusting Speed

You have the option to change the speed of the visualization using the speed control buttons. The default setting is "Fast."

![Speed Control](https://user-images.githubusercontent.com/52308072/187068569-ecce4cb4-021b-4cca-9d17-c997b1da0cc4.png)

## Running the Project Locally

To run this project on your PC, make sure you have at least Python 3.7.0 installed.

1. Install Pygame using pip:

   ```
   pip install pygame
   ```

2. Clone this repository:

   ```
   git clone https://github.com/sahil1699/The-Path-Finding-Visualizer.git
   ```

3. Start the project:

   In your terminal, navigate to the directory where you've cloned this project and execute:

   ```
   python main.py
   ```

# ParkingAvailabilitySystem
A smart parking system simulation built with Python and Pygame that finds the nearest available parking spot from a defined entry point. It uses AI-based pathfinding to allocate spots efficiently, simulating real-time vehicle movement in a grid-based layout for smart city applications.
Parking System with Pathfinding 
and Adversarial Decision-Making 
Simulation
Introduction: 
In this project, we have developed a parking system that incorporates both pathfinding and adversarial 
decision-making. The system is designed to simulate a parking lot scenario, where the user must find the 
shortest path to a parking slot, while accounting for possible adversarial actions that might block the available 
parking spots. The core algorithms used in this system include the A* pathfinding algorithm for navigation and 
Alpha-Beta pruning to simulate adversarial behavior. The system is built using Python and includes a 
Graphical User Interface (GUI) created with the Tkinter library.
2. Objectives
The primary goals of this project are:
• To implement an A* pathfinding algorithm to find the optimal path to a parking slot.
• To simulate adversarial decision-making using the Alpha-Beta pruning algorithm, which evaluates 
blocking behavior in the parking system.
• To create an interactive GUI that allows the user to input parking slot coordinates, check availability, 
and make parking decisions based on the results.
3. System Design and Architecture
The system is built around the concept of a grid-based parking layout, where each parking space is 
represented by a cell in a 2D grid. The grid uses 1 to represent obstacles (unavailable parking spaces) and 0 to 
represent available parking spaces.
The architecture consists of two main components:
1. Pathfinding Module (ParkingSystem class):
o Attributes:
▪ grid: A 2D array representing the parking lot, with 0 for available spaces and 1 for 
obstacles.
▪ start: The starting position (entrance) of the vehicle.
o Key Methods:
▪ is_valid(x, y): Validates if a cell is within the grid bounds and not an obstacle.
▪ heuristic(x, y, end): Computes the Manhattan distance to the destination as a heuristic 
for the A* algorithm.
▪ a_star_search(destination): Implements the A* algorithm to find the shortest path to 
the target parking slot.
▪ adversarial_alpha_beta(node, depth, alpha, beta, maximizing_player, destination): 
Implements Alpha-Beta pruning for adversarial decision-making, simulating obstacles 
blocking the parking spot.
▪ check_and_park(row, col): Checks the availability of the parking slot and computes the 
adversarial blocking score, along with the pathfinding result.
▪ draw_grid(): Draws the grid layout on the screen.
▪ move_car(path): Animates the car along the computed path.
▪ park_car(destination): Marks the destination as occupied.
2. GUI Module (Pygame):
 - The user interacts with the GUI to select parking slots by clicking on the grid.
 - The system responds with a path to the selected slot or a message if the slot is unavailable.
4. Algorithms
A* Pathfinding Algorithm
The A* algorithm is used to find the shortest path in the parking grid from the entrance to the target parking 
slot. The algorithm operates by exploring nodes (grid cells) and using a heuristic (Manhattan distance) to 
estimate the cost to reach the destination.
• Heuristic Function: The Manhattan distance between the current node and the destination is used to 
estimate the cost of the remaining path.
• Open Set: A priority queue stores nodes to be explored, ordered by the sum of the path cost and 
heuristic value.
• Exploration: The algorithm explores neighboring cells (up, down, left, right) and chooses the one with 
the lowest cost.
Alpha-Beta Pruning
The Alpha-Beta pruning algorithm simulates the actions of an adversary attempting to block the parking slot. 
It works by simulating two players: the system, which tries to maximize its score by finding the optimal path, 
and the adversary, which tries to minimize the system’s score by blocking potential paths.
• Alpha: The best score for the maximizing player.
• Beta: The best score for the minimizing player.
When Alpha is greater than or equal to Beta, further exploration of the current path is stopped, optimizing the 
search.
5. User Interface
The GUI is implemented using the Pygame library. The main components are:
1. Grid Display:
 - The grid represents the parking lot with available and occupied slots.
2. User Interaction:
 - The user clicks on a grid cell to select a parking slot.
3. Messages:
 - Informational messages: Display the pathfinding result.
 - Error messages: Inform the user if the slot is unavailable or blocked.
 - Confirmation messages: Notify the user if the car is successfully parked.
4. Interactive Flow:
 - After selecting a slot, the system computes the path and displays it. If the slot is available, the car moves to 
the slot and parks.
6. System Functionality
1. Parking Slot Check:
o The system checks if the selected parking slot is available (not an obstacle).
o If available, the system proceeds to calculate the optimal path to the parking spot using A* 
pathfinding.
2. Adversarial Blocking Simulation:
o Using Alpha-Beta pruning, the system evaluates the potential adversarial actions and calculates 
a blocking score. This score represents the difficulty of reaching the slot due to possible 
obstacles.
3. User Interaction:
o The user is shown the pathfinding results and adversarial score. They can decide whether to 
park in the selected slot or choose another.
7. Example Scenario
Consider the following grid layout:
grid = [
 [1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1],
 [1, 0, 0, 0, 1],
 [1, 0, 0, 0, 1],
 [1, 1, 1, 1, 1] 
]
• The starting point (entrance) is at (1, 1).
• The user checks parking at (3, 3), which is available.
• The A* algorithm finds the shortest path to (3, 3).
• The Alpha-Beta pruning algorithm simulates adversarial actions, and the system calculates a blocking 
score.
8. Challenges and Future Work
1. Obstacle Detection: The project assumes static obstacles, but future enhancements could include 
dynamic obstacles or real-time updates based on system status.
2. Pathfinding Optimization: The A* algorithm is efficient, but for larger grids or more complex 
environments, further optimizations or alternative algorithms (e.g., Dijkstra’s Algorithm) could be 
explored.
3. User Experience: Future versions of the GUI can include a visualization of the grid and the optimal path 
to make the experience more interactive.
9. Conclusion
This parking system project successfully integrates advanced algorithms (A* and Alpha-Beta pruning) to create 
a simulation that not only finds optimal parking paths but also accounts for adversarial actions. The GUI built 
using Tkinter allows users to interact with the system, check parking slot availability, and make informed 
decisions based on the computed results. This system can be expanded with additional features, including 
real-time obstacle detection and enhanced pathfinding algorithms for more complex environments.

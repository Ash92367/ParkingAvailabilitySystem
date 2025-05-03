import heapq
import pygame
import time

class ParkingSystem:
    def __init__(self, grid, start):
        self.grid = grid
        self.start = start
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.cell_size = 50  # Size of each cell in the grid
        self.screen = None
        self.car_color = (0, 0, 255)
        self.slot_color = (0, 255, 0)
        self.block_color = (255, 0, 0)
        self.path_color = (255, 255, 0)
        self.occupied_slots = set()

    def is_valid(self, x, y):
        """Check if a cell is valid for movement."""
        if not (0 <= x < self.rows and 0 <= y < self.cols):
            return False
        if self.grid[x][y] == 1 or (x, y) in self.occupied_slots:
            return False
        # Check if the green block is surrounded by red blocks
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        surrounded = all(0 <= x+dx < self.rows and 0 <= y+dy < self.cols and self.grid[x+dx][y+dy] == 1 for dx, dy in directions)
        return not surrounded

    def heuristic(self, x, y, end):
        """Calculate Manhattan distance as heuristic."""
        return abs(x - end[0]) + abs(y - end[1])

    def a_star_search(self, destination):
        """Perform A* search to find the optimal path."""
        pq = [(0, self.start, [self.start])]
        visited = set()

        while pq:
            cost, (x, y), path = heapq.heappop(pq)

            if (x, y) == destination:
                return path

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    new_cost = cost + 1
                    priority = new_cost + self.heuristic(nx, ny, destination)
                    heapq.heappush(pq, (priority, (nx, ny), path + [(nx, ny)]))

        return None  # No path found

    def draw_grid(self):
        """Draw the grid on the screen."""
        for x in range(self.rows):
            for y in range(self.cols):
                if (x, y) in self.occupied_slots:
                    color = self.block_color  # Red for occupied slots
                elif self.grid[x][y] == 1:
                    color = self.block_color  # Red for obstacles
                else:
                    color = self.slot_color  # Green for available slots
                rect = pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

    def draw_path(self, path):
        """Draw the path to the parking slot."""
        for x, y in path:
            rect = pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, self.path_color, rect)

    def move_car(self, path):
        """Animate the car along the path."""
        for x, y in path:
            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_path(path)

            # Draw the car
            car_rect = pygame.Rect(y * self.cell_size + 5, x * self.cell_size + 5, self.cell_size - 10, self.cell_size - 10)
            pygame.draw.rect(self.screen, self.car_color, car_rect)

            pygame.display.flip()
            time.sleep(0.5)

    def park_car(self, destination):
        """Mark the destination as occupied."""
        self.occupied_slots.add(destination)

    def show_popup(self, message):
        """Display a popup message."""
        font = pygame.font.Font(None, 24)  # Smaller font size
        text = font.render(message, True, (255, 255, 255))  # White text color
        text_rect = text.get_rect(center=(self.cols * self.cell_size // 2, self.rows * self.cell_size // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(2)

    def run(self):
        """Main loop to run the parking simulation."""
        pygame.init()
        self.screen = pygame.display.set_mode((self.cols * self.cell_size, self.rows * self.cell_size))
        pygame.display.set_caption("Parking System")

        running = True
        while running:
            self.screen.fill((255, 255, 255))
            self.draw_grid()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // self.cell_size, x // self.cell_size
                    if self.is_valid(row, col):
                        path = self.a_star_search((row, col))
                        if path:
                            self.move_car(path)
                            self.park_car((row, col))
                            self.show_popup("Parking Successful!")
                        else:
                            self.show_popup("No path found to the selected parking slot.")
                    else:
                        self.show_popup("Selected slot is unavailable or already occupied.")

        pygame.quit()

# Define a larger grid (1 = obstacle, 0 = free space)
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Starting point (entrance)
start = (1, 1)

# Initialize and run the parking system
parking_system = ParkingSystem(grid, start)
parking_system.run()

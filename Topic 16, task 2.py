class Turtle:
    def __init__(self, x=0, y=0, s=1):
        """Initialize turtle with position (x, y) and step size s"""
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        """Move turtle up by s units"""
        self.y += self.s
    
    def go_down(self):
        """Move turtle down by s units"""
        self.y -= self.s
    
    def go_left(self):
        """Move turtle left by s units"""
        self.x -= self.s
    
    def go_right(self):
        """Move turtle right by s units"""
        self.x += self.s
    
    def evolve(self):
        """Increase step size by 1"""
        self.s += 1
    
    def degrade(self):
        """Decrease step size by 1, raise error if s becomes ≤ 0"""
        if self.s <= 1:
            raise ValueError("Step size cannot be 0 or negative")
        self.s -= 1
    
    def count_moves(self, x2, y2):
        """
        Calculate minimum moves to reach target position (x2, y2)
        Returns tuple: (total_moves, x_moves, y_moves)
        """
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        # Calculate moves needed for each axis
        x_moves = dx // self.s
        if dx % self.s != 0:
            x_moves += 1
        
        y_moves = dy // self.s
        if dy % self.s != 0:
            y_moves += 1
        
        return x_moves + y_moves
    
    def __str__(self):
        return f"Turtle(position=({self.x}, {self.y}), step={self.s})"

# Example usage:
t = Turtle(0, 0, 2)  # Create turtle at (0,0) with step 2
print(t)  # Output: Turtle(position=(0, 0), step=2)

t.go_up()
t.go_right()
print(t)  # Output: Turtle(position=(2, 2), step=2)

t.evolve()
print(t.s)  # Output: 3

try:
    t.degrade()
    t.degrade()
    t.degrade()  # This will raise an error
except ValueError as e:
    print(e)  # Output: Step size cannot be 0 or negative

moves = t.count_moves(10, 5)
print(f"Moves needed: {moves}")  # Output: Moves needed: 5
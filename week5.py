class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom=bottom
        self.top=top
        self.current=current
        
    def up(self):
        """Makes the elevator go up one floor."""
        self.current = self.current+1
        return self.current
    def down(self):
        """Makes the elevator go down one floor."""
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        pass

elevator = Elevator(-1, 10, 0)
elevator.up() 
print(elevator.current) #should output 1
import math as m

class Termite:

    def __init__(self, posicion=(0, 0), color="red"):
        self.memory = []
        self.posicion = posicion
        self.color = color
        self.load = None

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color

    def moveUp(self, interval=1):
        return (self.posicion[0], self.posicion[1] + interval)

    def moveDown(self, interval=1):
        return (self.posicion[0], self.posicion[1] - interval)

    def moveRight(self, interval=1):
        return (self.posicion[0] + interval, self.posicion[1])

    def moveLeft(self, interval=1):
        return (self.posicion[0] - interval, self.posicion[1])

    # New functions for diagonal move

    def moveUpLeft(self, interval=1):
        return (self.posicion[0] - interval, self.posicion[1] + interval)
        
    def moveUpRight(self, interval=1):
        return (self.posicion[0] + interval, self.posicion[1] + interval)
        
    def moveDownLeft(self, interval=1):
        return (self.posicion[0] - interval, self.posicion[1] - interval)
        
    def moveDownRight(self, interval=1):
        return (self.posicion[0] + interval, self.posicion[1] - interval)
    
    # Method to calculate the euclidean distance between two points.
    def EuclideanDistance(self, start, end):
        # return int(M.sqrt(M.pow(start[0] - end[0], 2) + M.pow(start[1] - end[1], 2)))
        return int(m.dist(start, end))
        
    def move(self, limits, posChip, interval=1):
        
        self.memory.append(self.posicion)
        
        movesList = []
        
        # Generates movement within the limits        
        if self.posicion[1] < limits[1]:
            movesList.append(self.moveUp(interval))
            
        if self.posicion[1] > limits[0]:
            movesList.append(self.moveDown(interval))
            
        if self.posicion[0] > limits[2]:
            movesList.append(self.moveLeft(interval))
            
        if self.posicion[0] < limits[3]:
            movesList.append(self.moveRight(interval))       
        
        if self.posicion[1] < limits[1] and self.posicion[0] > limits[2]:
            movesList.append(self.moveUpLeft(interval))
            
        if self.posicion[1] < limits[1] and self.posicion[0] < limits[3]:
            movesList.append(self.moveUpRight(interval))
            
        if self.posicion[1] > limits[0] and self.posicion[0] > limits[2]:
            movesList.append(self.moveDownLeft(interval))
            
        if self.posicion[1] > limits[0] and self.posicion[0] < limits[3]:
            movesList.append(self.moveDownRight(interval))
            
        
        # Saving the values of every euclidean distance calculated
        EuclideanDistancesList = []
        
        # Calculating the euclidean distance for every move in my list
        for move in movesList:
            EuclideanDistancesList.append(self.EuclideanDistance(move, posChip))
            
        # Selecting the very first minimun distance
        minDistance = min(EuclideanDistancesList)
        
        # Looking for the index of the current minimun distance selected
        index = EuclideanDistancesList.index(minDistance)
                
        # Set the best movenent and do it.
        self.posicion = movesList[index]

    def pickChip(self, posChips):
        if self.posicion in posChips:
            self.memory.append(self.posicion)
            return self.posicion


class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index

    def getPos(self):
        return self.posicion
    
    def setPos(self, pos):
        self.posicion = pos

    def getColor(self):
        return self.color
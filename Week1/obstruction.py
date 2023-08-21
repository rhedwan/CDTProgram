from math import sqrt
from actualTime import ActualTime

class CheckObstruction:
    def __init__(self, pointA, pointB, speed):
        """
        Initialize the CheckObstruction class with point A, point B, speed, and actual time.

        pointA: List containing the coordinates of point A.
        pointB: List containing the coordinates of point B.
        speed: Speed of the machine in distance units per time unit.
        actualTime: Actual time taken to travel from point A to point B.

        """
        self.pointA = pointA
        self.pointB = pointB
        self.speed = speed

    def expectedTime(self):
        """
        Calculate the expected time to travel from point A to point B based on the speed.

        return: Expected time in time(minutes).
        """
        x1, x2 = self.pointA
        y1, y2 = self.pointB
        distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
        return distance / self.speed

    def checkObstruction(self):
        """
        Check if there is an obstruction based on the actual time and expected time.

        return: True if there is obstruction, False if there  is no obstruction.
        """
        if ActualTime().calActualTime()  > self.expectedTime() + 60:
            return False
        return True


if __name__ == "__main__":
    # Creating an instance of CheckObstruction
    check1 = CheckObstruction([53.5872, -2.4138], [53.474, -2.2388], 12)
    print(check1.checkObstruction())

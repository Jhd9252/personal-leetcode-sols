
'''
853. Car Fleet
Medium
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.


Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Given position where position[i] is starting mile of ith car
        Given speed where speed[i] is the miles per hour 
        Given target in mile
        Contraint: Cars cannot pass a car ahead of it. Thus forming groups.
        In other words, cars are bottle necked. 
        We want the amount of car fleets. This allows some movement of variables
        

        What we want is to sort the cars in position, and the time to arrive. 
        (position, time to finsih)
        time to finish = target - position / speed 

        if target is 10 miles, position is 0, and speed is 10, then it takes 1 to finish
        if target is 10 miles, position is 5, and speed is 10, then 10-5 = 5 miles to travel, with speed of 10, then .5 is time to finsih

        Starting from closest to finish time, cars are not allowed to overlap,
        stack = [(pos, ttf), (pos, ttf), (pos, ttf), (pos, ttf)]
        pop from the end, say that they are the closest to finishing, we want to keep popping if ttf is less than or equal to popped. that is one fleet. 
        we have that the clost position is the top of stack, so push thte farthest down first. 
        or rather, the lower pos is bottom of stack . 
        '''
        if target <= 0 or not position or not speed:
            return 0
        stack = []
        for pos, speed in zip(position, speed):
            ttf = (target-pos) / speed
            stack.append((pos, ttf))

        stack.sort()

        fleet = 0
        while stack:
            leader, time = stack.pop()
            fleet += 1
            while stack and stack[-1][1] <= time:
                stack.pop()
        return fleet
            
            

        
        
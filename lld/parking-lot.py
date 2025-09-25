from abc import ABC, abstractmethod
import itertools

class User:
    id_iter = itertools.count()
    def __init__(self):
        self.id = next(User.id_iter)

class ParkingSpot:
    id_iter = itertools.count()
    def __init__(self):
        self.parked = False
        self.id = next(ParkingSpot.id_iter)

class ParkingFloor:
    id_iter = itertools.count()
    def __init__(self, n: int):
        # be careful not to create references to same object
        self.spots = [[ParkingSpot() for _ in range(n)] for _ in range(n)]
        self.free = n * n 
        self.id = next(ParkingFloor.id_iter)

    def print_spots(self):
        for row in self.spots:
            print([x.parked for x in row])

class ParkingLot:
    id_iter = itertools.count()
    def __init__(self, floors: int, n: int):
        # be careful not to create references to same object
        self.floors = [ParkingFloor(n) for _ in range(floors)]
        self.id = next(ParkingLot.id_iter)
        self.free = floors

    def print_floors(self):
        for floor in self.floors:
            floor.print_spots()
            print('\n')

class SearchStrategy(ABC):
    @abstractmethod
    def search():
        pass

class Nearest(SearchStrategy):
    def lot(self, lot: ParkingLot):
        if lot.free == 0: raise ValueError()
        return lot

    def floor(self, lot: ParkingLot):
        for floor in lot.floors:
            if floor.free > 0:
                return floor
    def spot(self, floor: ParkingFloor):
        for i in range(len(floor.spots)):
            for j in range(len(floor.spots)):
                if floor.spots[i][j].parked == False:
                    return floor.spots[i][j]
    
    def search(self, lot: ParkingLot):
        res_lot = self.lot(lot)
        res_floor = self.floor(lot)
        res_spot = self.spot(res_floor)
        return res_lot, res_floor, res_spot
    
class MostFree(SearchStrategy):
    def lot(self, lot: ParkingLot):
        if lot.free == 0: raise ValueError()
        return lot
    def floor(self, lot: ParkingLot):
        fFloor = None
        fSpot = 0
        for floor in lot.floors:
            if floor.free > fSpot:
                fFloor = floor
                fSpot = floor.free
        return fFloor
    def spot(self, fFloor: ParkingFloor):
        for i in range(len(fFloor.spots)):
            for j in range(len(fFloor.spots[0])):
                if fFloor.spots[i][j].parked == False:
                    return fFloor.spots[i][j]
    def search(self, lot: ParkingLot):
        res_lot = self.lot(lot)
        res_floor = self.floor(res_lot)
        res_spot = self.spot(res_floor)
        return res_lot, res_floor, res_spot
    
class Manager:
    def __init__(self):
        self.strategies = {
            'nearest': Nearest(),
            'most_free': MostFree(),
        }
        self.current = {} # (user.id : (floor, spot, parked))
    def park(self, lot: ParkingLot, user: User, strat: str):
        res_lot, res_floor, res_spot = self.strategies[strat].search(lot)
        res_spot.parked = True
        res_floor.free -= 1
        if res_floor.free == 0:
            res_lot.free -= 1
        self.current[user.id] = (res_floor, res_spot, res_spot.parked)
        print('Parked at: ', res_floor.id, res_spot.id, res_spot.parked)

    def remove(self, lot: ParkingLot, user: User):
        # first check if user in parkinglot
        if user.id not in self.current:
            print('User not found')
            return 
        floor, spot, parked = self.current[user.id]
        spot.parked = False
        floor.free += 1
        if floor.free == 1:
            lot.free += 1
        self.current[user.id] = (floor, spot, spot.parked)
        print('Removed at: ', floor.id, spot.id, spot.parked)
    
            


if __name__ == '__main__':
    # # testing User
    # userA = User()
    # userB = User()
    # assert(userA.id == 0)
    # assert(userB.id == 1)

    # # testing parking spot
    # spotA = ParkingSpot()
    # assert(spotA.id == 0)
    # assert(spotA.parked == False)

    # # testing ParkingFloor
    # floorA = ParkingFloor(2)
    # assert(len(floorA.spots) == 2)
    # assert(floorA.free == 2*2)
    # assert(floorA.id == 0)

    # lotA = ParkingLot(2,3)
    # assert(len(lotA.floors) == 2)
    # assert(len(lotA.floors[0].spots) == 3)
    # assert(lotA.free == 2)

    # 2 floors, each floor is 3x3
    lotA = ParkingLot(2, 3) 
    manager = Manager()
    print('New ParkingLot')
    lotA.print_floors()

    # add userA 
    userA = User()
    manager.park(lotA, userA, 'nearest')
    print('After adding userA with Nearest Strat')
    lotA.print_floors()

    userB = User()
    manager.park(lotA, userB, 'most_free')
    print('After adding UserB with MostFree Strat')
    lotA.print_floors()

    manager.remove(lotA, userB)
    print('After removing UserB')
    lotA.print_floors()



    








class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for i in range(len(position)):
            car.append([position[i],speed[i]])
        car.sort(reverse=True)
        TimeOfFleet = []
        for i in range(len(car)):
            time = (target-car[i][0])/car[i][1]
            if i == 0:
                TimeOfFleet.append(time)
            else:
                if time>TimeOfFleet[-1]:
                    TimeOfFleet.append(time)
                else:
                    continue
        return len(TimeOfFleet)
            

            

        
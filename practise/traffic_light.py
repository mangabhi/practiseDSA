from enum import Enum 
class TrafficLight(Enum):
    RED=30
    YELLOW=5
    GREEN=25

    @property
    def duration(self)->int:
        return self.value
    
    def next(self)->"TrafficLight":
        transitions={
            TrafficLight.RED : TrafficLight.GREEN,
            TrafficLight.GREEN:TrafficLight.YELLOW,
            TrafficLight.YELLOW:TrafficLight.RED
        }
        return transitions[self]

    def display(self)->None:
        print(f"{self.name} : {self.duration}s")


# traffic=TrafficLight.RED

# for _ in range(6):
#     traffic.display()
#     traffic=traffic.next()




class StatusCode(Enum):
    OK=(200,"OK")
    BAD_REQUEST=(400,"Bad Request")
    NOT_FOUND=(404,"Not Found")
    INTERNAL_SERVER_ERROR=(500,"Internal Server Error")

    def __init__(self,code:int,message:str):
        self.code=code
        self.message=message

    def isSuccess(self)->bool:
        return self.code <400

    def display(self)->None:
        print(f"{self.code} {self.message}")

    @staticmethod
    def fromCode(code:int)->None:
        for status in StatusCode:
            if status.code == code:
                return status
        return None

# stats = StatusCode.NOT_FOUND
# print(StatusCode.fromCode(404))
# # stats.isSuccess()
# stats.display()
print(StatusCode.fromCode(404))



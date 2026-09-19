# class Car:
#     #constructor:
#     def __init__(self,brand,model):
#         #private attributes
#         self._model=model
#         self._brand=brand
#         self._speed=0

#     def get_car_speed(self,increment):
#         self._speed +=increment
#     #method
#     def get_display_info(self):
#         return f"{self._model} is good having {self._brand} with speed of {self._speed}"


# c1=Car("Toyota","Curizer")
# c1.get_car_speed(500)
# # print()
# print(c1.get_display_info())


class FoodDelivery:
    def __init__(self,order_id:str,customer_name:"str"):
        self._order_id=order_id
        self._customer_name=customer_name
        self._items:list[str]=[]
        self._total_amount=0.0
        self._is_placed=False

    #allow adding order before placing the order
    def add_items(self,name:str,price:float):
        if self._is_placed:
            print("Cannot Modify the order once placed")
            return
        self._items.append(name)
        self._total_amount +=price

    def place_order(self)->bool:
        if self._is_placed or not self._items:
            return False
        self._is_placed=True
        return True
    def get_item_count(self):
        return len(self._items)

    def display_order(self):
        status="PLACED" if self._is_placed else "PENDING"
        print(f"Order {self._order_id} ({self._customer_name} - {status})")
        for item in self._items:
            print(f" - {item}")
        print(f" Total Amount: {self._total_amount}")

if __name__ == "__main__":
    order1=FoodDelivery("ORD-101","Abhishek")
    order1.add_items("Biryani",12.90)
    order1.add_items("Ice-Cream",2.00)
    order1.add_items("Dal Makhni",0.20)
    order1.add_items("Palak Panner",22.90)
    order1.place_order()

    order2 = FoodDelivery("ORD-102", "Bob")
    order2.add_items("Burger", 9.99)
    order2.add_items("Fries", 3.99)

    order1.display_order()
    print()
    order2.display_order()
    order2.place_order()
    order2.display_order()

    

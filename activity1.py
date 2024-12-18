# Base Class
class Smartphone:
    def __init__(self, brand, model, price, battery_capacity):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_capacity = battery_capacity

    def call(self, number):
        return f"Dialing {number} from {self.model}..."

    def charge(self):
        return f"Charging {self.model}'s battery ({self.battery_capacity}mAh)..."

# Inherited Class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, battery_capacity, gpu, cooling_system):
        super().__init__(brand, model, price, battery_capacity)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        return f"Playing {game_name} on {self.model} with {self.gpu} and {self.cooling_system} cooling system."

# Example Usage
phone1 = Smartphone("Samsung", "Galaxy S21", 799, 4000)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 999, 6000, "Adreno 660", "Liquid Cooling")

print(phone1.call("1234567890"))
print(phone1.charge())
print(gaming_phone.call("0987654321"))
print(gaming_phone.play_game("Genshin Impact"))

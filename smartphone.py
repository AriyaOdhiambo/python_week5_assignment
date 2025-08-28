# Base class
class Smartphone:
    def __init__(self, brand, model, battery_capacity, storage):
        # Encapsulation: private attributes with underscore
        self._brand = brand
        self._model = model
        self._battery_capacity = battery_capacity  # in mAh
        self._storage = storage  # in GB
        self._is_power_on = False

    # Method to turn on the phone
    def power_on(self):
        if not self._is_power_on:
            self._is_power_on = True
            print(f"{self._brand} {self._model} is now ON.")
        else:
            print(f"{self._brand} {self._model} is already ON.")

    # Method to turn off the phone
    def power_off(self):
        if self._is_power_on:
            self._is_power_on = False
            print(f"{self._brand} {self._model} is now OFF.")
        else:
            print(f"{self._brand} {self._model} is already OFF.")

    # Method to check battery
    def check_battery(self):
        print(f"{self._brand} {self._model} has {self._battery_capacity} mAh battery.")

    # Getters and Setters (Encapsulation)
    def get_storage(self):
        return self._storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self._storage = new_storage
        else:
            print("Storage must be positive.")

    # Polymorphic method
    def install_app(self, app_name):
        print(f"Installing {app_name} on {self._brand} {self._model}...")

# Derived class (Inheritance)
class Android(Smartphone):
    def __init__(self, brand, model, battery_capacity, storage, android_version):
        super().__init__(brand, model, battery_capacity, storage)
        self.android_version = android_version

    # Overriding (Polymorphism)
    def install_app(self, app_name):
        print(f"Downloading {app_name} from Google Play on {self._brand} {self._model}.")

# Another derived class
class iPhone(Smartphone):
    def __init__(self, model, battery_capacity, storage, ios_version):
        super().__init__("Apple", model, battery_capacity, storage)
        self.ios_version = ios_version

    # Overriding (Polymorphism)
    def install_app(self, app_name):
        print(f"Downloading {app_name} from App Store on {self._brand} {self._model}.")

# Testing the classes
if __name__ == "__main__":
    samsung = Android("Samsung", "Galaxy S23", 5000, 256, "Android 14")
    iphone = iPhone("iPhone 15", 4350, 512, "iOS 17")

    samsung.power_on()
    samsung.install_app("WhatsApp")
    samsung.check_battery()

    print()

    iphone.power_on()
    iphone.install_app("Instagram")
    iphone.check_battery()

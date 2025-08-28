# 📱 OOP Assignment - Activity 1: Smartphone Class

## 📂 File: `smartphone.py`

This program creates a **Smartphone class** and demonstrates **encapsulation, inheritance, and polymorphism**.

---

## 📝 Steps Followed in the Code

### 1. Create the Base Class `Smartphone`
- Defined `__init__()` constructor with attributes:
  - `_brand`
  - `_model`
  - `_battery_capacity`
  - `_storage`
  - `_is_power_on`
- Marked attributes with `_` to indicate **encapsulation** (protected/private).
- Added methods:
  - `power_on()` → turns phone ON
  - `power_off()` → turns phone OFF
  - `check_battery()` → shows battery capacity
  - Getters & Setters for `storage`
  - `install_app()` → generic app installation

---

### 2. Create Child Class `Android`
- Inherits from `Smartphone`.
- Added new attribute: `android_version`.
- Overrode `install_app()` → installs apps via **Google Play**.

---

### 3. Create Child Class `iPhone`
- Inherits from `Smartphone`.
- Added new attribute: `ios_version`.
- Overrode `install_app()` → installs apps via **App Store**.

---

### 4. Test the Classes
- Created two objects:
  - `samsung = Android("Samsung", "Galaxy S23", 5000, 256, "Android 14")`
  - `iphone = iPhone("iPhone 15", 4350, 512, "iOS 17")`
- Called:
  - `power_on()`
  - `install_app()`
  - `check_battery()`
- Each class responded according to its own implementation (**polymorphism**).

---

## ▶️ How to Run
```bash
python smartphone.py

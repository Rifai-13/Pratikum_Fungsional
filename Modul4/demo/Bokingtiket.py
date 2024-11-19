from functools import wraps
from copy import deepcopy

# Constants
DESTINATIONS = [
    ("Jakarta", "Surabaya", 120),
    ("Jakarta", "Bali", 150),
    ("Surabaya", "Medan", 200),
    ("Medan", "Jakarta", 180),
    ("Bali", "Surabaya", 170)
]

# Data storage
accounts = {}
bookings = {}
friends = {}

# Decorator to log function execution
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

# Closure for maintaining a counter
def counter_closure():
    count = {"value": 0}

    def increment():
        count["value"] += 1
        return count["value"]

    def get_count():
        return count["value"]

    return increment, get_count

increment, get_count = counter_closure()

# First-Class Function: Accounts Handler
@log_execution
def handle_accounts(operation, *args, **kwargs):
    operations = {
        "register": lambda nik, name, password: (
            accounts.update({nik: {"name": name, "password": password}}) or "Account registered"
            if nik not in accounts
            else "NIK already registered"
        ),
        "login": lambda nik, password: (
            f"Welcome {accounts[nik]['name']}"
            if nik in accounts and accounts[nik]["password"] == password
            else "Invalid NIK or password"
        ),
        "edit_profile": lambda nik: (
            accounts[nik].update(kwargs) or "Profile updated"
            if nik in accounts
            else "Profile not found"
        ),
        "delete_account": lambda nik: (
            accounts.pop(nik, None) or "Account deleted"
            if nik in accounts
            else "Account not found"
        ),
    }
    return operations.get(operation, lambda *_: "Invalid operation")(*args)

# Higher-Order Function: Manage bookings
@log_execution
def manage_bookings(nik, action, *args):
    actions = {
        "book_flight": lambda flight_index: (
            bookings.setdefault(nik, []).append(
                f"{DESTINATIONS[flight_index][0]} to {DESTINATIONS[flight_index][1]} - ${DESTINATIONS[flight_index][2]}"
            )
            or "Flight booked"
            if flight_index in range(len(DESTINATIONS))
            else "Invalid flight selection"
        ),
        "view_history": lambda: bookings.get(nik, []),
        "delete_booking": lambda booking_index: (
            bookings[nik].pop(booking_index, None)
            if nik in bookings and 0 <= booking_index < len(bookings[nik])
            else "Invalid booking selection"
        ),
    }
    return actions.get(action, lambda *_: "Invalid action")(*args)

# Built-in HoF: Add or View Friends
@log_execution
def manage_friends(nik, action, *args):
    actions = {
        "add_friend": lambda friend_nik: (
            friends.setdefault(nik, []).append(friend_nik)
            or "Friend added"
            if friend_nik not in friends.get(nik, [])
            else "Friend already added"
        ),
        "view_friends": lambda: ", ".join(friends.get(nik, [])) or "No friends added",
        "remove_friend": lambda friend_nik: (
            friends[nik].remove(friend_nik)
            if nik in friends and friend_nik in friends[nik]
            else "Friend not found"
        ),
    }
    return actions.get(action, lambda *_: "Invalid action")(*args)

# New Feature: Flight Recommendations (Closure)
def flight_recommendation(min_price):
    def recommend():
        return [
            f"{origin} to {destination} - ${price}"
            for origin, destination, price in DESTINATIONS
            if price >= min_price
        ]
    return recommend

### TESTING ###

# Register accounts
print(handle_accounts("register", "123456", "Arthur", "password123"))
print(handle_accounts("register", "789101", "Natsu", "securepass"))

# Edit Profile
print(handle_accounts("edit_profile", "123456", role="Admin", phone="081234567890"))

# Book a flight
print(manage_bookings("123456", "book_flight", 0))
print(manage_bookings("123456", "view_history"))

# Add and View Friends
print(manage_friends("123456", "add_friend", "789101"))
print(manage_friends("123456", "view_friends"))

# Delete a Friend
print(manage_friends("123456", "remove_friend", "789101"))

# Flight Recommendations
recommend = flight_recommendation(150)
print("Recommended Flights:", recommend())

# Display counter
print("Flights Booked:", increment())
print("Flights Booked:", increment())
print("Total Flights Booked:", get_count())

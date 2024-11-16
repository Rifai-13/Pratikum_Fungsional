from functools import reduce, wraps
from copy import deepcopy

# Constants
DESTINATIONS = [
    ("Jakarta", "Surabaya", 120),
    ("Jakarta", "Bali", 150),
    ("Surabaya", "Medan", 200),
    ("Medan", "Jakarta", 180),
    ("Bali", "Surabaya", 170)
]

# Utility decorator to log function calls
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[INFO] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[INFO] Function {func.__name__} executed successfully.\n")
        return result
    return wrapper

# Closure for tracking logged-in users
def session_manager():
    active_user = None

    def login_user(nik):
        nonlocal active_user
        active_user = nik

    def logout_user():
        nonlocal active_user
        active_user = None

    def get_active_user():
        return active_user

    return login_user, logout_user, get_active_user

login_user, logout_user, get_active_user = session_manager()

# Pure functions
@log_function_call
def register(nik, name, password, accounts):
    accounts_copy = deepcopy(accounts)
    if nik in accounts_copy:
        return accounts_copy, "NIK sudah terdaftar. Coba login."
    new_accounts = {**accounts_copy, nik: {'name': name, 'password': password}}
    return new_accounts, "Registrasi berhasil. Silakan login."

@log_function_call
def login(nik, password, accounts):
    if nik in accounts and accounts[nik]['password'] == password:
        login_user(nik)
        return True, f"Selamat datang, {accounts[nik]['name']}!"
    return False, "NIK atau Password salah."

@log_function_call
def book_flight(flight_choice, bookings):
    active_user = get_active_user()
    if not active_user:
        return bookings, "Silakan login terlebih dahulu untuk memesan tiket."
    
    try:
        flight_choice = int(flight_choice) - 1
        if 0 <= flight_choice < len(DESTINATIONS):
            origin, destination, price = DESTINATIONS[flight_choice]
            bookings_copy = deepcopy(bookings)
            if active_user not in bookings_copy:
                bookings_copy[active_user] = []
            bookings_copy[active_user].append(f"{origin} to {destination} - ${price}")
            return bookings_copy, f"Anda telah memesan: {origin} to {destination} seharga ${price}"
        else:
            return bookings, "Nomor penerbangan tidak valid."
    except ValueError:
        return bookings, "Input tidak valid. Masukkan nomor penerbangan."

@log_function_call
def view_booking_history(bookings):
    active_user = get_active_user()
    if not active_user:
        return "Silakan login terlebih dahulu untuk melihat riwayat pemesanan."

    if active_user in bookings and bookings[active_user]:
        return "\n".join(bookings[active_user])
    return "Tidak ada riwayat pemesanan ditemukan."

@log_function_call
def delete_booking(choice, bookings):
    active_user = get_active_user()
    if not active_user:
        return bookings, "Silakan login terlebih dahulu untuk menghapus pemesanan."
    
    bookings_copy = deepcopy(bookings)
    if active_user in bookings_copy:
        try:
            booking_index = int(choice) - 1
            if 0 <= booking_index < len(bookings_copy[active_user]):
                del bookings_copy[active_user][booking_index]
                return bookings_copy, "Pemesanan berhasil dihapus."
            else:
                return bookings, "Nomor pemesanan tidak valid."
        except ValueError:
            return bookings, "Input tidak valid, masukkan nomor pemesanan."
    return bookings, "Tidak ada riwayat pemesanan ditemukan."

# Higher Order Function (HOF) to calculate total booking costs
@log_function_call
def calculate_total_cost(bookings):
    active_user = get_active_user()
    if not active_user:
        return "Silakan login untuk melihat total biaya pemesanan."
    
    flight_cost = lambda flight: int(flight.split("- $")[-1])
    total_cost = reduce(lambda total, flight: total + flight_cost(flight), bookings.get(active_user, []), 0)
    return total_cost

# Main application
if __name__ == "__main__":
    accounts = {}
    bookings = {}

    while True:
        print("\n=== Sistem Pemesanan Tiket ===")
        print("1. Register")
        print("2. Login")
        print("3. Pesan Tiket")
        print("4. Lihat Riwayat Pemesanan")
        print("5. Hapus Pemesanan")
        print("6. Lihat Total Biaya Pemesanan")
        print("7. Logout")
        print("8. Keluar")
        
        choice = input("Pilih menu: ")

        if choice == "1":
            nik = input("Masukkan NIK: ")
            name = input("Masukkan Nama: ")
            password = input("Masukkan Password: ")
            accounts, message = register(nik, name, password, accounts)
            print(message)

        elif choice == "2":
            nik = input("Masukkan NIK: ")
            password = input("Masukkan Password: ")
            success, message = login(nik, password, accounts)
            print(message)

        elif choice == "3":
            print("\nDaftar Tujuan:")
            for i, (origin, destination, price) in enumerate(DESTINATIONS, start=1):
                print(f"{i}. {origin} -> {destination} (${price})")
            flight_choice = input("Pilih nomor tujuan: ")
            bookings, message = book_flight(flight_choice, bookings)
            print(message)

        elif choice == "4":
            history = view_booking_history(bookings)
            print(history)

        elif choice == "5":
            history = view_booking_history(bookings)
            print(history)
            choice = input("Masukkan nomor pemesanan yang ingin dihapus: ")
            bookings, message = delete_booking(choice, bookings)
            print(message)

        elif choice == "6":
            total_cost = calculate_total_cost(bookings)
            print(f"Total Biaya: {total_cost}")

        elif choice == "7":
            logout_user()
            print("Logout berhasil.")

        elif choice == "8":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

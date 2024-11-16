import getpass
from copy import deepcopy

# Constants
DESTINATIONS = [
    ("Jakarta", "Surabaya", 120),
    ("Jakarta", "Bali", 150),
    ("Surabaya", "Medan", 200),
    ("Medan", "Jakarta", 180),
    ("Bali", "Surabaya", 170)
]

# Pure functions
def register(nik, name, password, accounts):
    accounts_copy = deepcopy(accounts)  # Create a copy of accounts
    if nik in accounts_copy:
        return accounts_copy, "NIK sudah terdaftar. Coba masuk lagi"

    new_accounts = {**accounts_copy, nik: {'name': name, 'password': password}}
    return new_accounts, "Registrasi berhasil. Silakan isi profil Anda."

def login(nik, password, accounts):
    if nik in accounts and accounts[nik]['password'] == password:
        return True, f"Selamat datang, {accounts[nik]['name']}!"
    return False, "NIK atau Password salah."

def fill_profile(nik, role, phone, accounts):
    accounts_copy = deepcopy(accounts)  # Create a copy of accounts
    if nik in accounts_copy:
        accounts_copy[nik].update({'role': role, 'phone': phone})
        return accounts_copy, "Profil berhasil diisi."
    return accounts_copy, "Profil tidak ditemukan."

def view_profile(nik, accounts):
    profile = accounts.get(nik)
    if profile:
        return f"Name: {profile['name']}, Role: {profile.get('role', 'Not set')}, Phone: {profile.get('phone', 'Not set')}"
    return "Profil tidak ditemukan."

def edit_profile(nik, name, role, phone, accounts):
    accounts_copy = deepcopy(accounts)  # Create a copy of accounts
    if nik in accounts_copy:
        accounts_copy[nik].update({'name': name, 'role': role, 'phone': phone})
        return accounts_copy, "Profil telah diperbarui."
    return accounts_copy, "Profil tidak ditemukan."

def delete_profile(nik, accounts):
    accounts_copy = deepcopy(accounts)  # Create a copy of accounts
    if nik in accounts_copy:
        del accounts_copy[nik]
        return accounts_copy, "Profil telah dihapus."
    return accounts_copy, "Profil tidak ditemukan."

def book_flight(nik, flight_choice, bookings):
    flight_choice = int(flight_choice) - 1  # Convert choice to integer

    if 0 <= flight_choice < len(DESTINATIONS):
        origin, destination, price = DESTINATIONS[flight_choice]
        bookings_copy = deepcopy(bookings)  # Create a copy of bookings
        if nik not in bookings_copy:
            bookings_copy[nik] = []
        bookings_copy[nik].append(f"{origin} to {destination} - ${price}")
        return bookings_copy, f"You have booked: {origin} to {destination} for ${price}"
    else:
        return bookings, "Invalid flight number."

def view_booking_history(nik, bookings):
    if nik in bookings and bookings[nik]:
        return "\n".join(bookings[nik])
    return "No bookings found."

def delete_booking(nik, choice, bookings):
    bookings_copy = deepcopy(bookings)  # Create a copy of bookings
    if nik in bookings_copy:
        try:
            booking_index = int(choice) - 1
            if 0 <= booking_index < len(bookings_copy[nik]):
                del bookings_copy[nik][booking_index]
                return bookings_copy, "Booking deleted successfully."
            else:
                return bookings, "Invalid booking number."
        except ValueError:
            return bookings, "Invalid input, please enter a number."
    
    return bookings, "No bookings found to delete."

def add_friend(nik, friend_nik, friends):
    friends_copy = deepcopy(friends)  # Create a copy of friends
    if nik not in friends_copy:
        friends_copy[nik] = []
        
    if friend_nik in friends_copy[nik]:
        return friends_copy, "Teman sudah ditambahkan."

    friends_copy[nik].append(friend_nik)
    return friends_copy, "Teman berhasil ditambahkan."

def delete_friend(nik, friend_nik, friends):
    friends_copy = deepcopy(friends)  # Create a copy of friends
    if nik in friends_copy and friend_nik in friends_copy[nik]:
        friends_copy[nik].remove(friend_nik)
        return friends_copy, "Teman berhasil dihapus."
    return friends_copy, "Teman tidak ditemukan."

def view_friends(nik, friends):
    if nik in friends and friends[nik]:
        return "\n".join(friends[nik])
    return "Tidak ada teman yang ditambahkan."

def user_menu(nik):
    options = [
        "View Profile",
        "Edit Profile",
        "Book Flight",
        "View Booking History",
        "Delete Booking",
        "Delete Profile",
        "Add Friend",
        "Delete Friend",
        "View Friends",
        "Logout"
    ]
    return options

def main():
    # Global data
    accounts = {}
    bookings = {}
    friends = {}  # Inisialisasi data teman

    while True:
        print("\n-- Menu Utama --")
        print("1. Daftar")
        print("2. Masuk")
        print("3. Keluar")

        choice = input("Pilih opsi: ")

        if choice == '1':
            nik = input("Masukkan NIK: ")
            name = input("Masukkan Nama: ")
            password = getpass.getpass("Masukkan Password: ")
            accounts, message = register(nik, name, password, accounts)
            print(message)

            if "berhasil" in message:
                role = input("Masukkan Role: ")
                phone = input("Masukkan Nomor Telepon: ")
                accounts, profile_message = fill_profile(nik, role, phone, accounts)
                print(profile_message)

        elif choice == '2':
            nik = input("Masukkan NIK: ")
            password = getpass.getpass("Masukkan Password: ")

            success, message = login(nik, password, accounts)
            print(message)

            if success:
                while True:
                    user_options = user_menu(nik)
                    print("\n-- User Menu --")
                    for index, option in enumerate(user_options, start=1):
                        print(f"{index}. {option}")
                    
                    user_choice = input("Pilih opsi: ")
                    if user_choice == '1':
                        profile_message = view_profile(nik, accounts)
                        print(profile_message)

                    elif user_choice == '2':
                        name = input("Masukkan Nama baru: ")
                        role = input("Masukkan Role baru: ")
                        phone = input("Masukkan Nomor Telepon baru: ")
                        accounts, message = edit_profile(nik, name, role, phone, accounts)
                        print(message)

                    elif user_choice == '3':
                        print("\n-- Daftar Penerbangan --")
                        for index, (origin, destination, price) in enumerate(DESTINATIONS, start=1):
                            print(f"{index}. {origin} to {destination} - ${price}")
                        flight_choice = input("Masukkan nomor penerbangan atau 'cancel': ")
                        if flight_choice.lower() == 'cancel':
                            continue
                        bookings, message = book_flight(nik, flight_choice, bookings)
                        print(message)

                    elif user_choice == '4':
                        history_message = view_booking_history(nik, bookings)
                        print(history_message)

                    elif user_choice == '5':
                        print("Bookings:")
                        for index, booking in enumerate(bookings.get(nik, []), start=1):
                            print(f"{index}. {booking}")
                        booking_choice = input("Masukkan nomor booking untuk dihapus (atau ketik 'cancel' untuk membatalkan): ")
                        if booking_choice.lower() == 'cancel':
                            continue
                        bookings, message = delete_booking(nik, booking_choice, bookings)
                        print(message)

                    elif user_choice == '6':
                        accounts, message = delete_profile(nik, accounts)
                        print(message)
                        break

                    elif user_choice == '7':
                        friend_nik = input("Masukkan NIK teman yang ingin ditambahkan: ")
                        friends, message = add_friend(nik, friend_nik, friends)
                        print(message)

                    elif user_choice == '8':
                        friend_nik = input("Masukkan NIK teman yang ingin dihapus: ")
                        friends, message = delete_friend(nik, friend_nik, friends)
                        print(message)

                    elif user_choice == '9':
                        friends_message = view_friends(nik, friends)
                        print(friends_message)

                    elif user_choice == '10':
                        print("Logout successful.")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Terima kasih! Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()

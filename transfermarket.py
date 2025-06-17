from tabulate import tabulate
import sys

player_list = {
    'players_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'name': ['Florian Wirtz', 'Dean Huijsen', 'Matheus Cunha', 'Viktor Gyokeres', 'Tijjani Reijnders',
             'Marcus Rashford', 'Darwin Nunez', 'Kim Min Jae', 'Rafael Leao', 'Mike Maignan',
             'Rayan Cherki', 'Joan Garcia', 'Theo Hernandez', 'Kingsley Coman'],
    'age': [22, 20, 26, 27, 26, 27, 25, 28, 25, 29, 21, 24, 27, 28],
    'position': ['Gelandang', 'Bek', 'Penyerang', 'Penyerang', 'Gelandang', 'Penyerang', 'Penyerang',
                 'Bek', 'Penyerang', 'Kiper', 'Gelandang', 'Kiper', 'Bek', 'Penyerang'],
    'price': [140000000, 60000000, 60000000, 75000000, 50000000, 50000000, 45000000, 40000000,
              75000000, 25000000, 45000000, 20000000, 40000000, 30000000],
    'contract_expire': [2027, 2030, 2029, 2028, 2030, 2028, 2028, 2028, 2028, 2026, 2026, 2028, 2026, 2027],
    'club': ['Bayer Leverkusen', 'Bournemouth', 'Wolves', 'Sporting CP', 'AC Milan', 'Manchester United',
             'Liverpool', 'Bayern Munich', 'AC Milan', 'AC Milan', 'Lyon', 'Espanyol', 'AC Milan', 'Bayern Munich'],
    'country': ['Jerman', 'Spanyol', 'Brasil', 'Swedia', 'Belanda', 'Inggris', 'Uruguay', 'Korea Selatan',
                'Portugal', 'Prancis', 'Prancis', 'Spanyol', 'Prancis', 'Prancis'] #daftar pemain
}

account = {
    'admin': {'username': 'admin', 'password': 'admin123'},
    'guest': {'username': 'guest', 'password': 'guest123'}
} #list akun

recycle_bin = [] #inisiasi recycle bin

#fitur login admin dan guest
def login():
    print("\n--- Login ---")
    while True:
        username = input("\nUsername: ")
        password = input("\nPassword: ")
        for acc, val in account.items():
            if username == val['username'] and password == val['password']:
                print(f"\nBerhasil login sebagai {acc.upper()}")
                return acc
        print("\nUsername atau password salah. Coba lagi.")

#fitur tampilkan pemain
def show_player():
    print("\n--- Tampilkan Pemain ---")
    print("\nDaftar Pemain Tersedia:")
    data = []
    for i in range(len(player_list['name'])):
        data.append([
            player_list['players_id'][i],
            player_list['name'][i],
            player_list['age'][i],
            player_list['position'][i],
            player_list['price'][i],
            player_list['contract_expire'][i],
            player_list['club'][i],
            player_list['country'][i]
        ])
    print(tabulate(data, headers=['ID', 'Nama', 'Umur', 'Posisi', 'Harga (€)', 'Akhir Kontrak', 'Klub', 'Negara'], tablefmt='grid'))

#fitur tambahkan pemain
def add_player():
    print("\n--- Tambah Pemain ---")
    name = input("\nNama Pemain: ")
    try:
        age = int(input("\nUmur Pemain: "))
        price = int(input("\nHarga Pemain (€): "))
        contract = int(input("\nTahun Kontrak Berakhir: "))
    #memastikan input umur, harga, dan kontrak itu numerik
    except ValueError:
        print("\nUmur, harga, dan tahun kontrak harus berupa angka.")
        return

    position = input("\nPosisi Pemain: ")
    club = input("\nKlub Pemain: ")
    country = input("\nNegara Pemain: ")

    #konfirmasi tambah
    confirmation = input(f"\nYakin ingin menambahkan pemain {name}? (y/n): ").lower()
    if confirmation == 'y':
        new_id = max(player_list['players_id']) + 1
        player_list['players_id'].append(new_id)
        player_list['name'].append(name)
        player_list['age'].append(age)
        player_list['position'].append(position)
        player_list['price'].append(price)
        player_list['contract_expire'].append(contract)
        player_list['club'].append(club)
        player_list['country'].append(country)
        print(f"\nPemain {name} berhasil ditambahkan.\n")
    else:
        print("\nPenambahan pemain dibatalkan.")
    show_player()

#fitur edit pemain
def update_player():
    show_player()
    print("\n--- Update Pemain ---")
    try:
        index = int(input("\nMasukkan ID pemain yang ingin diupdate: "))
    #memastikan ID harus angka
    except ValueError:
        print("\nInput harus berupa angka.")
        return

    if index in player_list['players_id']:
        i = player_list['players_id'].index(index)
        print("\nMasukkan data baru (tekan Enter untuk skip):")

        #user input untuk merubah data pemain
        name = input(f"Nama [{player_list['name'][i]}]: ") or player_list['name'][i]
        age_input = input(f"Umur [{player_list['age'][i]}]: ")
        price_input = input(f"Harga (€) [{player_list['price'][i]}]: ")
        contract_input = input(f"Kontrak Berakhir [{player_list['contract_expire'][i]}]: ")

        try:
            age = int(age_input) if age_input else player_list['age'][i]
            price = int(price_input) if price_input else player_list['price'][i]
            contract = int(contract_input) if contract_input else player_list['contract_expire'][i]
        except ValueError:
            print("\nUmur, harga, dan kontrak harus berupa angka.")
            return

        position = input(f"Posisi [{player_list['position'][i]}]: ") or player_list['position'][i]
        club = input(f"Klub [{player_list['club'][i]}]: ") or player_list['club'][i]
        country = input(f"Negara [{player_list['country'][i]}]: ") or player_list['country'][i]

        #konfirmasi update
        confirmation = input(f"\nYakin ingin mengupdate pemain? (y/n): ").lower()
        if confirmation == 'y':
            player_list['name'][i] = name
            player_list['age'][i] = age
            player_list['position'][i] = position
            player_list['price'][i] = price
            player_list['contract_expire'][i] = contract
            player_list['club'][i] = club
            player_list['country'][i] = country
            print("\nPemain berhasil diupdate.")
        else:
            print("\nPengupdate-an dibatalkan.")
            return
    else:
        print("\nID tidak ditemukan.")

#fitur hapus pemain
def delete_player():
    show_player()
    print("\n--- Hapus Pemain ---")
    try:
        index = int(input("\nMasukkan ID pemain yang ingin dihapus: "))
    except ValueError:
        print("\nInput harus berupa angka.")
        return

    if index in player_list['players_id']:
        i = player_list['players_id'].index(index)
        name = player_list['name'][i]

        #konfirmasi hapus
        confirmation = input(f"\nApakah Anda yakin ingin menghapus pemain? (y/n): ").lower()
        if confirmation != 'y':
            print("\nPenghapusan dibatalkan.")
            return

        #memasukkan pemain yang dihapus ke dalam recycle bin
        deleted = {player: player_list[player][i] for player in player_list}
        recycle_bin.append(deleted)
        for k in player_list:
            del player_list[k][i]
        print(f"\nPemain {deleted['name']} berhasil dihapus dan dimasukkan ke recycle bin.")
    else:
        print("\nID tidak ditemukan.")

#fitur cari pemain
def search_player():
    print("\n--- Cari Pemain ---")
    search_position = input("\nPosisi Pemain: ")
    try:
        search_price = int(input("\nHarga maksimum (€): "))
    except ValueError:
        print("\nHarga harus berupa angka.")
        return

    search_result = [] #untuk menyimpan data yang dicari
    for i in range(len(player_list['name'])):
        if player_list['position'][i].lower() == search_position.lower() and player_list['price'][i] <= search_price:
            search_result.append([
                player_list['players_id'][i],
                player_list['name'][i],
                player_list['age'][i],
                player_list['position'][i],
                player_list['price'][i],
                player_list['contract_expire'][i],
                player_list['club'][i],
                player_list['country'][i]
            ])
    if search_result:
        print("\nHasil Pencarian:")
        print(tabulate(search_result, headers=['ID', 'Nama', 'Umur', 'Posisi', 'Harga (€)', 'Akhir Kontrak', 'Klub', 'Negara'], tablefmt='grid'))
    else:
        print("\nTidak ada pemain yang cocok.")

#fitur beli pemain
def buy_player():
    show_player()
    print("\n--- Beli Pemain ---")
    try:
        index = int(input("\nMasukkan ID pemain yang ingin dibeli: ")) - 1
    except ValueError:
        print("\nInput harus berupa angka.")
        return

    if 0 <= index < len(player_list['name']):
        name = player_list['name'][index]
        price = int(player_list['price'][index])

        #menginput tawaran transfer untuk klub asal pemain
        print(f"\nHarga transfer resmi untuk {name} adalah €{price}")
        try:
            transfer_offer = int(input(f"\nMasukkan tawaran harga ke klub asal untuk {name}: €"))
        except ValueError:
            print("\nTawaran harus berupa angka.")
            return
        
         #konfirmasi beli
        confirmation = input(f"\nApakah Anda yakin ingin menawar {name} dengan harga €{transfer_offer}? (y/n): ").lower()
        if confirmation != 'y':
            print("\nPenawaran dibatalkan.")
            return

        if transfer_offer >= (price * 0.8): #membatasi harga yang ditawar
            print("\nTawaran diterima oleh klub asal. Mohon tunggu respon dari klub.")
        else:
            print("\nTawaran ditolak oleh klub. Harga yang ditawar minimal 80%.")
            return

#fitur recycle bin
def show_recycle_bin():
    print("\n--- Recycle Bin ---")
    if not recycle_bin:
        print("\nRecycle bin kosong.")
        return
    data_bin = [] #inisiasi untuk menyimpan pemain yang dihapus
    for item in recycle_bin:
        data_bin.append([
            item['players_id'],
            item['name'],
            item['age'],
            item['position'],
            item['price'],
            item['contract_expire'],
            item['club'],
            item['country']
        ])
    print(tabulate(data_bin, headers=['ID', 'Nama', 'Umur', 'Posisi', 'Harga (€)', 'Akhir Kontrak', 'Klub', 'Negara'], tablefmt='grid'))

    #fitur untuk mengembalikan pemain yang sudah dihapus
    restore = input("\nIngin restore pemain? (y/n): ").lower()
    if restore == 'y':
        try:
            id_restore = int(input("\nMasukkan ID pemain yang ingin direstore: "))
        except ValueError:
            print("\nID harus berupa angka.")
            return
        
        #konfirmasi restore
        confirmation = input(f"\nApakah Anda yakin ingin restore pemain? (y/n): ").lower()
        if confirmation != 'y':
            print("\nRestore dibatalkan.")
            return
        
        for item in recycle_bin:
            if item['players_id'] == id_restore:
                for key in player_list:
                    player_list[key].append(item[key])
                recycle_bin.remove(item)
                print("\nPemain berhasil direstore.")
                return
        print("\nID tidak ditemukan di recycle bin.")

def exit():
    #konfirmasi keluar
        confirmation = input(f"\nApakah Anda yakin ingin keluar program? (y/n): ").lower()
        if confirmation == 'y':
            print("Terima kasih telah menggunakan program!")
            sys.exit()
        else:
            print("Proses keluar dibatalkan")
            return

#menu utama
def main():
    acc = login() 
    while True: #untuk menampilkan terus menerus
        print("\n--- Transfer Market Liga Eropa ---")
        print("\nMenu:")
        print("1. Lihat Daftar Pemain")
        print("2. Cari Pemain") #fitur 1 dan 2 bisa diakses semua user
        if acc == 'admin': 
            print("3. Tambah Pemain")
            print("4. Update Pemain")
            print("5. Hapus Pemain")
            print("6. Beli Pemain")
            print("7. Recycle Bin") #tambah, update, hapus, beli, dan recycle bin hanya bisa diakses admin
            print("8. Keluar")
        else:
            print("3. Keluar") #menu "keluar" untuk guest dinaikkan menjadi no 3

        option = input("\nPilih menu: ")
        try:
            option = int(option)
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if acc == 'admin':
            if option == 1:
                show_player()
            elif option == 2:
                search_player()
            elif option == 3:
                add_player()
            elif option == 4:
                update_player()
            elif option == 5:
                delete_player()
            elif option == 6:
                buy_player()
            elif option == 7:
                show_recycle_bin()
            elif option == 8:
                exit()
            else:
                print("Pilihan tidak valid.")
        else:
            if option == 1:
                show_player()
            elif option == 2:
                search_player()
            elif option == 3:
                exit()
                break
            else:
                print("Pilihan tidak valid.")

main() #awal program

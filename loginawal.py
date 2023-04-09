import pwinput

def lihat():
    try:
        file = open("user.txt", "r")
    except FileNotFoundError:
        return []
    user = []
    for line in file:
        user.append(line.strip())
    file.close()
    return user

def cek_akun(nama, username, password):
    for akun in username :
        if nama in akun and username in akun and password in akun:
            return True
    return False

def registrasi(nama, username, password):
    user = lihat()
    if not cek_akun(nama, username, password):
        user.append(f"{nama} : {username} : {password}")
        file = open("user.txt", "w")
        for akun in user:
            file.write(akun + "\n")
        file.close()
        print("Pengguna berhasil ditambahkan.")
    else:
        print("Pengguna sudah terdaftar.")

def proses():
    nama = input("Masukkan Nama Anda : ")
    username = input("Masukkan Username Anda : ")
    password = pwinput.pwinput(prompt="Masukkan Password : ")
    return nama, username, password

def main():
    while True:
        print("="*45)
        print("="*45)
        print("\t1. Login")
        print("\t2. Registrasi Akun")
        print("\t3. Exit")
        print("="*45)
        pilih = int(input("Halo, ingin ke menu apa? "))
        print("")

        if pilih == 1:
            nama, username, password = proses()
            user = lihat()
            for akun in user:
                if nama in akun and username in akun and password in akun:
                    print("Anda berhasil login.")
                    break
                else:
                    print("Data pengguna tidak ditemukan. Silakan coba lagi.")            
                    print("")
        elif pilih == 2:
            nama, username, password = proses()
            registrasi(nama, username, password)
            print("")
        elif pilih == 3:
            print(" Terima Kasih ^___^ ".center(45,"-"))
            print("")
            break
        else:
            print("")
            print("Invalid")
            raise SystemExit
        
main()
import os
import pwinput
import json

admin = {"username" : ["novan", "lisya", "faiz"],
         "password" : ["admin1", "admin2", "admin3"]}

file_json = open("dataUser.json")
data_1 = json.loads(file_json.read())
def settingUser():
	with open("dataUser.json", "w") as dataBaru:
		json.dump(data_1, dataBaru)
		
def login_user():
    while True:
        username = input("Silahkan Masukkan Username Anda : ")
        password = pwinput.pwinput ("Silahkan Masukkan Password Anda : ")
        if password.isnumeric:
            try:
                login = data_1["username"].index(username)
                if username == data_1["username"][login] and password == data_1["password"][login]:
                    os.system('cls')
                    break
                else:
                    print("\n <<< Password Anda Salah >>> \nSilahkan Coba Kembali\n")
            except ValueError:
                print("\n<<< Username Anda Salah>>> \nSilahkan Coba Kembali\n")

def tambah_user():
    while True:
        try:
            username = input("Masukkan Username Baru Anda : ")
            if username.isalnum()==False:
                print("<<< Username tidak boleh ada spasi, simbol dan kosong >>>")
            elif username in data_1["username"]:
                print("<<< Username telah digunakan >>>")
            elif username not in data_1["username"]:
                password=str(pwinput.pwinput("Masukkan password : ")).replace("\t","").replace(" ","")
                if password =="":
                    print("!!! Password dilarang kosong dan menggunakan spasi !!! ")
                else:
                    data_1["username"].append(username)
                    data_1["password"].append(password)
                    os.system('cls')
                    print("Registrasi berhasil ^____^")
                    settingUser()
                    break
        except ValueError:
            print ("<<< Dilarang memasukkan data kosong !!! >>>")

def login_admin():
        while True:
            username = input("Silahkan Masukkan Username Anda : ")
            password = pwinput.pwinput ("Silahkan Masukkan Password Anda : ")
            try:
                login = admin.get("username").index(username)
                if username == admin.get("username")[login] and password == admin.get("password")[login]:
                    os.system('cls')
                    break
                else:
                    print("\n <<< Password Anda Salah >>> \nSilahkan Coba Kembali\n")
            except ValueError:
                print("\n <<< Username Anda Salah >>> \nSilahkan Coba Kembali\n")
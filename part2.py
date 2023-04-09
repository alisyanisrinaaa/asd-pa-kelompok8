from prettytable import PrettyTable
import datetime
from loginn import *

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.next = None
        self.created_at = datetime.datetime.now()
        self.deleted_at = None

class ToDoList:
    def __init__(self):
        self.head = None
        self.history = []
    
    def add_task(self, description):
        task = Task(description)
        if self.head is None:
            self.head = task
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = task
        self.history.append(('Menambahkan', task.description, task.created_at))
    
    def remove_task(self, description):
        current = self.head
        previous = None
        while current is not None:
            if current.description == description:
                current.deleted_at = datetime.datetime.now()
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.history.append(('Menghapus', current.description, current.deleted_at))
                return True
            previous = current
            current = current.next
        print("<<< To Do List Masih Kosong / To Do List Tidak Ada >>>")
        return os.system("pause")
    
    def complete_task(self, description):
        current = self.head
        while current is not None:
            if current.description == description:
                current.completed = True
                return True
            current = current.next
        print("<<< To Do List Masih Kosong >>>")
        return os.system("pause")
    
    def display_list(self):
        current = self.head
        while current is not None:
            if current.completed:
                print("[x]", current.description)
            else:
                print("[ ]", current.description)
            current = current.next

    def show_history(self):
        if self.history == []:
            print("Tidak Ada History")
        else:
            table = PrettyTable()
            table.field_names = ["Keterangan","To Do List","Waktu"]
            for i in self.history:
                table.add_row(i)
            print(table)

    def jump_search_task(self, description):
        # Sorting tasks by description
        tasks = self.sort_tasks()
        
        # Applying jump search algorithm
        n = len(tasks)
        jump = int(n**0.5)
        left = 0
        right = 0
        
        while right < n and tasks[right].description < description:
            left = right
            right = min(right+jump, n-1)
        
        for i in range(left, right+1):
            if tasks[i].description == description:
                return tasks[i]
        return None
    
    def sort_tasks(self):
        tasks = []
        current = self.head
        while current is not None:
            tasks.append(current)
            current = current.next
        tasks.sort(key=lambda task: task.description)
        return tasks
    

    def sort(self):
        sudah = []
        belum = []
        current = self.head
        while current is not None:
            if current.completed == True:
                sudah.append((current.description))
            elif current.completed == False:
                belum.append((current.description))
            current = current.next   
        return sudah + belum
    
    def mergesortasc(self,data):
        if len(data) > 1:
            mid = len(data) // 2
            left_data = data[:mid]
            right_data = data[mid:]

            self.mergesortasc(left_data)
            self.mergesortasc(right_data)

            i = j = k=0
            
            while i < len(left_data) and j < len (right_data):
                if left_data[i] < right_data[j]:
                    data[k]= left_data[i]
                    i += 1
                    k += 1

                else:
                    data[k] = right_data[j]
                    j += 1
                    k += 1

            while i < len(left_data):
                data[k] = left_data[i]
                i += 1
                k += 1

            
            while j < len(right_data):
                data[k] = right_data[j]
                j += 1
                k += 1
        return data
    
    def mergesortdesc(self,data):
        if len(data) > 1:
            mid = len(data) // 2
            left_data = data[:mid]
            right_data = data[mid:]

            self.mergesortdesc(left_data)
            self.mergesortdesc(right_data)

            i = j = k=0
            
            while i < len(left_data) and j < len (right_data):
                if left_data[i] > right_data[j]:
                    data[k]= left_data[i]
                    i += 1
                    k += 1

                else:
                    data[k] = right_data[j]
                    j += 1
                    k += 1

            while i < len(left_data):
                data[k] = left_data[i]
                i += 1
                k += 1

            
            while j < len(right_data):
                data[k] = right_data[j]
                j += 1
                k += 1
        return data
    
    def tampilansort(self,hasil):
        no = 1
        table = PrettyTable(["urutan","To do list"])
        for i in range(len(hasil)):
            table.add_row([no,hasil[i]])
            no +=1
        print(table)
        
    
    def aluruser(self):
        while True:
            os.system("cls")
            print(50*"=")
            print("1. Tambahkan To Do List")
            print("2. Hapus To Do List ")
            print("3. Tandai To Do List yang Selesai")
            print("4. Tampilkan To Do List")
            print("5. Cari To Do List")
            print("6. Mengurutkan To Do List sesuai Abjad ")
            print("7. Exit")
            print(50*"=")
            pilihan = int(input("Masukkan pilihan anda : "))
            if pilihan == 1:
                tdl = input("Masukkan to do list terbaru : ")
                self.add_task(tdl)
                os.system("cls")
            elif pilihan == 2:
                hapus = input("Masukkan to do list yang ingin dihapus : ")
                self.remove_task(hapus)
                os.system("cls")
            elif pilihan == 3:
                tanda = input("Masukkan to do list yang sudah selesai : ")
                self.complete_task(tanda)
                os.system("cls")
            elif pilihan == 4:
                self.display_list()
                os.system("pause")
                os.system("cls")
            elif pilihan == 5:
                tdl = input("Masukkan to do list yang ingin dicari : ")
                task = self.jump_search_task(tdl)
                if task is not None:
                    table = PrettyTable(['Description', 'Completed', 'Created At'])
                    table.add_row([task.description, task.completed, task.created_at])
                    print(table)
                else:
                    print(f"Task dengan description '{tdl}' tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
                os.system("cls")
            elif pilihan == 6:
                pilah = self.sort()
                print("1. Ascending\n2. Descending")
                x = input("Masukkan pilihan (1/2) : ")
                if x =='1':
                    hasil = self.mergesortasc(pilah)
                    self.tampilansort(hasil)
                    os.system("pause")
                elif x == '2':
                    hasil = self.mergesortdesc(pilah)
                    self.tampilansort(hasil)
                    os.system("pause")
                else:
                    print("Masukkan pilihan yang tersedia")
            else:
                os.system("cls")
                break

    def aluradmin(self):
        while True:
            os.system("cls")
            print(50*"=")
            print("1. Tambahkan To Do List")
            print("2. Hapus To Do List ")
            print("3. Tandai To Do List yang Selesai")
            print("4. Tampilkan To Do List")
            print("5. Tampilkan History Input dan Delete Data")
            print("6. Cari To Do List")
            print("7. Mengurutkan To Do List sesuai Abjad ")
            print("8. Exit")
            print(50*"=")
            pilihan = int(input("Masukkan pilihan anda : "))
            if pilihan == 1:
                tdl = input("Masukkan to do list terbaru : ")
                self.add_task(tdl)
                os.system("cls")
            elif pilihan == 2:
                hapus = input("Masukkan to do list yang ingin dihapus : ")
                self.remove_task(hapus)
                os.system("cls")
            elif pilihan == 3:
                tanda = input("Masukkan to do list yang sudah selesai : ")
                self.complete_task(tanda)
                os.system("cls")
            elif pilihan == 4:
                self.display_list()
                os.system("pause")
                os.system("cls")
            elif pilihan == 5:
                self.show_history()
                os.system("pause")
                os.system("cls")
            elif pilihan == 6:
                tdl = input("Masukkan to do list yang ingin dicari : ")
                task = self.jump_search_task(tdl)
                if task is not None:
                    table = PrettyTable(['Description', 'Completed', 'Created At'])
                    table.add_row([task.description, task.completed, task.created_at])
                    print(table)
                else:
                    print(f"Task dengan description '{tdl}' tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
                os.system("cls")
            elif pilihan == 7:
                pilah = self.sort()
                print("1. Ascending\n2. Descending")
                x = input("Masukkan pilihan (1/2) : ")
                if x == '1':
                    hasil = self.mergesortasc(pilah)
                    self.tampilansort(hasil)
                    os.system("pause")
                elif x == '2':
                    hasil = self.mergesortdesc(pilah)
                    self.tampilansort(hasil)
                    os.system("pause")
                else:
                    print("Masukkan pilihan yang tersedia")
            else:
                os.system("cls")
                break
    
    def mulai(self):
        global tdl
        os.system("cls")
        while True:
            print("Selamat datang di program pembuatan to do list\nSilahkan login terlebih dahulu")
            print("1. Login Admin\n2. Login User\n3. Register User\nPRESS ANYTHING FOR EXIT")
            x = input("Masukkan Pilihan Anda : ")
            if x == '1':
                login_admin()
                self.aluradmin()
            elif x == '2':
                login_user()
                self.aluruser()
            elif x == '3':
                tambah_user()
            else:
                break

            
import os
kaka = ToDoList()
kaka.mulai()

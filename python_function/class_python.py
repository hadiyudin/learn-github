# class Customer:
#     """_summary_
#     function didalam class = method
#     method parameternya harus diawali dengan self
#     self: method ini punyanya class customer
#     """
#     def identity(self, new_name):
#         self.name = new_name
#         print("Customer adalah",new_name) 

# customer1 = Customer()
# customer1.identity("angga")
# # print(customer1.name)



# Constructor __init__
# class Customer:
#     def __init__(self, name):
#         self.name = name
#         print("Siapa yang sedang mencoba init?")

# customer1 = Customer("Yudi")
# print(customer1.name)


# class
# class mahasiswa():
#     nama = 'nama'

#     def belajar(self, kondisi):
#         print(self.nama, "sedang belajar", kondisi)

#     def tidur(self):
#         print(self.nama, "tidur dikelas")



# # main programnya

# otong = mahasiswa()
# ucup = mahasiswa()

# otong.nama = "otong suratong"
# ucup.nama = "ucup markucup"

# otong.belajar("matematika")
# ucup.tidur()


# menggunakan init di class

class mahasiswa():
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim
        print(self.nama)
        print(self.nim)

    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)

    def tidur(self):
        print(self.nama, "tidur dikelas")



# main programnya

otong = mahasiswa("otong suratong", 13317001)
otong.nama = 'atang suratang'
print(otong.nama)
otong.belajar("matematika")



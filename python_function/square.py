# user defined function
# mengambil 1 parameter
# def square(val:int):
#     """
#     Pangkat 2 operation
#     """
#     new_value = val ** 2
#     print(new_value)
#     # return new_value

# hasil = square(10)
# print(hasil)

# 2 parameters function
# def perkalian(angka1:int, angka2:int):
#     """fungsi yang berguna untuk perkalian

#     Args:
#         angka1 (Integer): _description_
#         angka2 (Integer): _description_

#     Returns:
#         Integer: hasil perkalian
#     """
#     new_value = angka1 * angka2
#     return new_value

# hasil = perkalian(2,2)
# print(hasil)

#Return multiple values
# def return_multiple(angka1:int, angka2:int):
#     """
#     Fungsi yang mengembalikan 2 value
#     """
#     perkalian = angka1 * angka2
#     penambahan = angka1 + angka2

#     # multiple_value = (perkalian, penambahan)

#     return perkalian, penambahan

# hasil = return_multiple(3,2)
# print(hasil)

# def loop1(value):
#     for i in value:
#         print(i)
    
# hasil = loop1([1,2,3])


#Parameter, *args, **kwargs
# def greet(*names):
#     for name in names:
#         print(f'Hello {name}')

# greet('Angga','Budi','Susi')



def greet(**kwargs):
    print('Hello', kwargs['first_name'], kwargs['last_name'])

greet(first_name='Mohamad', last_name='Hadiyudin')
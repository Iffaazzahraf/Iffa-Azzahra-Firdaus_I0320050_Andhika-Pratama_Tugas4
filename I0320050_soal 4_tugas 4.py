
#untuk mendaftar kursus online siswa harus berusia minimal 21 tahun dan sudah lulus ujian kualifikasi
print("untuk dapat mendaftar di kursus ini, kamu harus berusia minimal 21 tahun dan sudah lulus ujian kualifikasi")
print("untuk itu, silahkan menjawab beberapa pertanyaan agar kami dapat menentukan apakah kamu bisa mendaftar")
#usia
usia=int(input("berapa usia kamu?"))
print(usia>=21)
#kelulusan ujian
ujian=str(input("apakah kamu sudah lulus ujian kualifikasi?(ya/tidak)"))
print(ujian=="ya")



if usia>=21 and ujian=="ya":
    print("Anda dapat mendaftar di kursus!!!")
    print(True)


else:
    print("Anda tidak dapat mendaftar di kursus!!!")
    print(False)







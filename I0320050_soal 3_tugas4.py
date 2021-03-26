print("maksimal berat barang bawaan adalah 50 lbs setara 22.7 kg")
#berat maksimal adalah 50lbs = 22.7 kg
b= float(input("berapa berat bawaan Anda dalam kg?"))
print(b<=22.7)
if b<=22.7:
    print('berat barang bawaan Anda memenuhi syarat')
else:
    print('berat barang bawaan Anda melebihi kapasitas, Anda dapat mengurangi atau membayar sejumlah bagasi')

#apa yang terjadi jika berat lebih dari 110 kg
b=float(input("apa yang terjadi jika beratnya lebih dari 110 kg? masukkan berat lebih dari 110 kg!"))
print(b<=22.7)
print('berat barang bawaan Anda melebihi kapasitas, Anda dapat mengurangi atau membayar sejumlah bagasi')


#apa yang terjadi jika beratnya 49 kg?
print("bagaimana jika berat bawaan 49 kg?")
b= 49
print(b<=22.7)
print('berat barang bawaan Anda melebihi kapasitas, Anda dapat mengurangi atau membayar sejumlah bagasi')





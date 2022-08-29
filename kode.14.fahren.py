# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput Satuan suhu
fahrenheit = float(input("Tuliskan Suhu fahrenheit: "))

# Mengkonversi
celcius= (fahrenheit - 32)* 0.556

# Menampilkan Hasil 
print('%0.2f derajat fahrenheit sama dengan %0.2f derajat celcius' %(fahrenheit,celcius))

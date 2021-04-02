nama = input('Masukan nama anda ')
jenis = input('Masukan jenis kelamin ')

if jenis == "laki-laki":
    panggilan = "Tuan"
elif jenis == "perempuan":
    panggilan = "Nyonya"
else:
    pass

print('Selamat datang,',panggilan,nama)
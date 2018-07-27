# untuk mengubah nama file
import os

print "membuat file baru=================================================="
try:
	sebuah_file = open("absen.txt",'w')
	print "nama file yang tadi dibuat :", sebuah_file.name
	print "mode pembacaan file:", sebuah_file.mode
	print "apakah filenya udah ditutup ? :",sebuah_file.closed
	sebuah_file.close()
	print "apakah filenya udah ditutup ? :",sebuah_file.closed
except IOError, e:
	print "proses gagal karena :",e


print "\n\n"
print "mengisi file=================================================="
try:
	sebuah_file = open("absen.txt",'w')
	print "nama file yang tadi dibuat :",sebuah_file.name
	print "mode pembacaan file :", sebuah_file.mode
	print "apakah filenya udah ditutup ? :", sebuah_file.closed
	sebuah_file.write('1.pesawat terbang, teknik mesin, ITD\n')
	sebuah_file.write('2.hacking wifi, teknik informatika, UNK\n')
	sebuah_file.write('3.electronika , teknik elektronika, PIP\n')
	sebuah_file.close()
	print "apakah filennya udah ditutup ? :",sebuah_file.closed
except IOError , e:
	print "gagal karena :", e

print "\n\n"
print "membaca isi file======================================================"
try:
	sebuah_file = open("absen.txt",'r')
	print "nama file yang tadi dibuat :",sebuah_file.name
	print "mode pembacaan file :",sebuah_file.mode
	print "isi file :\n",sebuah_file.read()
	print "posisi pointer pada file :",sebuah_file.tell()
	sebuah_file.close()
except IOError, e:
	print "gagal karena :",e

print "\n\n"
print "membaca file perbaris==============================================="
try:
	sebuah_file = open("absen.txt",'r')
	print "nama file",sebuah_file.name
	print "mode ", sebuah_file.mode
	print "isi file :\n"
	for line in sebuah_file:
		print line
	print "posisi pointer pada file :",sebuah_file.tell()
	sebuah_file.close()
except IOError, e:
	print "gagal karena :",e

print "\n\n"
print "mengatur posisi pointer=============================================="
try:
	sebuah_file = open("absen.txt",'rb')
	print "nama file :",sebuah_file.name
	print "mode : ",sebuah_file.mode
	print "isi file:\n"
	for line in sebuah_file:
		print line
	print "posisi pointer pada file:",sebuah_file.tell()
	print "kembali lagi ke awal :",sebuah_file.seek(0,0)
	print "isi file\n"
	for line in sebuah_file:
		print line
	print "posisi pointer pada file :",sebuah_file.tell()
	sebuah_file.close()
except IOError, e:
	print "gagal karena :",e
print "Pada contoh diatas, pointer file dipindahkan kembali ke posisi awal. Dengan memberikan jarak 0,"
print "dan menentukan patokan di awal file, maka posisi pointer file pindah ke bagian awal file. Dengan"
print "demikian file bisa dibaca ulang untuk kedua kalinya."

print "\n\n"
print "mengubah nama file==================================================="
try:
	os.rename('absen.txt','hoby.txt')
	print "Nama file sudah berubah..."
except (IOError, OSError), e:
	print "gagal karena",e

print "\n\n"
print "menghapus file================================================"
try:
	os.remove('hoby.txt')
	print "File sudah dihapus"
except (IOError, OSError), e:
	print "gagal karena",e

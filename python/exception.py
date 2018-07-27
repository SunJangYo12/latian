sebuah_angka = 29;

try:
	print sebuah_angka / 0
except:
	print "proses perhitungan gagal"
print "proses cetak ini masih dapat dijalankan"

try:
	print sebuah_angka / 0
except ZeroDivisionError, e:
	print "proses perhitungan gagal karena : ", e
print "proses cetak ini masih dapat dijalankan"

# print sebuah_angka / 0
# jika tidak memakai exception maka proses berikutnya tidak akan dijalankan
# print "apakah proses cetak ini masih dapat dijalankan ???"

print "\n"
sebuah_list = [1,2,3,4,5]
sebuah_tuple= (1,2,3,4,5)
sebuah_dictionary = {'nama':'Mangaraja','email':'mangaraja@gmail.com'}
try:
	print sebuah_list[10]
except IndexError, e:
	print "proses gagal karena :", e
print "proses cetak ini masih dapat dijalankan"

try:
	print sebuah_tuple[10]
except IndexError, e:
	print "proses gagal karena :", e
print "proses cetak ini masih dapat dijalankan"

try:
	print sebuah_dictionary['website']
except KeyError, e:
	print "proses gagal karena :", e
print "proses cetak ini masih dapar dijalankan"

print "\n\n"
print "populer========================================================"
class PersegiPanjang:
	panjang = 0
	lebar = 0
	def __init__(self,p,l):
		self.panjang = p
		self.lebar = l
persg_pjg = PersegiPanjang(10,5)
try:
	print "panjang : ",persg_pjg.panjang
	print "lebar   : ",persg_pjg.lebar
	print "tinggi  : ",persg_pjg.tinggi
except AttributeError, e:
	print "proses pemanggilan atribut gagal karena -->", e
print "proses cetak ini masih dapat dijalankan"

print "\n\n"
print "IOException========================================================"
try:
	f = open('nilai.txt')
except IOError, e:
	print "proses pembukaan file gagal karena :",e
print "ini masih dijalankan"

print "\n\n"
print "menyusun multi except================================================="
try:
	angka1 = int(raw_input('masukan angka ke-1:'))
	angka2 = int(raw_input('masukan angka ke-2:'))
	print 'hasil perhitungan :', angka1/ angka2
except ZerroDivisionError, e:
	print "proses pembagian gagal kerana :", e
except ValueError, e:
	print "proses perhitungan gagal karena :", e
print "ini masih dijalankan"

print "\n\n"
print "menggunakan multi exception=========================================="
try:
	angka1 = float(raw_input('masukan angka ke-1:'))
	angka2 = float(raw_input('masukna angka ke-2:'))
	print 'hasil perhitungan : ', angka1/angka2
except (ZeroDivisionError, ValueError, TypeError), e:
	print "proses perhitungan gagal karena : ",e
print "ini masih dijalankan"

print "\n\n"
print "except bersarang================================================="
try:
	angka1 = float(raw_input('masukan angka ke-1:'))
	angka2 = float(raw_input('masukan angka ke-2:'))
	try:
		print 'hasil perhitungan :', angka1 / angka2
	except ZeroDivisionError, e:
		print "proses perhitungan gagal karena :",e
except ValueError, e:
	print "proses input gagal karena :",e
print "ini masih dijalankan"

print "\n\n"
print "membuat sendiri except=============================================="
class NegativeValueError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		s = "Tidak menerima angka kurang dari 0" +str(self.value)
		return s
def cekAngka(angka):
	if angka < 0:
		raise NegativeValueError(angka)
try:
	sebuah_angka = int(raw_input('masukan sebuah angka :'))
	cekAngka(sebuah_angka)
except (NegativeValueError, TypeError), e:
	print "proses gagal karena :",e

print "\n\n"
print "menggunakan finally pada exception==================================="
try:
	angka1 = float(raw_input('masukan angka ke-1:'))
	angka2 = float(raw_input('masukan angka ke-2:'))
	try:
		print 'hasil perhitungan :', angka1 / angka2
	except ZeroDivisionError, e:
		print 'proses perhitungan gagal karena :',e
except ValueError, e:
	print "proses input gagal karena :",e
finally:
	print "coba perhatikan lagi nilai yang anda masukan"
print "ini masih dijalankan"

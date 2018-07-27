def fungsi_tanpa_parameter():
	for i in range(1, 5):
		print "looping ke - ", i
def fungsi_berparameter(batas_akhir):
	for i in range(1, batas_akhir):
		print "looping ke - ", i

print " tanpa return ========================================"
print " contoh penggunaan fungsi tanpa parameter : "
print "hasil : ", fungsi_tanpa_parameter()
print "\n"
print " contoh penggunaan fungsi berparameter : "
print "hasil : ", fungsi_berparameter(10)

print "\n\n"
print "menggunakan return ============================================"
def fungsi_tanpa_parameter():
	temp = 0
	for i in range(1, 5):
		temp = temp + i
	return temp
def fungsi_berparameter(batas_akhir):
	temp = 0
	for i in range(1, batas_akhir):
		temp = temp + i
	return temp
print " contoh penggunaan fungsi tanpa parameter : "
print "hasil : ", fungsi_tanpa_parameter()
print "hasil : ", fungsi_tanpa_parameter()
print "hasil : ", fungsi_tanpa_parameter()
print "\n"
print " contoh penggunaan fungsi berparameter : "
print "hasil : ", fungsi_berparameter(15)
print "hasil : ", fungsi_berparameter(20)
print "hasil : ", fungsi_berparameter(25)

print "\n\n"
print "argumen==========================================="
def cetak_biodata( nama, kota, umur=18):
	print "Nama : ", nama;
	print "Umur : ", umur;
	print "Kota : ", kota;
	return;
# kalau parameter diisi semua
print "Tanpa memakai default argument : "
cetak_biodata( nama="miki", umur=50, kota="bandung" )
print "\n"
# kalau parameter tidak diisi semua
print "Memakai default argument : "
cetak_biodata(kota="bandung", nama="miki")

print "\n\n"
print "variable-length argumen============================================"
def cetak_perolehan_nilai(nama,twitter, *scores):
	print "Nama :", nama;
	print "Twiter :", twitter;
	print "Score yang diperoleh :"
	i = 1
	for score in scores:
		print "nilai ke-%d : %d" %(i, score)
		i = i + 1
	return;
# kalau parameter diisi semua
print "Dengan adanya variabe-length variable sisa akan menjadi tuple : "
cetak_perolehan_nilai("Silvy","@sivlysiv",90,80,70,80,90)

print "\n\n"
print "keyword Argumen======================================================"
def cetak_biodata(nama,umur,kota):
	print "Nama :",nama;
	print "Umur :",umur;
	print "Kota :",kota;
# kalau pakai keyword argumen : mau urutanya gimanapun input akan sesuai
print "Tanpa memakai keyword argument : "
cetak_biodata(kota="bandung", nama="miki", umur=50)
print "\n"
# kalau tidak memakai keyword argument : mau urutanya gimanapun input tidak akan sesuai
print "Memakai keyword argument :"
cetak_biodata("bandung","miki", 50)
print "\n"
# kalau tidak memakai keyword argument : tapi urutanya sesuai maka input akan sesuai
print "Memakai keyword argument : tapi urutanya sesuai"
cetak_biodata("miki",50,"bandung")

print "\n\n"
print "keyword-length argumen==============================================="
def cetak_perolehan_nilai(nama,twitter,**data_tambahan):
	print "Nama :",nama;
	print "Twitter :",twitter;
	print "\n"
	print "Data lainya :"
	i = 1
	for data in data_tambahan:
		print "%s : %s" %(data, data_tambahan[data])
	return;
# kalau parameter diisi semua
print "Dengan adanya keyword argument, argument tersisa akan menjadi dictionary :"
cetak_perolehan_nilai("Silvy","@sivlysiv",email="silvfj@gmail.com",
facebook="www.facebook.com/sififjid", telp="0843-878-73848")

print "\n\n"
print "pass by refrence dan value ============================================"
def sebuah_fungsi(sebuah_list):
	sebuah_list = [1,2,3,4,5]
	print sebuah_list
def sebuah_fungsi_lainya(sebuah_list):
	sebuah_list.append([10,20,30])
	print sebuah_list
ini_list = [10,20,30]
sebuah_list = [100,200,300]
print "apakah ini_list berubah?"
print ini_list
sebuah_fungsi(ini_list)
print ini_list
print ini_list
sebuah_fungsi_lainya(ini_list)
print ini_list

print "apakah sebuah_list berubah ?"
print sebuah_list
sebuah_fungsi(sebuah_list)
print sebuah_list
print sebuah_list
sebuah_fungsi_lainya(sebuah_list)
print sebuah_list

print "\n\n"
print "variable scope====================================================="
def sebuah_fungsi():
	angka = 10
	print "didalam sebuah_fungsi, angka bernilai :", angka
def sebuah_fungsi_lainya():
	global angka
	angka = 114
	print "didalam sebuah_fungsi, angka bernilai :", angka
angka = 6666
print "sebelum dipanggil sebuah_fungsi :", angka
sebuah_fungsi()
print "sesudah dipanggil sebuah_fungsi :", angka
print "\n"
print "sebelum dipanggil sebuah_fungsi_lainya :", angka
sebuah_fungsi_lainya()
print "sesudah dipanggi sebuah_fungsi_lainya :", angka

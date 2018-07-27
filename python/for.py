print "for -------------------------------------------------"
for i in [1, 2, 3, 4, 5]:
	print "Ini pengulangan ke - ", i
for i in ["Rawon", "Nasi Kuning", "Soto Madura", "Kupat Tahu", "Kerak Telor", "Rendang Batoko", "Pempek Selam", "Ayam Betutu"] :
	print i, " adalah masakan khas nusantara ..."
for i in "abcde":
	print i, " adalah alfabet"

print "\n"
print "range() ---------------------------------------------"
print "Di Python terdapat fungsi yang bernama range. Range ini menghasilkan"
print "deret angka dengan parameter (start, stop, step). Start adalah batasawal dari list, stop adalah batas"
print "akhir dari list, step adalah jarak antar angka yang dihasilkan oleh range."
# kasus - 1 : jika step tidak disertakan maka step akan diisi 1 secara default
print range(1, 10)
# kasus - 2 : jika step disertakan maka step akan sesuai dengan angka yang diisikan31
print range(1, 10, 2)
print range(1, 10, 3)
print range(1, 10, 4)
print range(1, 10, 5)
# kasus - 3 : jika step melebihi stop maka list hanya akan berisi start
print range(1, 10, 11)
# kasus - 4 : jika start lebih besar nilainya daripada stop maka list akan kosong
print range(10, 1)
# kasus - 5 : jika start lebih besar nilainya daripada stop dan
# jika step melebihi stop maka list akan kosong
print range(10, 1, 2)
print range(10, 1, 11)
# kasus - 6 : jika start lebih besar daripada stop dan step bernilai minus
# dan jika start dikurangi step menghasilkan angka positif
# maka list akan berisi deret angka menurun
print range(10, 1, -1)
# kasus - 7 : jika start lebih besar daripada stop dan step bernilai minus
# dan jika start dikurangi step bernilai minus maka list hanya akan berisi start
print range(10, 1, -11)
# kasus - 8 : jika step bernilai 0 maka akan terjadi error
# print range(1, 10, 0)
# kasus - 9 : jika start lebih besar daripada stop dan step bernilai 0 maka akan terjadi error
# print range(10, 1, 0)

print "\n"
print "for range() -----------------------------------------------"
for i in range(1, 10):
	print "ini pengulangan ke - ", i

print "\n"
print "bintang"
for i in range(0, 10):
	for j in range (0, i+1):
		if j == i:
			print "x"
		else:
			print "*",
	print ""
print "\n"
print "mencari bilangan prima"
for i in range(1, 20):
	count_zero_remainder = 0
	for j in range(1, i+1):
		num_remainder = i % j
		#print num_remainder,
		if num_remainder == 0:
			count_zero_remainder = count_zero_remainder + 1
	if count_zero_remainder == 2:
		print i, " adalah bilangan prima"
	else:
		print i, " bukanlah bilangan prima"

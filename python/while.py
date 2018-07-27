angka = 0
while (angka < 10):
	print "Aku sudah berjalan sebanyak ", angka, " langkah "
	angka += 1

print "\n"
terus_tanya = True
while terus_tanya :
	temp = raw_input('masukkan angka kurang dari 10 !! : ')
	angka = int(temp)
	if angka < 10:
		terus_tanya = False
	else:
		terus_tanya = True

print "\n"
i = 1
jml_angka = 0
while i <= 10:
	print 'loop ke - %d : %d + %d' % (i, jml_angka, i)
	jml_angka = jml_angka + i
	i += 1
print 'total angka yang dijumlahkan : ', jml_angka

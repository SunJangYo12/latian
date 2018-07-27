# cara mendefinisikan list
sebuah_list = ['Zorin OS',
'Ubuntu',
'FreeBSD',
'NetBSD',
'OpenBSD',
'Backtrack',
'Fedora',
'Slackware']
# cara mendefinisikan tuple
sebuah_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# cara mendefinisikan dictionary
sebuah_dictionary = {'nama':'Wiro Sableng',
'prodi':'ilmu komputer',
'email':'wirosableng@localhost',
'website':'http://www.sitampanggarang.com'
}
print sebuah_list
print sebuah_tuple
print sebuah_dictionary

print "\n"
print "mengakses elemen====================================="
# mengakses elemennya
print "mengakses salah satu elemen : "
print "-----------------------------"
print sebuah_list[5]
print sebuah_tuple[8]
print sebuah_dictionary['website']
print "\n\n"
# mengakses beberapa elemen
print "mengakses beberapa elemen : "
print "-----------------------------"
print sebuah_list[2:5]
print sebuah_tuple[3:6]
print "\n\n"
# mengakses elemennya dengan looping
print "mengakses semua elemen dengan looping for : "
print "-----------------------------"
for sebuah in sebuah_list:
	print sebuah,
print "\n"
for sebuah in sebuah_tuple:
	print sebuah,
print "\n"
for sebuah in sebuah_dictionary:
	print sebuah, ':', sebuah_dictionary[sebuah],

print "\n"
print "update struktur=========================================="
# cara update sebuah elemen :
print "cara update sebuah elemen : "
print "\n"
print sebuah_list
sebuah_list[5] = 'Kali Linux'
print sebuah_list
print "\n"
print sebuah_tuple
# tuple tidak dapat melakukan operasi perubahan elemen :D
#sebuah_tuple[5] = 100
print sebuah_tuple
print "\n"
print sebuah_dictionary
sebuah_dictionary['email'] = 'wiro.sableng@gmail.com'
print sebuah_dictionary
print "\n\n"

print "menambah data==========================================="
# cara menambahkan data baru
print "cara menambahkan data baru : "
print "\n"
print sebuah_list
list_baru = sebuah_list + ['PC Linux OS', 'Blankon', 'IGOS', 'OpenSUSE']
print list_baru
print "\n"
print sebuah_tuple
tuple_baru = sebuah_tuple + (100, 200, 300)
print tuple_baru
print "\n"
print sebuah_dictionary
dictionary_baru = {'telp':'022-12345678', 'alamat':'Bandung, Jabar'}
sebuah_dictionary.update(dictionary_baru)
print sebuah_dictionary
print "\n\n"

print "menghapus data============================================"
# cara delete sebuah elemen :
print "cara delete sebuah elemen : "
print "\n"
print sebuah_list
del sebuah_list[0]
print sebuah_list
print "\n"
print sebuah_tuple
# tuple tidak mendukung proses penghapusan elemen :D.(coba hilangkan tanda '#' disampingnya)
#del sebuah_tuple[8]
print sebuah_tuple
print "\n"
print sebuah_dictionary
del sebuah_dictionary['website']
print sebuah_dictionary
print "\n\n"
# membandingkan yang lama dengan yang baru
print "membandingkan yang lama dengan yang baru ============================ \n"
print "sebuah_list banding list_baru : ", cmp(sebuah_list, list_baru)
print "sebuah_tuple banding tuple_baru : ", cmp(sebuah_tuple, tuple_baru)
print "sebuah_dictionary banding dictionary_baru : ", cmp(sebuah_dictionary, dictionary_baru)
print "\n\n"
# mengetahui panjang list, tuple, dan dictionary
print "mengetahui panjang list, tuple, dan dictionary========================= \n"
print "panjang sebuah_list : ", len(sebuah_list)
print "panjang sebuah_tuple : ", len(sebuah_tuple)
print "panjang sebuah_dictionary : ", len(sebuah_dictionary)
print "\n\n"
# mengubah list, tuple, dictionary menjadi string
print "mengubah list, tuple, dictionary menjadi string=========================\n"
print str(sebuah_list), ' memiliki panjang karakter : ', len(str(sebuah_list))
print str(sebuah_tuple), ' memiliki panjang karakter : ', len(str(sebuah_tuple))
print str(sebuah_dictionary), ' memiliki panjang karakter : ', len(str(sebuah_dictionary))
# mencari nilai max dan min
print "mencari nilai max dan min ============================================\n"
print "coba periksa sebuah_list :"
print "max : ", max(sebuah_list)
print "min : ", min(sebuah_list)
print "\n"
print "coba periksa sebuah_tuple :"
print "max : ", max(sebuah_tuple)
print "min : ", min(sebuah_tuple)
print "\n"
print "coba periksa sebuah_dictionary :"
print "max : ", max(sebuah_dictionary)
print "min : ", min(sebuah_dictionary)
print "\n"
# mengubah list ke tuple dan sebaliknya
print "mengubah list ke tuple ================================================"
print "semula : ", sebuah_list
print "menjadi : ", tuple(sebuah_list)
print "\n"
print "mengubah tuple ke list : "
print "semula : ", sebuah_tuple
print "menjadi : ", list(sebuah_tuple)

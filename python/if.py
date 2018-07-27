print "if-----------------------------------------------------"
print "Masukkan dua buah angka.."
angka1 = raw_input("Masukkan angka pertama : ")
angka1 = int(angka1)
angka2 = raw_input("Masukkan angka kedua : ")
angka2 = int(angka2)
if angka1 == angka2 :
	print "%d sama dengan %d" % (angka1, angka2)
if angka1 != angka2 :
	print "%d tidak sama dengan %d" % (angka1, angka2)
if angka1 < angka2 :
	print "%d kurang dari %d" % (angka1, angka2)
if angka1 > angka2 :
	print "%d lebih dari %d" % (angka1, angka2)
if angka1 <= angka2 :
	print "%d kurang dari sama dengan %d" % (angka1, angka2)
if angka1 >= angka2 :
	print "%d lebih dari sama dengan %d" % (angka1, angka2)

print "\n"
print "if else -------------------------------------------------------"
print "Masukkan dua buah angka.."
angka1 = raw_input("Masukkan angka pertama : ")
angka1 = int(angka1)
angka2 = raw_input("Masukkan angka kedua : ")
angka2 = int(angka2)
if angka1 == angka2 :
	print "%d sama dengan %d" % (angka1, angka2)
else:
	print "%d tidak sama dengan %d" % (angka1, angka2)

print "\n"
print "elif-------------------------------------------------------"
angka1 = raw_input("Masukkan angka pertama : ")
angka1 = int(angka1)
angka2 = raw_input("Masukkan angka kedua : ")
angka2 = int(angka2)
if angka1 == angka2 :
	print "%d sama dengan %d" % (angka1, angka2)
elif angka1 != angka2 :
	print "%d tidak sama dengan %d" % (angka1, angka2)
elif angka1 < angka2 :
	print "%d kurang dari %d" % (angka1, angka2)
elif angka1 > angka2 :
	print "%d lebih dari %d" % (angka1, angka2)
elif angka1 <= angka2 :
	print "%d kurang dari sama dengan %d" % (angka1, angka2)
elif angka1 >= angka2 :
	print "%d lebih dari sama dengan %d" % (angka1, angka2)

print "\n"
print "if nested -------------------------------------------------------"
username = raw_input("masukkan username : ")
password = raw_input("masukkan password : ")
username_from_db = "user"
password_from_db = "admin"
if username == username_from_db :
	if password == password_from_db :
		print "Username dan password cocok "
	else:
		print "Password salah "
else:
	print "User tidak terdaftar"

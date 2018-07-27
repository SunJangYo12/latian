from bidang import Segitiga,Persegi

sgtgA = Segitiga(3,9)
prsgA = Persegi(5)
print "Luas Segitiga A :", sgtgA.HitungLuas()
print "sisi miring segitiga A :",sgtgA.GetSisiMiring()
print "Keliling segitiga A :", sgtgA.HitungKeliling(sgtgA.GetSisiMiring())
print "\n"
print "Luas persegi A :", prsgA.HitungLuas()
print "Keliling segitiga A :", prsgA.HitungKeliling()

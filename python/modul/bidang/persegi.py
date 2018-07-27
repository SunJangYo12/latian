class Persegi:
        def __init__(self,s):
                self.sisi = s
        def SetSisi(self,s):
                self.sisi = s
        def GetSisi(self):
                return self.sisi
        def HitungKeliling(self):
                return 4 * self.sisi
        def HitungLuas(self):
                return self.sisi * self.sisi

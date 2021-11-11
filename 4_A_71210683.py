#list data harga
IkanBakar = 25000
EsDoger = 4000
RujakCingur = 8000

#Proses
print("=====MASUKKAN JUMLAH YANG DIPESAN=====")
MakananA = int(input("ikan bakar   Rp 25.000,00  : "))
MakananB = int(input("es doger     Rp 6.000,00   : "))
MakananC = int(input("rujak cingur Rp 8.000,00   : "))
      
#Total Harga Makanan
A = IkanBakar*MakananA
B = EsDoger*MakananB
C = RujakCingur*MakananC

print("=====TOTAL=====")
print("TOTAL IKAN BAKAR     : Rp ",MakananA)
print("TOTAL ES DOGER       : Rp ",MakananB)
print("TOTAL RUJAK CINGUR   : Rp ",MakananC)

#Total
total = MakananA+MakananB+MakananC
print("Jumlah total biaya yang harus dibayar adalah Rp",total)


                

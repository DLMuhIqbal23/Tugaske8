list_no = []
list_nama = []
list_nim = []
list_tugas = []
list_uts = []
list_uas = []
list_akhir = []
stop = False
x = 0 
while(not stop):
    list_nama.append(input("Nama : "))
    list_nim.append(int(input("NIM : ")))
    list_tugas.append(int(input("Nilai Tugas: ")))
    list_uts.append(int(input("Nilai UTS : ")))
    list_uas.append(int(input("Nilai UAS : ")))
    x += 1
    tanya = input("Tambah data(y/t): ")
    if(tanya == "t"):
        stop = True

for i in range(x):
    list_akhir.append(list_tugas[i] * 30/100 + list_uts[i] * 35/100 + list_uas[i] * 35/100)

print("=====================================================================================")
print("| No |\t\tNama\t\t|\tNIM\t|  Tugas  |  UTS  |  UAS   |  Akhir |")    
print("=====================================================================================")

for i in range (x):
    list_no.append(i+1)
    print("| %i  |\t\t%s\t\t|\t%i\t|    %i   |   %i  |   %i   |  {:.2f} |".format(list_akhir[i]) % (list_no[i], list_nama[i], list_nim[i], list_tugas[i], list_uts[i], list_uas[i]))
print("=====================================================================================")
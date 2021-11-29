# Tugaske8
Pertama yang dilakukan adalah masukkan array list dari no sampai dengan akhir, lalu masukkan stop sebagai falsen dan x bernilai 0. <p>
Selanjutnya kita menggunakan while(not stop) dengan kondisi stop masih false, kenapa menggunakan while (not stop)? agar nanti bila stop itu True perulangannya akan otomatis terhenti, lalu dibawahnya masukkan list array tadi lalu tambahkan (.append) append untuk menambahkan item, setelah itu list_nama.append sebagai string dan list_nim sampai dengan uas sebagai integer karena nilai yang akan diinput berupa angka satuan lalu x tambahkan dengan 1 selanjutnya masukkan tanya sebagai string, kenapa masukkan tanya? nanti setelah dirunning biar ada pilihan untuk melanjutkannya atau tidak, lalu masukkan if(tanya == "t") maka stop = True kenapa begini? agar jika nanti setelah dirunning ada pilihan lanjutkan atau tidak terus kita ketik t maka akan otomatis perulangannya berhenti karena stopnya sudah menjadi true.<p>
Selanjutnya masukkan perulangan for i in range(x) dan dibawahnya masukkan list_akhir.append(list_tugas[i] * 30/100 + list_uts[i] * 35/100 + list_uas[i] * 35/100) persennya terserah kalian, kenapa memakai [i]? agar nanti jika kita memasukkan 3 inputan tugas sampai dengan uas maka nanti hasil hasil dari list_akhir akan ada 3 dan jumlahnya berbeda tergantung nilai yang kalian masukkan.<p>
lalu untuk print (===) dan 2 dibawahnya itu terserah kalian mau mendesainnya bagaimana dan untuk "\t" itu gunannya untuk tab seperti di MsWord.<p>
Lalu masukkan perulangan for i in range (x) dan dibawahnnya masukkan list_no append(i+1), kenapa i+1? agar nanti list_no itu dimulai dengan angka 1, dan dibawahnnya ketik print("| %i  |\t\t%s\t\t|\t%i\t|    %i   |   %i  |   %i   |  {:.2f} |".format(list_akhir[i]) % (list_no[i], list_nama[i], list_nim[i], list_tugas[i], list_uts[i], list_uas[i])), {:.2f} |"format(list_akhir[i]) ini agar nanti {:.2f} akan memanggil list_akhir secara otomatis dan{:.2f} berfungsi untuk membatasi nilai desimal menjadi 2 angka dibelakang koma karena f itu adalah float atau bilangan desimal, lalu untuk yang lainnya kenapa menggunakan persen? sama seperti tadi % berfungsi untuk memanggil array list yang tadi lalu setelahnya sesuaikan bila list arraynya integer maka pakailah %i, dan jika list arraynya menggunakan string maka pakailah %s, dan terakhir print(=====) gunanya untuk merapihkan saja.<p>
Dan ini contoh kodenya<p>
[Gambar 1](ss/ss2.png)
[Gambar 2](ss/ss3.png)
Dan ini hasil dari kode yang tadi:
[Gambar 3](ss/ss1.png)
Dan ini adalah flowchartnya:<p>
Halaman pertama
[Gambar 4](ss/ss4.png)
Halaman 2
[Gambar 5](ss/ss5.png)
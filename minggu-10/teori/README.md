Pengantar Struktur Data
prinsip dasar yang harus diingat->penyelesaian data bersifat intrinsik.

Seri
adalah latik berlabel satu dimensi yang mampu menyimpan semua tipe data(bilangan bulat, string, angka floating point, objek python dll). 
label sumbu secara kolektif disebut sebagai indeks.
metode dasar untuk membuat seri adalah memanggil
>>> s = pd.Series(data, Index=index).
Data bisa banyak berbeda;- a python dict
                         - an ndarray
                         - a scalar value

- dict
ketika data berupa dict dan indeks tidak lulus, indeks seri akan diperintahkan oleh perintah penyisipan dict.
- ndarray
indeks harus memiliki panjang yang sama dengan data. jika tidak ada indek yang dilewatkan, yang akan dibuat memiliki nilai {0,..,len(data)-1]
- Scalar value
nilai skalar, indek harus disediakan nilai akan diulang agar sesuai dengan panjang indek.

>>Series is ndarray like
seris bertindak sangat mirip dg ndarray dan merupakan argumen yang valid untuk sebgai besar fungsi Numpy.
>>Series id dict like
series dikat ukuran tetap dimana bisa mendapatkan dan menetapkan nilai berdasarkan label indeks.

DataFrame
adalah struktur data berlabel 2 dimensi dengan kolom jenis yang berpontensi berbeda. 
dataframe menerima berbagai macam input
- dict of 10 ndarray, list, dicts or series
- 2D Numpy ndarray
- Struktur or recond ndarray
- a series
- anither daraframe.

Missing Data
Untuk membuat DataFrame dengan data yang hilang, kami menggunakan np.nan untuk merepresentasikan nilai yang hilang. Alternatifnya, 
dapat melewati numpy.MaskedArray sebagai argumen data ke konstruktor DataFrame, dan entri bertopengnya akan dianggap hilang

DataFrame.from_dict
DataFrame.from_dict mengambil dikt of dicts atau dict of array-like sequences dan mengembalikan DataFrame. 
Ini beroperasi seperti konstruktor DataFrame kecuali untuk parameter orientasi yang 'kolom' secara default, 
tetapi yang dapat diatur ke 'indeks' untuk menggunakan tombol dict sebagai label baris.
DataFrame.from_recordsmengambil daftar tupel atau ndarray dengan dtype terstruktur. Ia bekerja secara analog dengan konstruktor 
DataFrame normal, kecuali bahwa indeks DataFrame yang dihasilkan mungkin merupakan bidang spesifik dari dtype terstruktur

Data alignment and arithmetic
Penyelarasan data antara objek DataFrame secara otomatis sejajar pada kolom dan indeks (label baris). 
Sekali lagi, objek yang dihasilkan akan memiliki penyatuan label kolom dan baris.

DataFrame interoperability with NumPy functions
Elementwise NumPy ufuncs (log, exp, sqrt,…) dan berbagai fungsi NumPy lainnya dapat digunakan tanpa masalah pada DataFrame,
dengan asumsi data di dalamnya adalah numerik

Console display
DataFrames yang sangat besar akan dipotong untuk menampilkannya di konsol. Anda juga bisa mendapatkan ringkasan menggunakan info (). 
(Di sini saya membaca versi CSV dari dataset bisbol dari paket plyr R

Panel


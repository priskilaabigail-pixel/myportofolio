Priskila Abigail Magaini 2506590252

### Tugas 1

1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

- Ya, saya menggunakan elemen semantik. Elemen-elemen seperti <header>, <footer>, dan lainnya membantu saya untuk membedakan bagian-bagian website dalam kode saya di file html.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

- Tantangan tata letak yang saya temukan adalah cara mengatur letak section baru yang saya tambahkan. Saya tidak terlalu harus mengevaluasi elemen yang harus diubah posisinya saat berpindah tampilan karena saya lebih banyak menggunakan elemen-elemen yang sudah ada dari template tutorial. Saya hanya menambahkan sedikit elemen baru dan saya menyesuaikannya dengan elemen yang sudah ada sebelumnya.

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

- Batasan yang saya rasakan saat mencoba menyajikan informasi pada portofolio salah adalah interaktivitas yang kurang, contohnya pada bagian skills saya mencantumkan 2 kategori skills yang sangat berbeda. Misal dengan fitur filter kategori skills, pengunjung bisa melihat hanya satu dari 2 kategori skills tadi.

AI disclosure:
Saya menggunakan AI untuk menjelaskan ulang ke saya berbagai macam bagian dari projek ini. Kemudian saya juga menggunakan AI untuk menanyakan beberapa komponen dari pertanyaan di atas. (https://share.gemini.google/aejR6JVNmubn)
Saya tidak menggunakan AI untuk membuat section baru di web saya.

### Tugas 2

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

- Ketika pengguna mengirimkan request, request akan dikirimkan ke server. Kemudian request akan sampai di urls.py proyek yang akan mengopernya ke urls.py aplikasi. urls.py aplikasi akan mencocokan bagian akhir link lalu memanggil view yang tepat. Di view, logika bisnis dijalankan dan jika perlu view akan memanggil models (untuk data dinamis). Model adalah bentuk tabel database, model akan mengambil data yang diminta dari database kemudian mengirimkannya ke view. Lalu, template adalah kerangka tampilan. Biasanya akan ada placeholder pada template untuk menerima data dari view. Setelah semuanya bersatu menjadi file yang utuh, file tersebut akan dikirimkan kembali ke view yang akan mengirimkannya ke browser sebagai HTTP response.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

- Agar perubahan dan penambahan data menjadi lebih mudah. Jika ditulis langsung di dalam template, untuk mengubah atau menambahkan data kita harus menulis ulang di template. Sedangkan jika disimpan pada model kita bisa membuat objek baru di terminal dan langsung tercatat.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

- makemigrations berfungsi untuk mencatat perubahan yang dibuat pada kode dengan cara memindai models.py kemudian membuat file-file migrations. Sedangkan migrate berfungsi untuk mengeksekusi file-file migrations yang telah dibuat dengan cara mengirimkannya ke sistem database. Contohnya saat saya membuat atribut baru pada sebuah model, saya akan menjalankan kedua perintah makemigrations dan migrate secara berurutan.

AI disclosure:
Saya menggunakan AI untuk memperbaiki error di PWS karena ketidakcocokan versi Django yang digunakan di pws dan yang saya gunakan. Kemudian saya juga menanyakan AI untuk mengubah password admin. Terakhir saya menggunakan AI untuk memastikan bahwa kode HTML saya menghasilkan hasil yang saya inginkan. (https://share.gemini.google/SszJSYqb5e4X`)

### Tugas 3

1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!

- ModelForm pada Django efisien karena membantu kita mencatat data dengan logika yang tidak repetitif, otomatis membuatkan tag HTML, otomatis memvalidasi data, dan menyimpan langsung data ke database sesuai model yang ada. csrf_token berguna untuk memverifikasi bahwa data form yang dikirim memang dari website kita, bukan dari website lain.

2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

- JSON lebih disukai karena ukurannya ringan dan minim sintax, sehingga proses pemindahan data jadi lebih cepat dibanding XML.

3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

- User mengirimkan request ke URL tertentu yang kemudian dicocokan oleh Django dan memanggil fungsi view yang bertugas. Di view, Django kemudian mengambil data dari database. Hasil dari proses tersebut adalah QuerySet. QuerySet tersebut dimasukan kedalam fungsi serializers.serialize("json", data) yang akan mengubah struktur data menjadi bentuk string yang berstandar JSON. Serialization berfungsi sebagai penerjemah yang mengubah data dari bentuk kompleks menjadi bentuk teks pasangan key-value yang universal. Format JSON bersifat universal, ringan, dan gampang diurai menjadi objek disisi user.

AI Disclosure:
Saya menggunakan AI untuk membantu saya mengerti objektif tugas, membantu membuat ModelForm, menjelaskan kode, membantu membuat methods di views, membuat komponen template css, membantu membuat file html, mengatasi error, membantu membuat fitur edit, dan membantu menjawab pertanyaan refleksi. (https://share.gemini.google/TMlqb886ijf9)

### Tugas 4

AI Disclosure:
Saya menggunakan AI untuk membantu saya mengerti objektif tugas, membantu membuat komponen template css, menghapus cookies, menambahkan user group 'editor', dan memastikan fitur-fitur tersedia untuk user yang tepat. (https://share.gemini.google/oYzYkACPtXkp)

### Tugas 6

REST is a software architectural style that
describes a uniform interface between
physically separate components, often
across the Internet in a Client-Server
architecture.


1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!

- REST adalah arsitektur software yang mencakup interface yang seragam antara komponen-komponen yang terpisah, ering kali melintasi internet dalam arsitektur Client-Server. Mengembalikan JSON saja belum cukup karena JSON hanyalah format data. API disebut RESTful kalau juga memakai URL berbasis resource, method HTTP sesuai semantiknya, status code yang tepat (201, 404, 403), dan tidak menyimpan state klien di server. 

Perbedaan PUT dan PATCH: 
PUT mengganti seluruh resource, sehingga semua field wajib dikirim. Contoh: mengubah seluruh field education. Sedangkan PATCH mengubah sebagian field saja. Contoh: mengubah end_year saja.

2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?

- Serializer mengubah objek model/queryset menjadi tipe data native yang kemudian bisa diubah menjadi format JSON dan sebaliknya. Keuntungan dibanding JsonResponse manual:

- Kode lebih ringkas dan konsisten, tidak perlu menyusun dictionary per field.
- Validasi input otomatis
- Mendukung create/update langsung
- Perubahan model cukup disesuaikan di satu tempat

3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?

- Autentikasi adalah proses untuk mengidentifikasi user, sedangkan otorisasi adalah proses untuk menentukan hak akses user. Hak akses harus diperiksa dengan permission class di server agar user yang tidak mempunyai hak akses tidak bisa memanggil endpoint langsung lewat browser devtools, curl, atau postman. Menyembunyikan tombol di template hanya mengubah penampilan bagi user tanpa melarang.

4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?

- SessionAuthentication memakai cookie sesi yang dikirim browser, termasuk dari situs jahat. Karena itu permintaan yang mengubah data (POST, PUT, PATCH, DELETE) wajib menyertakan token CSRF agar server tahu permintaan berasal dari halaman yang sah.

force_authenticate tidak cukup karena melewati authentication class, sehingga pemeriksaan CSRF tidak pernah dijalankan dan test lulus tanpa token. Pembuktian yang benar memakai client.login() dengan APIClient(enforce_csrf_checks=True), lalu memastikan permintaan tanpa token ditolak (403).


AI Disclosure:
Saya menggunakan AI untuk membantu membuat implementasi Django RESTful untuk education, mulai dari api_views, serializers, education_html, api_urls, dan tests_api. Tetapi saya juga memastikan kode berjalan dengan lancar. Saya juga menggunakan AI untuk debugging. Selain itu, saya menggunakan AI untuk membantu saya menjawab pertanyaan reflektif. (https://share.gemini.google/KKpGzd69mbtZ)
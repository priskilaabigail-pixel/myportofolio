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

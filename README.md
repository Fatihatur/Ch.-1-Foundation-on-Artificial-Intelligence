Berikut adalah struktur teks yang telah diubah:

---

# Bab 1: Foundation on Artificial Intelligence (team task at Google Colab only)

## Daftar Isi

1. [Kalkulasi Pecahan Uang Tunai (`01_Kelompok_E_2.ipynb`)](#1-kalkulasi-pecahan-uang-tunai-01_kelompok_e_2ipynb)
2. [Analisis Data & Visualisasi (`01_Kelompok_E_3.ipynb`)](#2-analisis-data--visualisasi-01_kelompok_e_3ipynb)

## 1. Kalkulasi Pecahan Uang Tunai (`01_Kelompok_E_2.ipynb`)

### Deskripsi Tugas
Tugas ini mengharuskan pembuatan program Python yang menerima input berupa jumlah uang simpanan nasabah (dalam bentuk integer) dan menghitung jumlah masing-masing pecahan uang kertas dan koin Indonesia yang dibutuhkan untuk penarikan. Rentang input adalah dari Rp 0 hingga Rp 1 miliar.

### Spesifikasi
- **Input**: Integer yang merepresentasikan simpanan nasabah.
- **Output**: Jumlah setiap pecahan uang yang dibutuhkan dan pemberitahuan jika terdapat saldo yang tidak bisa dicairkan.

### Ketentuan
1. Mendahulukan pecahan uang terbesar.
2. Memberikan informasi jika ada sisa saldo yang tidak dapat ditarik.
3. Menghitung jumlah uang kertas dan koin secara terpisah.
4. Penarikan maksimal sebesar Rp 1 miliar.

### Struktur Kode
- **Validasi Input**: Memastikan bahwa input integer berada dalam rentang yang sesuai.
- **Kalkulasi Pecahan**: Menggunakan loop untuk menentukan jumlah setiap pecahan yang diperlukan.
- **Output Hasil**: Menampilkan jumlah uang kertas dan koin yang dibutuhkan, total uang kertas dan koin, serta saldo sisa yang tidak bisa dicairkan, jika ada.

---

## 2. Analisis Data & Visualisasi (`01_Kelompok_E_3.ipynb`)

### Deskripsi Tugas
Tugas ini berfokus pada analisis data menggunakan pustaka `pandas` dan visualisasi data dengan `matplotlib` dan `seaborn` pada dataset HRDataset.

### Tahapan Analisis
1. **Statistik Gaji Berdasarkan Status Pernikahan dan Jenis Kelamin**
   - Menggunakan `groupby` dan `agg` untuk mendapatkan nilai minimum, median, maksimum, dan rata-rata gaji.

2. **Alasan PHK Teratas (Top-5)**
   - Menggunakan `value_counts` untuk menemukan alasan PHK terbanyak.

3. **Sumber Rekrutmen Tertinggi untuk Karyawan dengan Skor Kinerja 'Exceeds'**
   - Menggunakan filter `PerformanceScore == 'Exceeds'` dan pengelompokan berdasarkan `RecruitmentSource`.

4. **Jumlah Manajer per Departemen**
   - Menggunakan `groupby` dan `nunique` untuk menghitung jumlah manajer unik di setiap departemen.

5. **Rasio PHK Berdasarkan Jenis Kelamin**
   - Menggunakan `value_counts` dengan normalisasi untuk menghitung rasio PHK per jenis kelamin.

### Visualisasi Data
1. **Rasio PHK Berdasarkan Jenis Kelamin**: Menggunakan bar chart untuk menunjukkan rasio PHK menurut jenis kelamin.
2. **Scatter Plot**: Visualisasi hubungan antara "Salary" dan "EngagementSurvey" dengan warna berbeda berdasarkan status `Termd`.
3. **Jumlah PHK Berdasarkan Departemen**: Bar chart yang menunjukkan jumlah PHK per departemen.
4. **Persentase PHK Berdasarkan Posisi (Pie Chart)**: Menampilkan persentase PHK menurut posisi karyawan.
5. **Boxplot Gaji Berdasarkan Status Pernikahan dan Status PHK**: Boxplot yang memperbandingkan distribusi gaji.
6. **Pairplot**: Menampilkan hubungan antarvariabel "Salary," "EngagementSurvey," "EmpSatisfaction," dan "Absences," dikategorikan berdasarkan status `Termd`.

---

## Petunjuk Menjalankan Kode

1. Buka Google Colab.
2. Unggah file `01_Kelompok_E_2.ipynb` dan `01_Kelompok_E_3.ipynb`.
3. Untuk `01_Kelompok_E_3.ipynb`, pastikan dataset HR tersedia melalui URL atau unggah langsung dataset tersebut ke Google Colab.

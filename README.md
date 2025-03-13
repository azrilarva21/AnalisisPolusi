# 📊 Dashboard Analisis Udara
by Wildan Azril Arvany
Akses : https://guanyuanpolusi.streamlit.app/
## Deskripsi Proyek
Dashboard ini dikembangkan untuk memantau dan menganalisis data kualitas udara di wilayah Guanyuan dari tahun 2013 hingga 2017. Proyek ini mengumpulkan informasi terkait:
- **Polutan Utama:** PM2.5, PM10, SO2, NO2, CO, dan O3.
- **Parameter Cuaca:** Suhu (TEMP), Tekanan Udara (PRES), Titik Embun (DEWP), Curah Hujan (RAIN), dan Kecepatan Angin (WSPM).

Visualisasi interaktif dibangun menggunakan Streamlit sehingga pengguna dapat dengan mudah menjelajahi tren polusi udara serta hubungannya dengan kondisi cuaca.

## Fitur Utama
- **Filter Dinamis:** Pilih tahun dan bulan untuk analisis mendetail.
- **Grafik Tren Polusi:** Menampilkan perubahan konsentrasi polutan seiring waktu.
- **Heatmap Korelasi:** Mengungkap hubungan antara parameter cuaca dan tingkat polusi.
- **Peta Interaktif:** Visualisasi distribusi polutan dalam area studi.
- **Ringkasan Analisis:** Dokumentasi lengkap dan kesimpulan hasil analisis.

## Struktur File Proyek
- **DashBoard_Polusi.py:** File utama yang memuat kode dashboard (dibuat dengan Streamlit).
- **PRSA_Data_Guanyuan_20130301-20170228.csv:** Dataset yang berisi data kualitas udara.
- **requirements.txt:** Daftar pustaka Python yang dibutuhkan untuk menjalankan proyek.
- **README.md:** Dokumentasi lengkap mengenai proyek ini.

## Cara Menjalankan Dashboard
1. **Instal Python:**  
   Pastikan Python telah terpasang pada sistem Anda. Jika belum, silakan unduh dari [python.org](https://www.python.org).

2. **Instal Dependensi:**  
   Buka terminal dan jalankan perintah berikut untuk memasang semua pustaka yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi Streamlit:**  
   Gunakan perintah di bawah ini untuk menjalankan dashboard:
   ```bash
   streamlit run DashBoard_Polusi.py
   ```

4. **Akses Dashboard:**  
   Setelah aplikasi berjalan, Anda dapat mengakses dashboard melalui:
   - **Localhost:** [http://localhost:8501](http://localhost:8501)
 
## Troubleshooting Umum
- **Module Tidak Ditemukan (ModuleNotFoundError):**  
  Jika muncul pesan error seperti:
  ```bash
  ModuleNotFoundError: No module named 'folium'
  ```
  Anda bisa mengatasi dengan menginstal modul yang hilang:
  ```bash
  pip install folium streamlit-folium
  ```

- **File Tidak Ditemukan:**  
  Apabila muncul error:
  ```bash
  Error: Invalid value: File does not exist: DashBoard_Polusi.py
  ```
- **Localhost Tidak Merespon:**  
  Jika [http://localhost:8501](http://localhost:8501) tidak dapat diakses, coba jalankan dengan port alternatif:
  ```bash
  streamlit run DashBoard_Polusi.py --server.port 8502
  ```
  Juga, periksa pengaturan firewall atau antivirus yang mungkin menghambat akses.
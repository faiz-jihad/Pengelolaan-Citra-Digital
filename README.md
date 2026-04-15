# 📘 Image Enhancement Project

### Sharpening & Contrast Adjustment (CLAHE)

---

## 📌 Deskripsi

Project ini merupakan implementasi teknik **perbaikan kualitas citra (image enhancement)** menggunakan Python.
Metode yang digunakan meliputi:

* 🔍 **Image Sharpening** → untuk mengatasi citra blur
* 🌗 **CLAHE (Contrast Limited Adaptive Histogram Equalization)** → untuk meningkatkan kontras

Project ini dibuat sebagai tugas mata kuliah **Pengolahan Citra Digital**.

---

## 🎯 Tujuan

* Memperbaiki citra yang blur agar lebih tajam
* Meningkatkan kontras citra dengan metode adaptif
* Memahami penggunaan OpenCV dan NumPy dalam pengolahan citra

---

## 🧰 Teknologi yang Digunakan

* Python 3.x
* OpenCV (`cv2`)
* NumPy
* Matplotlib
* Jupyter Notebook

---

## 📂 Struktur Project

```
project/
│
├── venv/                  # Virtual environment
├── blured.jpg             # Dataset citra blur
├── contrast.png           # Dataset citra kontras rendah
├── Image-enhanced.ipynb   # Notebook utama
├── hasil_sharpen.jpg      # Output sharpening
├── hasil_clahe.jpg        # Output CLAHE
└── README.md
```

---

## ⚙️ Instalasi

### 1. Clone / Download Project

```bash
git clone <repository-url>
cd project
```

### 2. Buat Virtual Environment

```bash
python -m venv venv
```

### 3. Aktifkan Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Mac:**

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install opencv-python numpy matplotlib notebook ipykernel
```

---

### 5. Jalankan Jupyter Notebook

```bash
jupyter notebook
```

Lalu buka:

```
Image-enhanced.ipynb
```

---

## 🚀 Cara Menjalankan

1. Pastikan semua dependency sudah terinstall
2. Jalankan Jupyter Notebook
3. Run semua cell secara berurutan
4. Hasil akan ditampilkan dalam bentuk visual (before–after)

---

## 🔍 Metode yang Digunakan

### 1. Sharpening

Menggunakan kernel konvolusi:

```python
kernel = [[-1,-1,-1],
          [-1, 9,-1],
          [-1,-1,-1]]
```

Fungsi:

* Menonjolkan tepi objek
* Mengurangi efek blur

---

### 2. CLAHE

Langkah:

1. Konversi BGR → LAB
2. Ambil channel L (luminance)
3. Terapkan CLAHE
4. Gabungkan kembali

Fungsi:

* Meningkatkan kontras lokal
* Menghindari over-exposure

---

## 📊 Hasil

### 🔹 Sharpening

* Sebelum: gambar blur
* Sesudah: tepi objek lebih tajam

### 🔹 CLAHE

* Sebelum: kontras rendah
* Sesudah: detail lebih terlihat

---

## 🧠 Analisis

* Sharpening efektif untuk meningkatkan ketajaman, tetapi berpotensi menambah noise
* CLAHE lebih baik dibanding histogram equalization global karena menjaga detail lokal
* Kombinasi kedua metode memberikan hasil yang optimal

---

## 📌 Output

Hasil akan disimpan sebagai:

* `hasil_sharpen.jpg`
* `hasil_clahe.jpg`

---

## ❗ Catatan

* Pastikan file gambar berada di folder yang sama
* Jangan menjalankan `.ipynb` dengan Python langsung
* Gunakan Jupyter Notebook / VS Code

---

## 👨‍💻 Author

**Nama:** Faiz Jihad A.
**Mata Kuliah:** Pengolahan Citra Digital

---

## 📄 Lisensi

Digunakan untuk keperluan pembelajaran dan akademik.

---

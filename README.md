# Image Enhancement Project: Sharpening and Contrast Adjustment

## Overview

This project implements advanced image enhancement techniques using Python, focusing on sharpening blurred images and improving contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization). Developed as part of the Digital Image Processing course, this implementation demonstrates practical applications of computer vision algorithms.

## Features

- **Image Sharpening**: Utilizes unsharp masking technique to restore sharpness in blurred images
- **Contrast Enhancement**: Implements CLAHE for adaptive contrast improvement without over-enhancement
- **Professional Visualization**: Side-by-side comparison of original and enhanced images
- **High-Quality Output**: Saves processed images with optimized quality settings
- **Modular Code**: Well-structured functions with comprehensive error handling

## Technologies Used

- **Python 3.x**
- **OpenCV** - Computer vision library
- **NumPy** - Numerical computing
- **Matplotlib** - Data visualization
- **Jupyter Notebook** - Interactive development environment

## Project Structure

```
Image-Enhancement/
│
├── images/                    # Input images directory
│   ├── blured.jpg            # Blurred image sample
│   └── contrast.png          # Low-contrast image sample
│
├── hasil/                     # Output directory
│   ├── hasil_sharpen.jpg     # Sharpened image output
│   └── hasil_clahe.jpg       # CLAHE enhanced image output
│
├── venv/                      # Python virtual environment
├── Image-enhanced.ipynb       # Main Jupyter notebook
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd image-enhancement-project
   ```

2. **Create virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

## Usage

1. Open `Image-enhanced.ipynb` in Jupyter Notebook
2. Execute cells sequentially to:
   - Load input images
   - Apply sharpening algorithm
   - Apply CLAHE contrast enhancement
   - Visualize results
   - Save enhanced images

## Key Functions

### `unsharp_mask(image, sigma=2.0, strength=2.0)`

Applies unsharp masking for image sharpening.

### `apply_clahe(image, clip_limit=4.0, tile_grid_size=(8,8))`

Enhances image contrast using CLAHE algorithm.

### `plot_comparison(original, processed, title_original, title_processed)`

Creates professional before/after image comparisons.

## Results

The project successfully demonstrates:

- Significant improvement in image sharpness
- Enhanced contrast without artifacts
- Maintains natural image appearance
- High-quality output suitable for further processing

## Academic Context

This project was developed for the **Digital Image Processing** course, showcasing practical implementation of:

- Spatial domain filtering
- Histogram equalization techniques
- Adaptive image enhancement algorithms

## License

This project is developed for educational purposes.

## Author

[Your Name] - Digital Image Processing Course Project

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

- Menonjolkan tepi objek
- Mengurangi efek blur

---

### 2. CLAHE

Langkah:

1. Konversi BGR → LAB
2. Ambil channel L (luminance)
3. Terapkan CLAHE
4. Gabungkan kembali

Fungsi:

- Meningkatkan kontras lokal
- Menghindari over-exposure

---

## 📊 Hasil

### 🔹 Sharpening

- Sebelum: gambar blur
- Sesudah: tepi objek lebih tajam

### 🔹 CLAHE

- Sebelum: kontras rendah
- Sesudah: detail lebih terlihat

---

## 🧠 Analisis

- Sharpening efektif untuk meningkatkan ketajaman, tetapi berpotensi menambah noise
- CLAHE lebih baik dibanding histogram equalization global karena menjaga detail lokal
- Kombinasi kedua metode memberikan hasil yang optimal

---

## 📌 Output

Hasil akan disimpan sebagai:

- `hasil_sharpen.jpg`
- `hasil_clahe.jpg`

---

## ❗ Catatan

- Pastikan file gambar berada di folder yang sama
- Jangan menjalankan `.ipynb` dengan Python langsung
- Gunakan Jupyter Notebook / VS Code

---

## 👨‍💻 Author

**Nama:** Faiz Jihad A.
**Mata Kuliah:** Pengolahan Citra Digital

---

## 📄 Lisensi

Digunakan untuk keperluan pembelajaran dan akademik.

---

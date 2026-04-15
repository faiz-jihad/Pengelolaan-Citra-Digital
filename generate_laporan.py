from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.units import cm
import os

PDF_FILE = 'Laporan_Tugas.pdf'
INPUT_IMAGES = [
    ('Original Blur', 'images/blured.jpg'),
    ('Sharpened Result', 'hasil/hasil_sharpen.jpg'),
    ('Original Low Contrast', 'images/contrast.png'),
    ('CLAHE Result', 'hasil/hasil_clahe.jpg'),
]

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CustomTitle', fontSize=24, leading=28, alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name='CustomHeading1', fontSize=18, leading=22, spaceBefore=12, spaceAfter=10))
styles.add(ParagraphStyle(name='CustomHeading2', fontSize=14, leading=18, spaceBefore=10, spaceAfter=8))
styles.add(ParagraphStyle(name='CustomBodyText', fontSize=11, leading=16, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Caption', fontSize=9, leading=12, alignment=TA_CENTER, spaceAfter=6, textColor=colors.gray))

story = []

story.append(Paragraph('LAPORAN TUGAS AKHIR', styles['CustomTitle']))
story.append(Paragraph('Image Enhancement Project: Sharpening and CLAHE Contrast Adjustment', styles['Heading2']))
story.append(Spacer(1, 12))
story.append(Paragraph('Nama Mahasiswa: [Masukkan Nama Anda]', styles['BodyText']))
story.append(Paragraph('Mata Kuliah: Pengolahan Citra Digital', styles['BodyText']))
story.append(Paragraph('Dosen Pengampu: [Masukkan Nama Dosen]', styles['BodyText']))
story.append(Paragraph('Semester: 4', styles['BodyText']))
story.append(Spacer(1, 20))

story.append(Paragraph('1. Pendahuluan', styles['CustomHeading1']))
story.append(Paragraph(
    'Laporan ini membahas implementasi teknik peningkatan kualitas citra digital dengan fokus pada pemulihan ketajaman gambar yang blur dan peningkatan nilai kontras pada citra dengan kontras rendah. ' 
    'Penggunaan OpenCV, NumPy, dan Matplotlib memungkinkan pemrosesan citra secara efisien dan visualisasi hasil secara profesional.',
    styles['BodyText']))

story.append(Paragraph('2. Tujuan', styles['CustomHeading1']))
story.append(Paragraph(
    'Tujuan utama dari tugas ini adalah:\n'
    '- Memperbaiki ketajaman citra blur menggunakan teknik sharpening.\n'
    '- Meningkatkan kontras citra menggunakan algoritma CLAHE.\n'
    '- Menyajikan perbandingan sebelum dan sesudah pemrosesan dengan visualisasi yang jelas.',
    styles['BodyText']))

story.append(Paragraph('3. Ruang Lingkup', styles['CustomHeading1']))
story.append(Paragraph(
    'Laporan ini mencakup proses teknis mulai dari pemuatan citra, praproses, metode sharpening, metode CLAHE, visualisasi hasil, sampai penyimpanan output secara berkualitas.',
    styles['BodyText']))

story.append(Paragraph('4. Landasan Teori', styles['CustomHeading1']))
story.append(Paragraph(
    '<b>Sharpening</b> adalah teknik peningkatan tepi pada citra untuk membuat detail lebih jelas. ' 
    'Metode unsharp masking bekerja dengan mengurangkan versi citra yang sudah diburamkan dari citra asli sehingga detail halus menjadi lebih menonjol.',
    styles['BodyText']))
story.append(Paragraph(
    '<b>CLAHE</b> (Contrast Limited Adaptive Histogram Equalization) adalah algoritma adaptif yang memperbaiki distribusi intensitas pada setiap blok citra. '
    'Pendekatan ini mengurangi over-enhancement dengan membatasi kontras lokal pada nilai tertentu.',
    styles['BodyText']))

story.append(Paragraph('5. Alat dan Teknologi', styles['CustomHeading1']))
story.append(Paragraph(
    '- Python 3.x\n'
    '- OpenCV untuk pemrosesan citra\n'
    '- NumPy untuk komputasi numerik\n'
    '- Matplotlib untuk visualisasi\n'
    '- Jupyter Notebook untuk interaktifitas dan dokumentasi',
    styles['BodyText']))

story.append(Paragraph('6. Metodologi', styles['CustomHeading1']))
story.append(Paragraph(
    'Alur kerja terdiri dari beberapa tahap utama: pemuatan gambar, implementasi fungsi pemrosesan, visualisasi perbandingan, dan penyimpanan hasil. ' 
    'Bagian ini memastikan semua langkah dilakukan secara terstruktur.',
    styles['BodyText']))
story.append(Paragraph('6.1 Pemuatan Gambar', styles['Heading2']))
story.append(Paragraph(
    'Gambar dimuat menggunakan fungsi OpenCV. Proses memeriksa keberadaan file diperlukan untuk mencegah kesalahan jika sumber data tidak ditemukan.',
    styles['BodyText']))
story.append(Paragraph('6.2 Pengolahan Sharpening', styles['Heading2']))
story.append(Paragraph(
    'Sharpening diterapkan menggunakan fungsi unsharp masking. Teknik ini menggunakan Gaussian blur untuk menghasilkan citra kabur yang kemudian dikombinasikan dengan citra asli untuk memperkuat detail tepi.',
    styles['BodyText']))
story.append(Paragraph('6.3 Pengolahan CLAHE', styles['Heading2']))
story.append(Paragraph(
    'CLAHE diterapkan pada kanal luminansi citra pada ruang warna LAB untuk menjaga pewarnaan dan meningkatkan kontras secara adaptif di setiap area citra.',
    styles['BodyText']))

story.append(PageBreak())

story.append(Paragraph('7. Implementasi', styles['CustomHeading1']))
story.append(Paragraph(
    'Implementasi utama dilakukan dalam file `Image-enhanced.ipynb` dengan struktur modular sebagai berikut:\n'
    '- Fungsi `unsharp_mask()` untuk sharpening\n'
    '- Fungsi `apply_clahe()` untuk contrast enhancement\n'
    '- Fungsi `plot_comparison()` untuk visualisasi profesional\n'
    '- Pengecekan error untuk pemuatan file\n'
    '- Penyimpanan output JPEG kualitas tinggi ke dalam direktori `hasil/`',
    styles['BodyText']))

story.append(Paragraph('8. Evaluasi Hasil', styles['CustomHeading1']))
story.append(Paragraph(
    'Hasil pengolahan menunjukkan peningkatan visual yang signifikan. Gambar blur menjadi lebih tajam, dan citra kontras rendah menjadi lebih jelas dengan detail yang lebih baik. ' 
    'Hasil akhir tersimpan sebagai file `hasil_sharpen.jpg` dan `hasil_clahe.jpg`.',
    styles['BodyText']))

story.append(Paragraph('9. Visualisasi Hasil', styles['CustomHeading1']))
story.append(Paragraph('Berikut adalah perbandingan visual antara citra asli dan citra hasil pemrosesan:', styles['CustomBodyText']))

for title, path in INPUT_IMAGES:
    if os.path.exists(path):
        img = Image(path)
        img.drawHeight = 8 * cm
        img.drawWidth = 12 * cm
        story.append(img)
        story.append(Paragraph(title, styles['Caption']))
        story.append(Spacer(1, 10))
    else:
        story.append(Paragraph(f'Gambar tidak ditemukan: {path}', styles['BodyText']))
        story.append(Spacer(1, 10))

story.append(PageBreak())

story.append(Paragraph('10. Kesimpulan', styles['CustomHeading1']))
story.append(Paragraph(
    'Proyek ini berhasil mengimplementasikan pemrosesan citra digital yang efektif untuk meningkatkan kualitas gambar. ' 
    'Metode sharpening dan CLAHE memberikan hasil yang professional, menjaga detail sambil meningkatkan kontras secara adaptif.',
    styles['BodyText']))
story.append(Paragraph(
    'Rekomendasi: parameter clipping CLAHE dan kekuatan sharpening dapat dituning lebih lanjut sesuai karakteristik dataset untuk hasil yang optimal.',
    styles['BodyText']))

story.append(Paragraph('11. Referensi', styles['CustomHeading1']))
story.append(Paragraph(
    '- Rafael C. Gonzalez, Richard E. Woods, "Digital Image Processing"\n'
    '- OpenCV Documentation\n'
    '- NumPy Documentation\n'
    '- Matplotlib Documentation',
    styles['BodyText']))

if __name__ == '__main__':
    doc = SimpleDocTemplate(PDF_FILE, pagesize=A4,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40)
    doc.build(story)
    print(f'PDF report generated: {PDF_FILE}')

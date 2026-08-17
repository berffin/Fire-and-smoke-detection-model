# YOLO11 Yangın ve Duman Tespiti (Fire & Smoke Detection)

Bu proje, son teknoloji **YOLO11** modelini kullanarak gerçek zamanlı yangın ve duman tespiti yapmak amacıyla geliştirilmiştir. Sistem; fotoğraflar, videolar ve canlı kamera akışları üzerinde çalışabilmektedir.

## Model Performansı (Doğruluk Oranları)
Model, özel bir veri seti üzerinde eğitilmiş olup aşağıdaki mAP@0.5 (Ortalama Hassasiyet) skorlarını elde etmiştir:

*   **Duman (Smoke):** ~0.81 mAP (Yüksek başarı)
*   **Ateş (Fire):** ~0.60 mAP (Geliştirilmeye açık)
*   **Genel Ortalama:** ~0.71 mAP

> **Not:** Model, duman formlarını tanımada oldukça başarılıdır. Ateşin rengi ve şekli çok değişken olduğu için ateş tespitinde geliştirme çalışmaları (veri artırımı) devam etmektedir. İdeal kullanım için güven eşiği (confidence threshold) **0.39** olarak belirlenmiştir.
## Gelecek Planları (Roadmap)

Modelin mevcut performansını daha da ileriye taşımak için planlanan güncellemeler:
* **Ateş Veri Setinin Genişletilmesi:** Ateş sınıfındaki tespit başarısını (0.60 mAP) duman seviyesine çıkarmak için, veri setine gece/gündüz çekilmiş, farklı boyut ve renklerde daha fazla ateş/alev görseli eklenecek ve model yeniden eğitilecektir.
* **Negatif Örneklerin Eklenmesi:** Sis, bulut, gün batımı kızıllığı veya parlak ışıklar gibi modelin kafasını karıştırabilecek arka plan görselleri (background images) veri setine dahil edilerek yanlış alarmlar (false-positive) en aza indirilecektir.
## Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Depoyu Klonlayın:**
```bash
git clone [https://github.com/](https://github.com/)[KULLANICI_ADINIZ]/YOLO11-Fire-Smoke-Detection.git
cd YOLO11-Fire-Smoke-Detection

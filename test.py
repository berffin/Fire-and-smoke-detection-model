from ultralytics import YOLO

# Eğittiğiniz modelin ağırlık dosyasını (best.pt) yüklüyoruz
# Klasör yolunu kendi bilgisayarınızdaki yere göre güncelleyebilirsiniz
model = YOLO("runs\\detect\\Fire_Smoke_Detection\\yolo11_run_1-3\\weights\\best.pt")
#Modeli bir video veya kamera üzerinde test etmek için predict fonksiyonunu kullanıyoruz.
#Grafikten elde ettiğimiz ideal conf=0.39 ayarı tam olarak buraya yazılıyor!
results = model.predict(source="g.mp4", show=True, conf=0.39)

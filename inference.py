import cv2
from ultralytics import YOLO

# ==========================================
# 1. MODELİ LOAD ET (Ortak Adım)
# ==========================================
MODEL_PATH = r"C:\Users\tavan\OneDrive\Masaüstü\infodif\runs\detect\Fire_Smoke_Detection\yolo11_run_1-3\weights\best.pt"
print("Model yükleniyor...")
model = YOLO(MODEL_PATH)


def inference_on_image(image_path):
    print(f"{image_path} okunuyor...")
    # 2. Resmi Yükle
    img = cv2.imread(image_path)
    if img is None:
        print("Hata: Resim bulunamadı!")
        return

    # 3. Forward & Inference
    results = model(img, conf=0.39)
    
    # 4. Sonuçları Çiz
    annotated_img = results[0].plot()

    # 5. Göster
    cv2.imshow("Yangin ve Duman Tespiti - RESIM", annotated_img)
    cv2.waitKey(0) # Tuşa basana kadar bekle
    cv2.destroyAllWindows()


def inference_on_video(video_path):
    print(f"{video_path} başlatılıyor...")
    
    # 2. Videoyu Yükle (Kamera için video_path yerine 0 yazabilirsiniz)
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Hata: Video veya Kamera açılamadı!")
        return

    # Video akmaya devam ettiği sürece döngü çalışır
    while cap.isOpened():
        # Videodan tek bir kare (frame) oku
        success, frame = cap.read()
        
        if success:
            # 3. Forward & Inference (Sadece o anki kareyi ağdan geçir)
            results = model(frame, conf=0.39)
            
            # 4. Sonuçları Çiz
            annotated_frame = results[0].plot()
            
            # 5. Göster
            cv2.imshow("Yangin ve Duman Tespiti - VIDEO", annotated_frame)
            
            # Videonun akması için cv2.waitKey(1) kullanıyoruz. 
            # Klavyeden 'q' tuşuna basılırsa döngüyü kır (çık).
            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("Kullanıcı tarafından kapatıldı.")
                break
        else:
            print("Video bitti.")
            break

    # İşlem bitince belleği temizle ve pencereleri kapat
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    
    # Resim test etmek istiyorsanız bu satırı kullanın:
    # inference_on_image("test_resmi.jpg")
    
    # Video (veya mp4) test etmek istiyorsanız bu satırı kullanın:
    inference_on_video("2.mp4") 
    
    # Canlı web kameranızı test etmek isterseniz:
    # inference_on_video(0)
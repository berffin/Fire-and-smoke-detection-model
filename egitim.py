from ultralytics import YOLO

def train_fire_smoke_model():
    # 1. Başlangıç modelini (Pre-trained) yükle
    model = YOLO("yolo11n.pt") 

    print("Eğitim başlıyor... (Seçim yapabilmeniz için modeller her 10 epoch'ta bir kaydedilecek)")

    # 2. Modeli Eğit ve Ara Kayıtları (Checkpoint) Al
    results = model.train(
        data=r"YOLO_Hazir_Veriseti\data.yaml", 
        epochs=100, 
        imgsz=640,
        batch=16,
        device=0, 
        project="Fire_Smoke", 
        name="egitilmis_sn", 
        patience=20, 
        optimizer="auto",
        workers=0,
        
        # --- İŞTE EĞİTMENİNİZİN BAHSETTİĞİ ARA KAYIT (CHECKPOINT) AYARLARI ---
        save=True,          # Modeli diske kaydetme özelliğini aç (Varsayılan True'dur)
        save_period=10      # HER 10 EPOCH'TA BİR YENİ MODEL KAYDET
    )

    # 3. Modelin Doğruluğunu Test Et (Validation)
    metrics = model.val()
    
    print("-" * 50)
    print("Eğitim başarıyla tamamlandı!")
    print("Ara modelleriniz şu klasöre kaydedildi:")
    print(r"Fire_Smoke\egitilmis_sn\weights")

if __name__ == "__main__":
    train_fire_smoke_model()

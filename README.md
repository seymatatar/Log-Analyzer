# 📊 Simple Log Analyzer

<p align="center">
  <a href="#-english">English</a> | 
  <a href="#-turkish">Turkish</a>
</p>

---

## 🇺🇸 English

This project is a fundamental Python script designed to scan server log files (`server.log`), identify specific error types, and convert the analysis results into a professional, timestamped report.

### ✨ Features
* 🔍 **Error Detection:** Automatically identifies `ERROR`, `FAILED LOGIN`, `404`, and `WARNING` keywords.
* 📂 **Professional Reporting:** Saves analysis results in a structured format to `report.txt`.
* 🕒 **Timestamping:** Documents the exact time of analysis using the `datetime` library.

### 🚀 Installation & Usage
1. Clone the repository.
2. Place your `server.log` file in the same directory as the script.
3. Run the analyzer using the following command:
```bash
python log_analyzer.py
```

### 📂 File Structure
* `log_analyzer.py`: Main analysis script.
* `server.log`: Source data to be analyzed (must be provided by the user).
* `rapor.txt`: Result report created upon completion of the analysis.

### ⚖️ License
This project is provided under the **MIT License**.



# 📊 Simple Log Analyzer

## us Turkish

Bu proje, bir sunucu log dosyasını (`server.log`) tarayarak belirli hata türlerini ayırt eden ve analiz sonuçlarını tarih damgalı profesyonel bir rapor dosyasına dönüştüren temel bir Python scriptidir.

### ✨ Özellikler
* 🔍 **Hata Tespiti:** `ERROR`, `FAILED LOGIN`, `404` ve `WARNING` anahtar kelimelerini otomatik olarak tespit eder.
* 📂 **Profesyonel Raporlama:** Analiz sonuçlarını düzenli ve okunabilir bir formatta `rapor.txt` dosyasına kaydeder.
* 🕒 **Zaman Damgası:** `datetime` kütüphanesini kullanarak her analiz raporuna işlem zamanını ekler.

### 🚀 Kurulum ve Kullanım
Uygulamayı çalıştırmak için şu adımları izleyin:

1. Projeyi bilgisayarınıza klonlayın veya dosyaları indirin.
2. Analiz edilecek `server.log` dosyanızın script ile aynı klasörde olduğundan emin olun.
3. Terminal veya komut istemcisi üzerinden şu komutu çalıştırın:
```bash
python log_analyzer.py
```

### 📂 Dosya Yapısı
* `log_analyzer.py`: Ana analiz scripti.
* `server.log`: Analiz edilecek kaynak veri (Kullanıcı tarafından sağlanmalıdır).
* `rapor.txt`: Analiz tamamlandığında oluşturulan sonuç raporu.

### ⚖️ Lisans
Bu proje **MIT Lisansı** altında sunulmaktadır.

# Simple Log Analyzer

Bu proje, bir sunucu log dosyasını (`server.log`) tarayarak hata türlerini ayırt eden ve analiz sonuçlarını tarih damgalı bir rapor dosyasına dönüştüren temel bir Python scriptidir.

## Özellikler
* `ERROR`, `FAILED LOGIN` , `404` ve `WARNING` hatalarını tespit eder.
* Sonuçları `rapor.txt` dosyasına profesyonel bir formatta kaydeder.
* `datetime` kütüphanesi ile analiz zamanını belgeler.

## Kurulum
1. Projeyi klonlayın.
2. Aynı klasöre `server.log` dosyanızı ekleyin.
3. `python log_analyzer.py` komutuyla çalıştırın.

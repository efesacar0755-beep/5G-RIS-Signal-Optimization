# 5G Akıllı Yansıtıcı Yüzey (RIS) Temel Sinyal Gücü Hesaplayıcı
# Hazırlayan: Halit Efe Sacar - 1. Sınıf Elektrik-Elektronik Mühendisliği

def yansima_gucu_hesapla(baz_istasyonu_gucu_dbm, mesafe_m, yuzey_turu):
    """
    Sinyalin çarptığı yüzeye göre hedefe ulaşan kalan sinyal gücünü (dBm) hesaplar.
    Basitleştirilmiş serbest uzay kayıp modeli ve yüzey kazancı baz alınmıştır.
    """
    # Mesafeye bağlı temel kayıp (Basitleştirilmiş model: her 10 metrede -5 dBm kayıp)
    mesafe_kaybi = (mesafe_m / 10) * 5 
    
    if yuzey_turu == "Beton Duvar":
        # Beton duvar sinyali rastgele dağıtır ve büyük oranda soğurur (Örn: -15 dBm kayıp)
        yuzey_etkisi = -15
    elif yuzey_turu == "RIS Paneli":
        # RIS (Akıllı Yüzey) sinyali soğurmaz, hedefe odaklar ve pasif kazanç sağlar (Örn: +10 dBm kazanç)
        yuzey_etkisi = 10
    else:
        yuzey_etkisi = 0

    hedefe_ulasan_guc = baz_istasyonu_gucu_dbm - mesafe_kaybi + yuzey_etkisi
    return hedefe_ulasan_guc

# --- Senaryo Analizi ---
# Baz istasyonundan çıkan ilk güç (Örn: 40 dBm) ve engelin arkasındaki kullanıcıya toplam mesafe (50m)
iletilen_guc = 40 
toplam_mesafe = 50 

# 1. Durum: Sinyal standart bir binaya çarpıp yansıyor (Multipath paraziti)
standart_yansima = yansima_gucu_hesapla(iletilen_guc, toplam_mesafe, "Beton Duvar")

# 2. Durum: Sinyal Huawei RIS paneli kaplı bir yüzeye çarpıp yansıyor (Odaklanmış sinyal)
ris_yansima = yansima_gucu_hesapla(iletilen_guc, toplam_mesafe, "RIS Paneli")

# Çıktılar
print("--- 5G Sinyal Yansıması ve RIS Optimizasyonu Analizi ---")
print(f"Standart Beton Duvar Yansıması ile Hedefe Ulaşan Güç: {standart_yansima} dBm")
print(f"RIS (Akıllı Yüzey) Yansıması ile Hedefe Ulaşan Güç: {ris_yansima} dBm\n")

# Mühendislik Yorumu
fark = ris_yansima - standart_yansima
print("--- SONUÇ ---")
print(f"RIS teknolojisi, yansımaları dezavantajdan avantaja çevirerek sinyal gücünde {fark} dBm'lik devasa bir iyileşme sağlamıştır.")
print("Bu sistem, ekstra enerji harcamadan kör noktalardaki kapsama alanını genişletir.")

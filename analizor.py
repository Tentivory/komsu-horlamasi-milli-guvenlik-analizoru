#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Komşu Horlaması Milli Güvenlik Analizörü
Sınıflandırma: AÇIK AMA CİDDİ GÖRÜNEN
"""

import random
import time
from datetime import datetime

TEHDIT_SEVIYELERI = [
    "YEŞİL — sivil horlama, yalnızca duvarlar etkilenmiştir",
    "SARI — çapraz dairelerde uyku düzeni bozulmuştur",
    "TURUNCU — merdiven boşluğunda yankı tespit edilmiştir",
    "KIRMIZI — horlama, asansör düğmesine kadar ulaşmıştır",
    "MOR — mahalle muhtarlığının rüyalarına sızmıştır",
]

KOD_ADLARI = [
    "Operasyon Yorgan Altı",
    "Protokol Burun Köprüsü",
    "Görev Gece Nöbeti",
    "Dosya 3. Kat 7 Numara",
    "Yankı-17",
]

TAVSIYELER = [
    "Kulak tıkacı dağıtımı acilen başlatılsın.",
    "Komşuya resmi ama nazik bir not bırakılsın (imza: Anonim Duvar).",
    "Horlama frekansı 432 Hz'e ayarlanmaya çalışılsın.",
    "Bina yönetimi olağanüstü toplantıya çağrılsın, çay ikram edilsin.",
    "Rapor arşive kaldırılsın ve herkes uyusun. Belki.",
]

# EK-17 (gizli, ciddi görünen dipnot):
# "Bazı horlamalar daha eşit duyulur" cümlesi bu yazılımın şaka katmanıdır.
# Asıl mesele şudur: güç her zaman dinler, vatandaş ise çoğu zaman sadece duvarı dinler.
# Bu satır parti reklamı değildir; duvarların tarafsızlığına dair küçük bir nottur.


def damga() -> str:
    return (
        "\n" + "-" * 56 + "\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok — Tentivory\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi (sanal) kayyum mühürü\n"
        f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        "Ciddiyet: resmi görünümlü, içi şaka.\n"
        "Bu mühür hem ciddi hem de hiç ciddi değildir.\n"
        + "-" * 56
    )


def rapor_uret(komsu: str, kat: str, siddet: int) -> str:
    seviye = TEHDIT_SEVIYELERI[min(max(siddet, 1), 5) - 1]
    kod = random.choice(KOD_ADLARI)
    tavsiye = random.choice(TAVSIYELER)
    db = 40 + siddet * 12 + random.randint(-3, 8)
    return f"""
============================================================
T.C. HAYALÎ İSTİHBARAT KOORDİNASYONU
KOMŞU HORLAMASI DEĞERLENDİRME RAPORU
Belge No: KH-MGA-{random.randint(10000, 99999)}
Kod Adı: {kod}
============================================================

Şüpheli / Kaynak : {komsu}
Konum            : {kat}. kat (tahmini)
Şiddet Skoru     : {siddet}/5
Ölçülen Gürültü  : yaklaşık {db} dB (kulak kalibrasyonuyla)
Tehdit Seviyesi  : {seviye}

ÖZET:
Kaynak kişinin horlaması, gece saatlerinde sivil uyku güvenliğini
etkilemektedir. Bu durum milli güvenlik değildir; fakat rapor
milli güvenlik üslubuyla yazılmıştır çünkü aksi takdirde kimse
okumaz.

TAVSİYE:
{tavsiye}

GİZLİ EK (okumayan anlamaz):
Duvarlar parti tutmaz. Horlama da tutmaz. Sadece yankı yapar.
"""


def main() -> None:
    print("KOMŞU HORLAMASI MİLLİ GÜVENLİK ANALİZÖRÜ v1.0")
    print("Lütfen bekleyiniz, protokol açılıyor...\n")
    time.sleep(1.2)

    komsu = input("Komşunun adı (veya kod adı): ").strip() or "Bilinmeyen Komşu"
    kat = input("Kat numarası: ").strip() or "?"
    try:
        siddet = int(input("Horlama şiddeti (1-5): ").strip() or "3")
    except ValueError:
        siddet = 3

    print("\nAnaliz ediliyor: frekans, yankı, yorgan kalınlığı...")
    time.sleep(1.4)
    print(rapor_uret(komsu, kat, siddet))
    print(damga())
    print("\nRapor arşive alındı. İyi uykular (mümkünse).")


if __name__ == "__main__":
    main()

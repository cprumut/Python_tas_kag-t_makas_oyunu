import random

def tas_kagit_makas_UMUT_CAN_CAPAR():
    # Oyun Tanıtımı
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyun kuralları: Taş makası yener, Makas kağıdı yener, Kağıt taşı yener.")
    print("İlk iki turu kazanan oyunu kazanır.")

    while True:
        # Oyun Kurulumu
        secenekler = ['taş', 'kağıt', 'makas']
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0

        # Oyunun Ana Döngüsü
        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            print("\nYeni bir tur başlıyor...")
            print(f"Şu ana kadar oyuncu: {oyuncu_galibiyetleri} - Bilgisayar: {bilgisayar_galibiyetleri}")

            # Turların Döngüsü
            oyuncu_secimi = input("Lütfen seçiminizi yapın (taş, kağıt, makas): ").lower()
            while oyuncu_secimi not in secenekler:
                oyuncu_secimi = input("Geçersiz seçim! Lütfen tekrar deneyin (taş, kağıt, makas): ").lower()

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            # Sonuçları belirleme
            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
                 (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kağıt') or \
                 (oyuncu_secimi == 'kağıt' and bilgisayar_secimi == 'taş'):
                print("Oyuncu kazandı!")
                oyuncu_galibiyetleri += 1
            else:
                print("Bilgisayar kazandı!")
                bilgisayar_galibiyetleri += 1

        # Oyun Galibini Belirleme
        if oyuncu_galibiyetleri == 2:
            print("\nTebrikler! Oyunu kazandınız!")
        else:
            print("\nBilgisayar oyunu kazandı. Üzgünüm!")

        # Devam Etme İsteği
        tekrar_oyna = input("\nBaşka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        if tekrar_oyna != 'evet':
            print("Oyun bitti. Tekrar görüşmek üzere!")
            break

# Oyunu başlat
tas_kagit_makas_UMUT_CAN_CAPAR()

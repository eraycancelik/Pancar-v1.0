while True:
    ilk_sayı = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
        break  # Hata olmadan işlem başarılı, döngüden çık
    except ValueError:
        print("Lütfen sadece sayı girin!")  # Hata olduğunda mesaj ver ve döngüyü tekrar döndür
        continue  # Yeniden kullanıcı girişi almak için döngüyü baştan döndür
import random

tur = int(input("KAÇ TUR OYNANSIN: "))
turlar = 0

güncelPuanlar = {}

while turlar < tur:
    A = ['♠', '♣', '♥', '♦']
    B = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deste = []
    for i in A:
        for j in B:
            deste.append(i+j)

    oyuncular = {}
    oyuncu_sira = ['oyuncu1', 'oyuncu2', 'oyuncu3', 'oyuncu4']
    
    for i in range(4):
        oyuncular.setdefault(oyuncu_sira[i], {}.fromkeys(A))

    for oyuncu in oyuncular:
        for i in A:
            oyuncular[oyuncu][i] = []
        for i in range(13):
            kart = random.choice(deste)
            oyuncular[oyuncu][kart[0]].append(kart[1:])
            deste.remove(kart)

    print("\nDAĞITILAN KARTLAR:")
    for oyuncu in oyuncular:
        print(oyuncu + ":")
        for karttip in oyuncular[oyuncu]:
            oyuncular[oyuncu][karttip].sort(key=B.index)
            print(karttip, oyuncular[oyuncu][karttip])

    tahminler = {}
    for i in range(4):
        tahmin = int(input(f"{oyuncu_sira[i]} için kaç el kazanır tahimi: "))
        tahminler.setdefault(oyuncu_sira[i],tahmin)

    print("\nOYUN BAŞLADI...")
    oyun_skor = dict()
    macaAtildi = False
    sira = random.randrange(4)

    for el in range(13):  # 13 el oynanacak
        print(str(el+1) + ". el:")
        oynayan = 0
        oynanan_kartlar = []  # bu liste içine kimin hangi kartı attığı yazılacak
        while oynayan < 4:
            oyuncu = oyuncu_sira[sira]
            if oynayan == 0:  # ilk kart atacak oyuncu ise kart tipi belirlenecek (rastgele)
                while True:
                    if macaAtildi:  # Maça önceki bir elde koz olarak kullanıldı ise oyuncu Maça ile başlayabilir
                        print(f"{oyuncu} ADLI DESTENİZ:",oyuncular[oyuncu_sira[sira]])
                        while True:
                            tip = input("ATACAĞINIZ KART TİPİNİ SEÇİN\n♠ için 1\n♣ için 2\n♥ için 3\n♦ için 4\n")        
                            if tip == "1":
                                kart_tipi = "♠"
                                break
                            elif tip == "2":
                                kart_tipi = "♣"
                                break
                            elif tip == "3":
                                kart_tipi = "♥"
                                break
                            elif tip == "4":
                                kart_tipi = "♦"
                                break
                            else:
                                print("KART TİPNİ DOĞRU SEÇİNİZ")
                    else:  # Maça önceki bir elde koz olarak kullanılmadı ise diğer üç kart tipinden atabilir
                        print(f"{oyuncu} ADLI DESTENİZ:",oyuncular[oyuncu_sira[sira]])
                        while True:
                            tip = input("ATACAĞINIZ KART TİPİNİ SEÇİN\n♣ için 1\n♥ için 2\n♦ için 3\n")    
                            if tip == "1":
                                kart_tipi = "♣"
                                break
                            elif tip == "2":
                                kart_tipi = "♥"
                                break
                            elif tip == "3":
                                kart_tipi = "♦"
                                break
                            else:
                                print("KART TİPNİ DOĞRU SEÇİNİZ")
                    if len(oyuncular[oyuncu_sira[sira]][kart_tipi]):  # o tipte kartı yoksa döngü devam edecek
                        break
                    else:
                        print("ATMAK İSTEDİĞİNİZ TİPTE KARTINIZ YOK")
                # oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())  # o tipteki en büyük kartı atıyor
                # NOT: Oyuncunun o tipteki en büyük kartı atması çoğu durumda mantıklı değil. Rastgele olarak seçilmesi veya
                # en küçüğü atmak da mantıklı olmaz. Oyuncunun mantıklı bir kart atmasını sağlamak için birçok ilave kontrol
                # eklenmesi gerekir (Daha önce 'A' çıktı ise 'K' ile başlamak mantıklı olabilir vb.). Bu programda o elin
                # ilk kartı atılırken de, sonraki kartlar için de mantıklı olmasına yönelik kontroller bulunmamaktadır.
                '''Burada mantıklı kart atma işlemini kendi atacağımız kartı seçerek yapmayı tercih ettim'''
                
                while True:
                    print(oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi])
                    atılan_kart = input(f"{kart_tipi} TİPİNDEN ATACAĞINIZ KARTI SEÇİN (ör:'A','K','9'): ").upper()    
                    if atılan_kart in oyuncular[oyuncu][kart_tipi]:
                        oyuncu_kart = (oyuncu, kart_tipi, atılan_kart)
                        oyuncular[oyuncu][kart_tipi].remove(atılan_kart)
                        break
                    else:
                        print("ELİNİZDEKİ KARTLARDAN ATMAYA ÇALIŞIN")
            else:  # diğer oyuncular ilk oyuncunun belirlediği kart tipinde kart atacak
                if len(oyuncular[oyuncu][kart_tipi]):  # o kart tipinde kartı varsa en büyük olanı atacak
                    while True:
                        print(oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi])
                        atılan_kart = input(f"{kart_tipi} TİPİNDEN ATACAĞINIZ KARTI SEÇİN (ör:'A','K','9'): ").upper()
                    
                        if atılan_kart in oyuncular[oyuncu][kart_tipi]:
                            oyuncu_kart = (oyuncu, kart_tipi, atılan_kart)
                            oyuncular[oyuncu][kart_tipi].remove(atılan_kart)
                            break
                        else:
                            print("ELİNİZDEKİ KARTLARDAN ATMAYA ÇALIŞIN")
                elif len(oyuncular[oyuncu]['♠']):  # o kart tipinde kartı yoksa en küçük maça kartını atacak
                    oyuncu_kart = (oyuncu, '♠', oyuncular[oyuncu]['♠'].pop(0))
                    macaAtildi = True  # Maça koz olarak oynandığı için sonraki ellerde doğrudan Maça atılabilecek
                else:  # maça kartı da yoksa, diğer 2 tipin hangisinde daha çok kart varsa en küçük kartı atacak
                    kart_tipleri = A[1:].copy()  # maça hariç diğer 3 kart tipi kopyalandı
                    if kart_tipi != '♠':  # oynanan kart tipi maça değilse
                        kart_tipleri.remove(kart_tipi)  # oynanan kart tipi de oyuncuda olmadığı için silindi
                    if len(oyuncular[oyuncu][kart_tipleri[0]]) > len(oyuncular[oyuncu][kart_tipleri[1]]):
                        oyuncu_kart = (oyuncu, kart_tipleri[0], oyuncular[oyuncu][kart_tipleri[0]].pop(0))
                    else:
                        oyuncu_kart = (oyuncu, kart_tipleri[1], oyuncular[oyuncu][kart_tipleri[1]].pop(0))
            print(oyuncu_kart[0], oyuncu_kart[1] + oyuncu_kart[2])
            oynanan_kartlar.append(oyuncu_kart)
            oynayan += 1
            sira += 1
            if sira >= 4:
                sira -= 4
        # atılan 4 karta göre eli kazananı bulma:
        en_buyuk = oynanan_kartlar[0]   # ilk atılanı en büyük kart kabul et
        for kart in oynanan_kartlar[1:]:
            if kart[1] == en_buyuk[1] and B.index(kart[2]) > B.index(en_buyuk[2]):
                en_buyuk = kart  # en büyük ile aynı kart tipinde daha büyük atıldı ise en büyük kart kabul et
            elif en_buyuk[1] != '♠' and kart[1] == '♠':
                en_buyuk = kart  # en büyük maça değilken maça atıldı ise en büyük kart kabul et
        print("eli kazanan:", en_buyuk[0])
        sira = oyuncu_sira.index(en_buyuk[0])
        oyun_skor[en_buyuk[0]] = oyun_skor.setdefault(en_buyuk[0], 0) + 1

    print("SKOR:", oyun_skor)  # oyuncuların kaçar el adığını gösterir (gerçek kurallara göre bir puanlama sistemi yok)
    print("TAHMİNLER:",tahminler)
    
    puanlar = {}

    for kisi,win in oyun_skor.items():
        if win >= tahminler[kisi]:
            puan = tahminler[kisi] * 10 + (win - tahminler[kisi])
            puanlar.setdefault(kisi,puan)
            güncelPuanlar.setdefault(kisi,0)
        else:
            puan = tahminler[kisi] * (-10)
            puanlar.setdefault(kisi,puan)
            güncelPuanlar.setdefault(kisi,0)
    for x,y in puanlar.items():
        gnclPuan = y + güncelPuanlar[x]
        güncelPuanlar.update({x:gnclPuan})

    print("PUAN TABLOSU:",güncelPuanlar)
    turlar += 1
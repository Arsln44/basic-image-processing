import cv2
import numpy as np

# ↓kameraya erisim sagladik
goruntu = cv2.VideoCapture(0)
while True:
    # ↓ ret görüntünün başarılı şekilde alınıp alınmadığını belirten bir değerdir.
    # ↓ frame alınan kareyi temsil ediyor. 
    ret, frame = goruntu.read() 
    
    # ↓ renk uzayini RGB den HSV'ye donsturduk.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # ↑ BGR2HSV donusturme kodudur 2 yerine 1 koysaydik gray tonlamali olurdu.
    
    # ↓ kimizi renk tonlarinin alt,ust sinirlarini tanimlayacagiz
    low_red = np.array([0,100,100])
    up_red = np.array([10,255,255])
    # ↑ HSV ton,doyma,parlaklik olarak dizi degerlerini belirledik.
    
    # ↓ maskeleme islemi gerceklestiriyoruz.
    mask = cv2.inRange(hsv, low_red, up_red)
    # ↑ cv2.inRange belirli bir aralıktaki degerlere sahip pikselleri içeren bir maske olusturur.
    
    # ↓ goruntude belirttigimiz rengi gostermek icin maskeyi uyguluyoruz.
    result = cv2.bitwise_and(frame, frame,mask=mask)
    # ↑ cv2.bitwise_and() fonksiyonu iki görüntü arasında bit düzeyinde "ve" işlemi gerçekleştirir.
    
    # ↓ olusturulan goruntuleri pencerede gosterdik.
    cv2.imshow("orijinal goruntu",frame)
    cv2.imshow("maskelenmis goruntu",result)
    
    # ↓ cikis icin 'q' tusuna basilirsia donguyu kir.
    if cv2.waitKey(1) & 0xFF==ord("q"):
        # ↑ 0xFF ascii q degeridir tusu kontrol eder ve eşitse true döndürür.
        break
    
goruntu.release() # kamera baglantisini kapattik.
cv2.destroyAllWindows() # tum pencereleri kapattik.Q
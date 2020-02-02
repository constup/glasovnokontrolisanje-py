import speech_recognition as sr
import os 
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source: # Koristi podrazumevni mikrofon za izvor zvuuka
        r.adjust_for_ambient_noise(source) # Slusaj jednu sekundu za kalibraciju jacine mikrofona i okolnu buku (u slucaju da buka nije konstantna, speech_recognition detektovace i probace da je ocita). 
        audio = r.listen(source) # Sada kada slušamo, prag je već postavljen na dobru vrednost i možemo pouzdano  odmah uhvatiti govor.
        print("") # Dodavanje novog reda da bi znali da je mikrofon pokupio zvuk.
        try:
            odgovor =( r.recognize_google(audio , language="sr-RS")) # Pokusati prepoznati izgovoreno, i stavljati u string odgovor. 
            print(odgovor) # Stampaj odgovor.
            return str(odgovor) 
            
        except Exception as e :
            if str(e) == "": 
                print(e)
            else:
                print("Greška!")
                print(str(e)) # Stampanje greske 
def prvopokretanje(): # Koristimo ovo kako bi ocitali i obrisali greske koje se javljaju prilikom pokretanja.
    r=sr.Recognizer()
    with sr.Microphone() as source: # Koristi podrazumevni mikrofon za izvor zvuuka
       
        os.system('clear')
if __name__ == "__main__":
    main()

import speech_recognition as sr
 
def main():
    
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 


        print("#CEKAM KOMANDU#")
 
        audio = r.listen(source)
 
        print("")
        try:
            odgovor =( r.recognize_google(audio , language="sr-RS"))
           
            odgovor2 = odgovor.lower()
            odgovor3 = odgovor2.replace(" ","_")
            print(odgovor3)
            return odgovor3
            
        except Exception :
            print("Nisam uspeo prepoznati.")
        
 
if __name__ == "__main__":
    main()

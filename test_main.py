import unittest
import main
import os
import listen
import type
lokacija = (os.path.dirname(os.path.realpath(__file__)))
komande= lokacija + "/" + 'komande.cfg'
reci = lokacija + '/' + 'reci.cfg' 
class TestMain (unittest.TestCase):

    def test_nadji_rec(self):
        self.assertEqual(main.nadji_rec('otvori_chrome'), True)
        self.assertEqual(main.nadji_rec('otvori_firefox'), True)
        self.assertEqual(main.nadji_rec('enter'), True)

    def test_nadji_red(self):
        with open(reci) as myFile:                 
            for num, line in enumerate(myFile, 1):
                if '!NE BRISI OVU LINIJU,SLUZI ZA TESTIRANJE!' in line:                   
                    self.assertEqual(main.nadji_red('!NE BRISI OVU LINIJU,SLUZI ZA TESTIRANJE!'), num)
          
    def test_nadji_komandu(self):
        f=open(komande)             
        linija=f.readlines() 
        linija2 = linija[0]
        linija2 = linija2.strip('\n')                
        linija2 = linija2.strip('\t')      
        self.assertEqual(main.nadji_komandu( 0 ), '!NE BRISI OVU LINIJU,SLUZI ZA TESTIRANJE!' )

    def test_izvrsi_komandu(self):
        self.assertEqual(main.izvrsi_komandu('xdotool'), True )
    def test_proveri_fajlove(self):
        self.assertEqual(main.proveri_fajlove(), True )

    def test_main(self):
        self.assertEqual(main.proveri_fajlove(), True )

    def test_listen_prvopokretanje(self):
        self.assertEqual(listen.prvopokretanje(), True)
    
if __name__ == '__main__':
    unittest.main()

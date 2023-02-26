

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('gurbanguli','agildasaev')        
        self.assertEqual(name, 'Gurbanguli Agildasaev')
    
    def test_otasining_ismi(self):
        name=get_full_name('hasan', 'husanov','olimovich')
        self.assertEqual(name, 'Hasan Olimovich Husanov')



from circle import doira_yuzi,doira_perimetri

class CirleTest(unittest.TestCase):
    def test_doira_yuzi(self):
        yuz=doira_yuzi(28)
        self.assertAlmostEqual(yuz, 2463.00656)
        
    def test_doira_perimetri(self):
        perimetr=doira_perimetri(28)
        self.assertAlmostEqual(perimetr, 175.92904)
        
unittest.main()        















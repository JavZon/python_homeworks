# test.py
import unittest
from uy_ishi_test import katta_harf_qil,kattasini_top,juft_son_top

# class KattaHarf_Test(unittest.TestCase):
#     def test_katta_harf(self):
#         natija=kattasini_top(5, 18, 85)
#         self.assertEqual(natija, 85)
        

class JuftSon_test(unittest.TestCase):
    def test_juft_son(self):
        juft=juft_son_top(84)
        self.assertEqual(juft, 84)

      
    
juft=juft_son_top(52,35,14,25,19)
print(juft)























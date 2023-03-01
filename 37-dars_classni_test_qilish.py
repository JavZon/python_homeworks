
import unittest
from CarTest import Car,car1


# class CARTEST(unittest.TestCase):
#     def test_car_create(self):
#         self.assertIsNotNone(car1.producer)
#         self.assertIsNotNone(car1.model)
#         self.assertIsNotNone(car1.color)
#         self.assertIsNotNone(car1.year)
#         self.assertIsNotNone(car1.price)
#         self.assertEqual(car1.get_km(), 0)

       

class CAR_TEST(unittest.TestCase):
    def setUp(self):
        producer="Mitsubishi"
        model='watashiwas'
        color='black'
        year=2023
        self.price=45000
        self.km=1200
        self.avto1=Car(producer,model,color,year)
        self.avto2=Car(producer,model,color,year,price=self.price)
        
    def test_crash(self):
        self.assertIsNotNone(self.avto1.producer)
        self.assertIsNotNone(self.avto1.model)
        
        self.assertIsNone(self.avto1.price)
        
        self.assertEqual(self.price, self.avto2.price)
        
unittest.main()

















        

                
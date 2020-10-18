import unittest
from moonlander import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 9), 1.296)
   def test_update_acc3(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 5), 0)   
   def test_update_alt1(self):
      self.assertAlmostEqual(updateAltitude(1300, 500, 1.296), 1800.648)
   def test_update_alt2(self):
      self.assertAlmostEqual(updateAltitude(400, 356, -1.62), 755.19)
   def test_update_alt3(self):
      self.assertEqual(updateAltitude(0, 0, -1.62), None)
   def test_update_vel1(self):
      self.assertAlmostEqual(updateVelocity(9, 1800.648), 1809.648)
   def test_update_vel3(self):
      self.assertAlmostEqual(updateVelocity(5, 755.19), 760.19) 
   def test_update_vel2(self):
      self.assertEqual(updateVelocity(3, 400), 403)
   def test_update_fuel1(self):
      self.assertEqual(updateFuel(470,5), 465)
   def test_update_fuel2(self):  
      self.assertEqual(updateFuel(500,9), 491)
   def test_update_fuel3(self):  
      self.assertEqual(updateFuel(78,8), 70)  
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

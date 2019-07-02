# TESTING FILE 'farm.py'

import unittest as ut
from farm import Pets as pt
from farm import FarmAnimals as fa

class TestFarm(ut.TestCase):

    # Setting up class instances
    def setUp(self):
    
        # Creaing class instances
        self.pet1 = pt('cat', 3, 'Filemon')
        self.pet2 = pt('dog', 1, 'Ghost')
        self.ani1 = fa('cow', 7, 'Krasula', 'moo')
        self.ani2 = fa('pig', 9, 'Pinky', 'oink')

        # Setting other parameters
        self.pet1.hunger = 65
        self.ani1.hunger = 100

        print('Set Up')

    # Testing hungry method
    def test_hungry(self):
        result = pt.hungry(self.pet1)
        self.assertEqual(result, 'Your animal is hungry! You should feed your cat !')

        result = pt.hungry(self.ani1)
        self.assertEqual(result, 'Your cow is full and happy :)')

        print('Hungry method test')

    # Testing hunger setter
    def test_hunger(self):
        self.pet2.hunger = 121
        self.assertEqual(self.pet2.hunger, 121)

        print('Hunger setter method test')

    # Testing name setter
    def test_name(self):
        self.ani2.name = 'Friday'
        self.assertEqual(self.ani2.name, 'Friday')

        self.pet1.name = 'Crow'
        self.assertEqual(self.pet1.name, 'Crow')

        print('Name setter method test')

    # Animal sound method test
    def test_makeSound(self):
        self.assertEqual(self.ani1.makeSound(), 'cow does moo!')
        self.assertEqual(self.ani2.makeSound(), 'pig does oink!')

        print('makeSound method test')

    # Animal anger test
    def test_anger(self):
        self.assertFalse(self.ani1.anger)

        print('Anger method test')

    # Alternative constructor test
    def test_from_file(self):
        self.pet3 = pt.from_file('pet_info.txt')
        self.assertEqual(self.pet3.kind, 'cat')
        self.assertEqual(int(self.pet3.age), 2)
        self.assertEqual(self.pet3.name, 'Snowball')

        print('Constructor - from_file - test')


if __name__ == '__main__':
    ut.main()
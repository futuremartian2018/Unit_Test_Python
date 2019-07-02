# Pets&Animals - Unit Test

This programs aim is to test simple class methods of two classes - Pets and FarmAnimals.

# Pets&Animals

A single pet consists of its kind (species), name, age and information about how hungry it is.

![image](https://user-images.githubusercontent.com/37414943/60544053-324a0b00-9d18-11e9-8ecb-a2ae46acd4d4.png)

One can also create an instance of a class by reading information about pets from a text file.

![image](https://user-images.githubusercontent.com/37414943/60544171-763d1000-9d18-11e9-934b-c505e47ee852.png)

Class FarmAnimals inherits form Pets, while adding an additional field which contains a sound, that a particualar animal makes.

![image](https://user-images.githubusercontent.com/37414943/60544537-48a49680-9d19-11e9-9ed4-579815aab20a.png)

# Test

In order to test classes mentioned above and their methods we create another file, which contains testing methods.
Testing requires importing unittest library as well as classes that will be tested. Inside class TestFarm
we set up class instances and their parameters befeore each tests execution.

![image](https://user-images.githubusercontent.com/37414943/60544786-cd8fb000-9d19-11e9-9ec2-e9df786f81ee.png)

After each method is tested information about its execution is printed to console.

![image](https://user-images.githubusercontent.com/37414943/60545285-04b29100-9d1b-11e9-9d53-1b3837f934e1.png)

After running the test we get an information about how many tests took place and if there were any issues with our code.

![image](https://user-images.githubusercontent.com/37414943/60547001-e8b0ee80-9d1e-11e9-8bdc-dc9d2c183aba.png)

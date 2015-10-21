import unittest
import mock 

from animals import animal

class animal_unittest(unittest.TestCase):

    def setUp(self):
        self.dog_test = animal('Wut')
        self.dog_test.add_trick('Sit')
    
    @mock.patch('animals.os')

    def test_dempty_method(self, blah):
        self.dog_test.dempty("/tmp_test")
        blah.path.exists.assert_called_with("/tmp_test")
    
    @mock.patch('animals.os')

    def test_dempty_list_retrival(self, blah):
	blah.listdir.return_value = []
	self.assertEqual(self.dog_test.dempty('/tmp_test'), True) 

    def test_dog_class_name_init(self):
        self.assertEqual(self.dog_test.name, 'Wut', 'Correctly set name')

    def test_dog_tricks_array_type(self):
        self.assertIs(type(self.dog_test.tricks), list)

    def test_dog_class_prints_tricks(self):
        self.assertEqual(hasattr(self.dog_test, 'print_tricks'), True)

    def test_dog_class_has_add_tricks(self):
        self.assertEqual(hasattr(self.dog_test, 'add_trick'), True)

    def test_dog_class_it_adds_tricks(self):
        self.assertEqual(self.dog_test.tricks, ['Sit'], 'the trick was not added')

    def test_zdog_class_method_print_tricks_works(self):
        self.assertEqual(self.dog_test.print_tricks(), ['Sit'], 'Is not printing!')

if __name__ == '__main__':
    unittest.main()

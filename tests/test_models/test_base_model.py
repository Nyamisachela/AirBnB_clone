import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test instance of the BaseModel class, its methods and properties"""

    @classmethod
    def setUpClass(cls):
        """Setup test self.bm.ct as a class attribute"""
        cls.bm = BaseModel()

    def test_init(self):
        """Test for proper self.bm.ct initialization"""
        self.assertIsInstance(self.bm, BaseModel)
        self.assertEqual(self.bm.__class__.__name__, 'BaseModel')

    def test_val_id(self):
        self.assertIsNotNone(self.bm.id)

    def test_typ_id(self):
        self.assertIsInstance(self.bm.id, str)

    def test_len_id(self):
        self.assertEqual(len(self.bm.id), 36)

    def test_def_name(self):
        self.assertIsNone(self.bm.name)

    def test_default_num(self):
        self.assertIsNone(self.bm.my_number)

    def test_def_ts(self):
        self.assertIsNot(self.bm.created_at, None)
        self.assertIsNot(self.bm.updated_at, None)

    def test_eq_ts(self):
        self.assertEqual(self.bm.created_at, self.bm.updated_at)

    def test_typ_ts(self):
        self.assertIsInstance(self.bm.created_at, datetime.datetime)
        self.assertIsInstance(self.bm.updated_at, datetime.datetime)

    def test_name_val(self):
        v_name: str = "Test Name"
        self.bm.name = v_name
        self.assertEqual(self.bm.name, v_name)
        self.assertIsInstance(self.bm.name, str)

    def test_num_val(self):
        v_number: int = 999
        self.bm.my_number = v_number
        self.assertEqual(self.bm.my_number, v_number)
        self.assertIsInstance(self.bm.my_number, int)

    def test_save(self):
        self.bm.save()
        self.assertNotEqual(self.bm.created_at, self.bm.updated_at)
        self.assertIsInstance(self.bm.updated_at, datetime.datetime)

    def test_typ_str(self):
        self.assertIsInstance(self.bm.__str__(), str)

    def test_val_str(self):
        v_expected = "[{}] ({}) {}".format(
            self.bm.__class__.__name__,
            self.bm.id,
            str(self.bm.__dict__)
        )
        self.assertEqual(self.bm.__str__(), v_expected)

    def test_to_dict_typ(self):
        self.assertIsInstance(self.bm.to_dict(), dict)

    def test_vals_to_dict(self):
        v_dict = {
            '__class__': 'BaseModel',
            'id': self.bm.id,
            'name': self.bm.name,
            'my_number': self.bm.my_number,
            'created_at': self.bm.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'updated_at': self.bm.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        }
        self.assertEqual(self.bm.to_dict(), v_dict)




if __name__ == '_main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBaseModel)
    verbosity = 2
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

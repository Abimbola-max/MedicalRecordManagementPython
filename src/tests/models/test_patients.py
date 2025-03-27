import unittest

from src.data.models.patient import Patient
from src.data.repositories.patients import Patients


class MyPatientsTestCase(unittest.TestCase):

    def setUp(self):
        self.patients = Patients()
        self.patients.collection.delete_many({})

    def tearDown(self):
        self.patients.collection.delete_many({})

    def test_that_patients_details_can_be_saved(self):
        self.assertEqual(0,self.patients.count())
        patient_one = Patient("1", "abimbola", "aisha", "abisoye@gmail.com", "2015-05-19", "08118234308", "headache")
        self.patients.save(patient_one)
        self.assertEqual(1,self.patients.count())





if __name__ == '__main__':
    unittest.main()

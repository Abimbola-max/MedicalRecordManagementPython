import unittest

from src.data.models.patientprofile import PatientProfile
from src.data.repositories.patientrepo.patients import Patients


class MyPatientsTestCase(unittest.TestCase):

    def setUp(self):
        self.patients = Patients()
        self.patients.collection.delete_many({})

    def tearDown(self):
        self.patients.collection.delete_many({})

    def test_that_patients_details_can_be_saved(self):
        self.assertEqual(0,self.patients.count())
        patient_one = PatientProfile("1", "abimbola", "aisha", "abisoye@gmail.com", "2015-05-19", "08118234308", "headache")
        self.patients.save_patient(patient_one)
        self.assertEqual(1,self.patients.count())





if __name__ == '__main__':
    unittest.main()

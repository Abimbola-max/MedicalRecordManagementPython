import unittest

# from app import patient_repo
from src.data.models.patientprofile import PatientProfile
from src.data.repositories.patientrepositories.patientrepo import PatientRepo
from src.data.repositories.patientrepositories.patients import PatientRepo
from src.data.repositories.userrepositories.users import Users


class MyPatientsTestCase(unittest.TestCase):

    def setUp(self):
        self.patient_repo = Users()
        self.patients = PatientRepo(self.patient_repo)
        self.patients.collection.delete_many({})

    def tearDown(self):
        self.patients.collection.delete_many({})

    def test_that_patients_details_can_be_saved(self):
        self.assertEqual(0,self.patients.count())
        patient_one = PatientProfile("1", "abimbola@gmail.com", "aisha", "", "abimbola", "aishat", "2009-05-19", "08118234308", "female", "none")
        self.patients.save(patient_one)
        self.assertEqual(1,self.patients.count())





if __name__ == '__main__':
    unittest.main()

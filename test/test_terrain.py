
import unittest
import xmlrunner
from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):
 def test_chargement(self):

    fichier_test = "terrains/t1.txt"

    terrain = Terrain()

    terrain.charger(fichier_test)

    self.assertEqual(terrain.cases[0][0], Case.VIDE, "La case (1,1) devrait être VIDE.")
    self.assertEqual(terrain.cases[2][10], Case.CLIENT, "La case (2,10) devrait être CLIENT.")
    self.assertEqual(terrain.cases[9][17], Case.ENTREE, "La case (9,18) devrait être ENTREE.")




    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))


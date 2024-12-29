import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = rat.Runner('Усэйн', 10)
        self.runner_andrei = rat.Runner('Андрей', 9)
        self.runner_nick = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_run, result in cls.all_results.items():
            print(result)


    def test_run1(self):
        tourn = rat.Tournament(90, self.runner_usain, self.runner_nick)
        results = tourn.start()
        TournamentTest.all_results["test_run1"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[1].speed > results[2].speed)


    def test_run2(self):
        tourn = rat.Tournament(90, self.runner_andrei, self.runner_nick)
        results = tourn.start()
        TournamentTest.all_results["test_run2"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[1].speed > results[2].speed)


    def test_run3(self):
        tourn = rat.Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nick)
        results = tourn.start()
        TournamentTest.all_results["test_run3"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[1].speed > results[2].speed > results[3].speed)



if __name__ == '__main__':
    unittest.main()


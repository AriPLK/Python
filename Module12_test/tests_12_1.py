import unittest
import runner


is_frozen = 0
class RunnerTest(unittest.TestCase):


    @unittest.skipIf(lambda: is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        _runner = runner.Runner('Keith')
        for x in range(10):
            _runner.walk()

        self.assertEqual(_runner.distance, 50)

    @unittest.skipIf(lambda: is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        _runner = runner.Runner('Kate')
        for x in range(10):
            _runner.run()

        self.assertEqual(_runner.distance, 100)

    @unittest.skipIf(lambda: is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        _runner = runner.Runner('Keith')
        _runner2 = runner.Runner('Kate')
        for x in range(10):
            _runner.walk()
            _runner2.run()

        self.assertNotEqual(_runner.distance, _runner2.distance)



if __name__ == '__main__':
    unittest.main()
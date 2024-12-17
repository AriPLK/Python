import unittest
import runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        _runner = runner.Runner('Keith')
        for x in range(10):
            _runner.walk()

        self.assertEqual(_runner.distance, 50)

    def test_run(self):
        _runner = runner.Runner('Kate')
        for x in range(10):
            _runner.run()

        self.assertEqual(_runner.distance, 100)

    def test_challenge(self):
        _runner = runner.Runner('Keith')
        _runner2 = runner.Runner('Kate')
        for x in range(10):
            _runner.walk()
            _runner2.run()

        self.assertNotEqual(_runner.distance, _runner2.distance)

    def test_challenge2(self):
        _runner = runner.Runner('Keith')
        _runner2 = runner.Runner('Kate')
        for x in range(10):
            _runner.walk()
            _runner2.run()

        self.assertEqual(_runner.distance, _runner2.distance)

if __name__ == '__main__':
    unittest.main()
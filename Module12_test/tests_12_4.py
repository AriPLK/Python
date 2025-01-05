import logging
import unittest
import rt_with_exceptions as runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

is_frozen = 0
class RunnerTest(unittest.TestCase):

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:

            _runner = runner.Runner('Keith', -5)
            for x in range(10):
                _runner.walk()

            self.assertEqual(_runner.distance, 50)
            logging.info("test_walk выполнен успешно")
        except ValueError as err:
            logging.log(logging.WARNING, 'Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            _runner = runner.Runner(1)
            for x in range(10):
                _runner.run()

            self.assertEqual(_runner.distance, 100)
        except TypeError:
            logging.log(logging.WARNING, 'Неверный тип данных для объекта Runner', exc_info=True)
            raise TypeError


if __name__ == '__main__':
    unittest.main()

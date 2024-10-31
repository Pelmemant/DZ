import runner_and_tournament
import runner
import unittest
import logging

logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w", encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('runner1', -5)
        self.runner2 = runner.Runner(111)

    def test_walk(self):
        try:
            if self.runner1.speed < 0:
                raise TypeError("Скорость не может быть меньше 0")
            for i in range(10):
                self.runner1.walk()
            self.assertEqual(self.runner1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning("Неверная скорость для Runner", exc_info=e)

    def test_run(self):
        try:
            if not isinstance(self.runner2.name, str):
                raise TypeError("Имя должно быть строкой")
            for i in range(10):
                self.runner2.run()
            self.assertEqual(self.runner2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except Exception as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=e)

    def test_challenge(self):
        for i in range(10):
            self.runner1.run()
            self.runner2.walk()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)


if __name__ == '__main__':
    unittest.main()

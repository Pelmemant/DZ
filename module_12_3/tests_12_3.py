import runner_and_tournament
import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner1 = runner.Runner('runner1')
        self.runner2 = runner.Runner('runner2')

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_walk(self):
        for i in range(10):
            self.runner1.walk()
        self.assertEqual(self.runner1.distance, 50)

    def test_run(self):
        for i in range(10):
            self.runner1.run()
        self.assertEqual(self.runner1.distance, 100)

    def test_challenge(self):
        for i in range(10):
            self.runner1.run()
            self.runner2.walk()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner_2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner_3 = runner_and_tournament.Runner("Ник", 3)

    def tearDown(self):
        print(self.all_results)

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_Tournament1(self):
        Tournament1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        result = Tournament1.start()
        self.all_results = result
        self.assertTrue(result[len(result)], "Ник")

    def test_Tournament2(self):
        Tournament2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        result = Tournament2.start()
        self.all_results = result
        self.assertTrue(result[len(result)], "Ник")

    def test_Tournament3(self):
        Tournament3 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = Tournament3.start()
        self.all_results = result
        self.assertTrue(result[len(result)], "Ник")


if __name__ == '__main__':
    unittest.main()


from unittest import TestCase, main
from algorithms3 import solution

class TestMyAlgorithms(TestCase):
    def test_solution(self):
        test_case_data = [
            (["ABBBBC", "AABAAC", "BCDDAC", "DCCDDE", "DCCEDE", "DDEEEB"], 20),
            (["DDCCC", "DBBBC", "DBABC", "DBBBC", "DDCCC"], 25),
            (["BCECE", "AAAAA", "AAAAA", "AAAAA", "CBCDE"], 17),
            (["ZZAB", "AZZB", "BAZZ", "ZBAZ"], 10),
        ]
        
        for board, answer in test_case_data:
            print(board)
            self.assertEqual(solution(board), answer)


if __name__ == '__main__':
    main()

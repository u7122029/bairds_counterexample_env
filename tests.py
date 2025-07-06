import unittest
import gymnasium as gym
from bairds_counterexample_env import BairdsCounterexampleEnv


class BairdsCounterexampleTests(unittest.TestCase):
    def test_zero_action_always_zero_state(self):
        env = BairdsCounterexampleEnv()
        for i in range(1000):
            for start_state in range(env.num_intermediate_states):
                state, _ = env.reset(start_state=start_state)
                next_state, _, _, _, _ = env.step(0)
                self.assertEqual(next_state, 0)

    def test_seeding(self):
        env = BairdsCounterexampleEnv()

        state, _ = env.reset(seed=1)
        path1 = [env.step(1)[0] for _ in range(1000)]

        state, _ = env.reset(seed=1)
        path2 = [env.step(1)[0] for _ in range(1000)]

        self.assertEqual(path1, path2)

if __name__ == '__main__':
    unittest.main()

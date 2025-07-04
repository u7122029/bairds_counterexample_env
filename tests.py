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




if __name__ == '__main__':
    unittest.main()

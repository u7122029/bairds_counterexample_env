import gymnasium as gym
import numpy as np
from gymnasium import spaces


class BairdsCounterexampleEnv(gym.Env):
    metadata = {"render_modes": [], "render_fps": 4}

    def __init__(self, num_intermediate_states=6):
        # num_intermediate_states possible states, one special one (0), and the rest (1-6) are intermediate states.
        self.num_intermediate_states = num_intermediate_states

        self.observation_space = spaces.Discrete(self.num_intermediate_states + 1)
        self.action_space = spaces.Discrete(2)

        self._agent_location = None


    def reset(self, seed=None, start_state=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)
        if start_state is not None:
            assert 0 <= start_state < self.num_intermediate_states, "Inappropriate chosen start state."
            self._agent_location = start_state

        # Choose the agent's location uniformly at random
        self._agent_location = self.observation_space.sample()

        return self._agent_location, {}


    def step(self, action):
        # Map the action (element of {0,1,2,3}) to the direction we walk in
        # We use `np.clip` to make sure we don't leave the grid
        assert action in {0, 1}, "Invalid action"

        if action == 0:
            observation = 0
        else:
            observation = np.random.randint(1, self.num_intermediate_states + 1)

        return observation, 0, False, False, {}


    def render(self):
        pass


    def close(self):
        pass

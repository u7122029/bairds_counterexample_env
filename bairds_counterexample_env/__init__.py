from .bairds_counterexample import BairdsCounterexampleEnv
from gymnasium.envs.registration import register

register(
    id="bairds_counterexample-v0",
    entry_point="bairds_counterexample_env.bairds_counterexample:BairdsCounterexampleEnv"
)
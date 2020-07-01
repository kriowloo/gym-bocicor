from gym.envs.registration import register

register(
    id='bocicor-v1',
    entry_point='gym_bocicor.envs:FirstEnv',
)
register(
    id='bocicor-v2',
    entry_point='gym_bocicor.envs:SecondEnv',
)
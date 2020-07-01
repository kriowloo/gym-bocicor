# OpenAI Gym environment: gym-bocicor

This environment was created to represent the RL tasks related to genome assembly presented in the manuscript entitled [A Reinforcement Learning Approach for Solving the Fragment Assembly Problem](https://doi.org/10.1109/SYNASC.2011.9). According to OpenAI Gym instructions, use PIP to install it (after installing [Gym](https://gym.openai.com/)). You can do it directly using the Github repository address, as follows:

```sh
$ pip install -e git+https://github.com/kriowloo/gym-bocicor.git#egg=gym-bocicor
```

There are two versions that can be used after installing *gym-bocicor*, namely *gym_bocicor:bocicor-v1* and *gym_bocicor:bocicor-v2* (see an example below). The first one corresponds to the task addressed by the first experiment of the aforementioned manuscript; while the last one corresponds to the second experiment.

```python
env = gym.make('gym_bocicor:bocicor-v1')
action = env.action_space.sample()
print('Random action:', action) # expected output: an integer ranging from 0 to 3
```

> Note: if you have trouble to install and/or execute it, we recommend you to use a container of Python's Docker Image, as described below:

```sh
$ docker run -it python:3.7.8 bash
# pip install gym
# pip install -e git+https://github.com/kriowloo/gym-bocicor.git#egg=gym-bocicor
# python your_code.py
```

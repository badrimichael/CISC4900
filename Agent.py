# The Agent class details all attributes and abilities of an agent. These will start simple and become more complex
# later on. An agent may be instantiated with a probability to surge forward. Otherwise, every agent is created the
# same. They are created outside of the environment (current_state initial value is None) and they are created without
# the reward (reward initial value is False). The agent is compelled to traverse an environment as long as it doesn't
# have a reward.

from abc import ABC, abstractmethod


# Some agents have a probability to surge forward.
# All have a current state, and a reward field. All agents are
# also capable of traversal through an environment.
class Agent(ABC):
    @property
    @abstractmethod
    def probability_of_surge(self):
        pass

    @property
    @abstractmethod
    def current_state(self):
        pass

    @property
    @abstractmethod
    def reward(self):
        pass

    # As the agent traverses, the current node will change
    # to reflect the agent's current position in the environment.
    @abstractmethod
    def set_current_state(self, current_state):
        pass

    # As an agent traverses, the reward value will update based on
    # the reward of the current state.
    @abstractmethod
    def set_reward(self, reward_value):
        pass

    # The agent enters the environment.
    @abstractmethod
    def traverse(self, environment):
        pass

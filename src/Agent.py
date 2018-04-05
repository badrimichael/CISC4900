# The Agent class details all attributes and abilities of an agent. These will start simple and become more complex
# later on. An agent may be instantiated with a probability to surge forward. Otherwise, every agent is created the
# same. They are created outside of the environment (current_state initial value is None) and they are created without
# the reward (reward initial value is False). Some agents will traverse an environment based on learning algorithms
# or random number generators.

# Abstract class.
from abc import ABC, abstractmethod
import random


# Some agents have a probability to surge forward.
# All have a current state, and a reward field. All agents are
# also capable of traversal through an environment and are capable
# of recording their actions in a csv output file.
class Agent(ABC):
    # Actions list holds all of the possible actions. For an environment of m states, the actions are 0 - m-1.
    actions = []

    # Number of episodes to attempt. This can be any number.
    number_of_episodes = 500

    # The number of steps (actions) to take per episode. This can be any number, does not have to equal number
    # of episodes.
    number_of_steps = 100

    # The state where the Agent is currently located.
    current_state = None

    # The probability of the Agent surging to a higher state from the starting state.
    probability_of_surge = 0.05

    # Whether or not the Agent has a reward.
    reward = False

    @property
    @abstractmethod
    def agent_type(self):
        pass

    # The agent enters the environment.
    @abstractmethod
    def traverse(self, environment, index, csv_writer):
        pass

    # As an agent traverses, the reward value will update based on
    # the reward of the current state.
    def set_reward(self, reward_value):
        self.reward = reward_value

    # As the agent traverses, the current node will change
    # to reflect the agent's current position in the environment.
    def set_current_state(self, current_state):
        self.current_state = current_state

    # Learning agents can write their activities to an output file.
    @staticmethod
    def write_to_csv(writer, episode, state, total_reward, time, action, index, agent_type):
        file = open('output/output.csv', 'a')
        writer.writerow(
            {'Episode': episode, 'State': str(state.state), 'Reward': total_reward, 'Time': time, 'Action': action,
             'Agent': index, 'Agent Type': agent_type})
        file.close()

    @staticmethod
    def surge(environment):
        random_advance = random.randint(1, len(environment.nodes) - 1)
        current_state = environment.nodes[random_advance]
        print("Agent surged to node " + str(current_state.state))

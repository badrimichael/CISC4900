# The Agent class details all attributes and methods of an agent, regardless of whether or not it has the ability to
# learn. Agents are created outside of the environment and then inserted into the environment specified in traverse().

# Abstract class.
# Random needed for random number generators.
from abc import ABC, abstractmethod
import random


class Agent(ABC):
    # Actions list holds all of the possible actions. For an environment of m states, the actions are 0 - m-1.
    actions = []

    # Number of episodes to attempt.
    # This can be any integer > 0.
    number_of_episodes = 500

    # The number of steps (actions) to take per episode.
    # This can be any integer > 0.
    number_of_steps = 100

    # The state where the Agent is currently located.
    # Initially set to None.
    current_state = None

    # The probability of the Agent surging to a higher state from the starting state.
    probability_of_surge = 0.05

    # Whether or not the Agent has a reward.
    # This only applies to Optimal and Random agents.
    # This is overridden for learning agents in LearningAgent.py.
    reward = False

    # String that holds the reinforcement learning algorithm the agent is utilizing.
    @property
    @abstractmethod
    def agent_type(self):
        pass

    # The agent enters the environment and attempts to reach the reward.
    # Optimal and Random agents do not attempt to learn the correct path to the reward.
    # All Learning agents utilize some reinforcement learning algorithm to learn the correct path to the reward.
    # The environment that the agent will traverse, the agent number (index), and the csv_writer object created
    # in main.py are passed so the agent may record its actions in the output.csv.
    # This method returns the timesteps it took for a traversal, so Plotter.py can graph create an average graph.
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

    # If the agent surges, it chooses a random node to jump to.
    @staticmethod
    def surge(environment):
        random_advance = random.randint(1, len(environment.nodes) - 2)
        current_state = environment.nodes[random_advance]
        print("Agent surged to node " + str(current_state.state))

    # Learning agents write their activities to an output file.
    # This is necessary for analysis post-simulation.
    @staticmethod
    def write_to_csv(writer, episode, state, total_reward, time, action, index, agent_type):
        file = open('output.csv', 'a')
        writer.writerow(
            {'Episode': episode, 'State': str(state.state), 'Reward': total_reward, 'Time': time, 'Action': action,
             'Agent': index, 'Agent Type': agent_type})
        file.close()

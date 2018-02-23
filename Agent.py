# The Agent class details all attributes and abilities of an agent. These will start simple and become more complex
# later on. The agent is instantiated with a probability to surge forward. Otherwise, every agent is created the same.
# They are created outside of the environment (current_node initial value is None) and they are created without the
# reward (reward initial value is False). The agent is compelled to traverse an environment as long as it doesn't have
# a reward.

from abc import ABC, abstractmethod
import random # Necessary for random number generators.

# All agents have a probability to surge forward,
# a current node, and a reward. All agents are
# also capable of traversal through an environment.


class Agent(object):
    probability_of_surge = None
    current_node = None
    reward = False

    # Constructor that assigns a probability to surge.
    def __init__(self, probability_of_surge):
        self.probability_of_surge = probability_of_surge

    # As the agent traverses, the current node will change
    # to reflect the agent's current position in the environment.
    def set_current_node(self, current_node):
        self.current_node = current_node

    # Since the reward is initially False and cannot be
    # taken away, this method only must set it to True.
    def set_reward(self):
        self.reward = True

    # By setting the current node to the initial node, the agent
    # enters the environment. If the agent is at the initial node,
    # it has the chance to surge forward to a later state.
    # If the agent does not surge forward, it can only move forward
    # when the RNG rolls a 1. If the RNG rolls any other number,
    # the agent is sent back to the initial state.
    def traverse(self, environment):
        self.current_node = environment.nodes[0]
        while self.reward is False:
            random_surge = random.uniform(0, 1)
            if self.current_node.state == 0:
                if random_surge < self.probability_of_surge:
                    self.current_node = environment.nodes[random.randint(1, len(environment.nodes)-1)]
                    self.reward = self.current_node.reward
                    print("Agent surged to state " + str(self.current_node.state))
                    continue
                else:
                    self.current_node = self.current_node.next
                    print("Agent moved to state " + str(self.current_node.state))
            random_advance = random.randint(0, len(environment.nodes))
            if random_advance == 1:
                self.current_node = self.current_node.next
                self.reward = self.current_node.reward
                print("Agent moved to state " + str(self.current_node.state))
            else:
                self.current_node = environment.nodes[0]
                print("Agent moved back to state 0.")




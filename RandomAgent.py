# The random agent utilizes a random number generator to determine if it will move from one state to another.
# This agent will usually obtain the reward due to surging near the final state. The probability of rolling a one
# nine times in a row is very low. Random agents are different based on their probability to surge forward.

import random  # Necessary for random number generators.
from Agent import Agent


# See Agent.py.
class RandomAgent(Agent):
    probability_of_surge = None
    current_node = None
    reward = False

    # Constructor that assigns a probability to surge.
    # Required for Random Agents.
    def __init__(self, probability_of_surge):
        self.probability_of_surge = probability_of_surge

    # See Agent.py.
    def set_current_node(self, current_node):
        self.current_node = current_node

    # See Agent.py.
    def set_reward(self):
        self.reward = True

    # See Agent.py.
    # If the random agent is at the initial node,
    # it has the chance to surge forward to a later state.
    # If the random agent does not surge forward, it can only move forward
    # when the RNG rolls a 1. If the RNG rolls any other number,
    # the random agent is sent back to the initial state.
    def traverse(self, environment):
        self.current_node = environment.nodes[0]
        print("Random agent entered environment. (State 0)")
        while self.reward is False:
            random_surge = random.uniform(0, 1)
            if self.current_node.state == 0:
                if random_surge < self.probability_of_surge:
                    self.current_node = environment.nodes[random.randint(1, len(environment.nodes) - 1)]
                    self.reward = self.current_node.reward
                    print("Random agent surged to state " + str(self.current_node.state) + ".")
                    continue
                else:
                    self.current_node = self.current_node.next
                    print("Random agent moved to state " + str(self.current_node.state) + ".")
            random_advance = random.randint(0, len(environment.nodes))
            if random_advance == 1:
                self.current_node = self.current_node.next
                self.reward = self.current_node.reward
                print("Random agent moved to state " + str(self.current_node.state) + ".")
            else:
                self.current_node = environment.nodes[0]
                print("Random agent moved back to state 0.")
        else:
            print("Random agent obtained reward.\n")

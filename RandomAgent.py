# The random agent utilizes a random number generator to determine if it will move from one state to another.
# This agent will usually obtain the reward due to surging near the final state. The probability of rolling a one
# nine times in a row is very low. Random agents are different based on their probability to surge forward.

# Importing random is necessary for random number generators.
import random
from Agent import Agent


# See Agent.py.
class RandomAgent(Agent):
    probability_of_surge = 0.3
    current_state = None
    reward = False

    # Constructor to initialize the variables needed for the Random Agent.
    def __init__(self):
        # Actions list holds all of the possible actions. For an environment of m states, the actions are 0 - m-1.
        self.actions = []

        # Number of episodes to attempt. This can be any number.
        self.number_of_episodes = 25

        # The number of steps (actions) to take per episode. This can be any number, does not have to equal number
        # of episodes.
        self.number_of_steps = 50

    # See Agent.py.
    # If the random agent is at the initial node,
    # it has the chance to surge forward to a later state.
    # If the random agent does not surge forward, it can only move forward
    # when the RNG rolls a 1. If the RNG rolls any other number,
    # the random agent is sent back to the initial state.
    def traverse(self, environment, index, csv_writer):
        time = 0
        for episode in range(self.number_of_episodes):
            self.current_state = environment.starting_node
            reward = 0
            terminal_state = False
            for step in range(self.number_of_steps):
                time = time + 1
                random_surge = random.uniform(0, 1)
                if self.current_state == environment.starting_node and random_surge < self.probability_of_surge:
                    random_advance = random.randint(0, len(environment.nodes) - 1)
                    self.current_state = environment.nodes[random_advance]
                    print("Agent surged to node " + str(self.current_state.state))
                else:
                    random_advance = random.randint(0, len(environment.nodes) - 1)
                    if random_advance == 1:
                        self.current_state = self.current_state.next
                        print("Agent moved to node " + str(self.current_state.state))
                    else:
                        self.current_state = environment.starting_node
                        print("Agent moved to starting state.")
                if self.current_state.reward is True:
                    reward = 100
                    terminal_state = True
                self.write_to_csv(csv_writer, episode + 1, self.current_state, reward, time, random_advance, index)
                if terminal_state:
                    print("Agent obtained reward.")
                    break
            print("Episode " + str(episode + 1) + ": " + "Reward = " + str(reward))
            print("Steps taken: " + str(step + 1) + "\n")

# The random agent utilizes a random number generator to determine if it will move from one state to another.
# This agent will usually obtain the reward due to surging near the final state. The probability of rolling a one
# nine times in a row is very low. Random agents are different based on their probability to surge forward.

# Importing random is necessary for random number generators.
import random
from Agent import Agent


# See Agent.py.
class RandomAgent(Agent):
    agent_type = "Random"

    # See Agent.py.
    # If the random agent is at the initial node,
    # it has the chance to surge forward to a later state.
    # If the random agent does not surge forward, it can only move forward
    # when the RNG rolls a 1. If the RNG rolls any other number,
    # the random agent is sent back to the initial state.
    def traverse(self, environment, index, csv_writer):
        print("Random Agent:")
        time = 0
        reward = 0
        for episode in range(self.number_of_episodes):
            self.current_state = environment.starting_node
            terminal_state = False
            for step in range(self.number_of_steps):
                time = time + 1
                random_surge = random.uniform(0, 1)
                if self.current_state == environment.starting_node and random_surge < self.probability_of_surge:
                    self.surge(environment)
                    random_advance = 1
                else:
                    random_advance = random.randint(0, len(environment.nodes) - 1)
                    if random_advance == 1:
                        self.current_state = self.current_state.next
                        print(self.agent_type + " agent moved to node " + str(self.current_state.state))
                    else:
                        self.current_state = environment.starting_node
                        print(self.agent_type + " agent moved to starting state.")
                if self.current_state.reward is True:
                    reward = reward + 100
                    terminal_state = True
                self.write_to_csv(csv_writer, episode + 1, self.current_state, reward, time, random_advance, index,
                                  self.agent_type)
                if terminal_state:
                    print(self.agent_type + " agent obtained reward.")
                    break
            print("Episode " + str(episode + 1) + ": " + "Reward = " + str(reward))
            print("Steps taken: " + str(step + 1) + "\n")

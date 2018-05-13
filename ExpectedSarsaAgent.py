# The ExpectedSarsaAgent relies on the reinforcement learning algorithm: Expected-SARSA to traverse the environment.

# The ExpectedSarsaAgent is a LearningAgent because it utilizes some reinforcement learning algorithm.
# The max method from numpy module is needed in the Bellman equation.
from LearningAgent import LearningAgent
import numpy as np


class ExpectedSarsaAgent(LearningAgent):
    # Explicitly state the reinforcement learning algorithm for the output.csv file.
    agent_type = "Expected SARSA"

    # Constructor is needed for initializing more than one agent.
    def __init__(self):
        self.actions = []
        self.q_table = {}

    # See Agent.py
    def traverse(self, environment, index, csv_writer):
        print("Expected Sarsa Agent:")
        # Initialize possible actions based on environment size.
        for node in environment.nodes:
            self.actions.append(node.state)
        time = 0

        # For each episode, the initial state is the starting state in the environment,
        # the reward is zero'd, the alpha chosen corresponds to the number of the episode.
        for episode in range(self.number_of_episodes):
            self.current_state = environment.starting_node
            alpha = self.decaying_alphas[episode]
            # For each step, it chooses a new action, determines the next state, reward, and if the next state is
            # terminal or not. Then the Sarsa function is calculated and the agent moves to the next state.
            for step in range(self.number_of_steps):
                time = time + 1
                action = self.choose_action(self.current_state)
                next_state, reward, terminal_state = self.act(self.current_state, action, environment)
                self.total_reward += reward
                best_action = np.argmax(self.q(next_state))
                expected_return = (
                        (1 - self.epsilon) * self.q(next_state, best_action) + (self.epsilon / len(self.actions))
                        * sum(self.q(next_state, act) for act in range(len(self.actions))))
                # expected_return = np.max(self.q(next_state))
                self.q(self.current_state)[action] = self.q(self.current_state, action) + alpha * (
                        reward + self.gamma * expected_return - self.q(self.current_state, action))
                self.current_state = next_state
                self.write_to_csv(csv_writer, episode + 1, self.current_state, self.total_reward, time, action, index,
                                  self.agent_type)
                if terminal_state:
                    print("Agent obtained reward.")
                    if self.learned_reward_value > 0:
                        if self.total_reward % self.learned_reward_value == 0:
                            self.set_correct_action(self.choose_random_action())
                    break
            print("Episode " + str(episode + 1) + ": " + "Reward = " + str(self.total_reward))
            print("Steps taken: " + str(step + 1) + "\n")
        print("Total time-steps: " + str(time))
        return time

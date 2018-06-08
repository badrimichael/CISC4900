# The QAgent relies on the reinforcement learning algorithm: Q-Learning to traverse the environment.

# The QAgent is a LearningAgent because it utilizes some reinforcement learning algorithm.
# The max method from numpy module is needed in the Bellman equation.
from LearningAgent import LearningAgent
import numpy as np


class QAgent(LearningAgent):
    # Explicitly state the reinforcement learning algorithm for the output.csv file.
    agent_type = "Q-learning"

    # Constructor is needed for initializing more than one agent.
    def __init__(self):
        self.actions = []
        self.q_table = {}

    # See Agent.py
    def traverse(self, environment, index, csv_writer):
        print("Q-learning Agent:")
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
            # terminal or not. Then the q-learning function is calculated and the agent moves to the next state.
            for step in range(self.number_of_steps):
                time = time + 1
                environment.random_action_change()
                action = self.choose_action(self.current_state, environment)
                next_state, reward, terminal_state = self.act(self.current_state, action, environment)
                self.total_reward += reward
                self.q(self.current_state)[action] = self.q(self.current_state, action) + alpha * (
                        reward + self.gamma * np.max(self.q(next_state)) - self.q(self.current_state, action))
                self.current_state = next_state
                self.write_to_csv(csv_writer, episode + 1, self.current_state, self.total_reward, time, action, index,
                                  self.agent_type)
                if terminal_state:
                    print(self.agent_type + " agent obtained reward.")
                    environment.process_terminal_state_obstacles(self.total_reward)
                    break
            print("Episode " + str(episode + 1) + ": " + "Reward = " + str(self.total_reward))
            print("Steps taken: " + str(step + 1) + "\n")
        print("Total time-steps: " + str(time))
        return time

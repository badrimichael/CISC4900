# The SarsaAgent relies on Sarsa to obtain a reward. The agent either randomly explores the environment or
# chooses the best action from experience. The agent gains experience from randomly exploring, so at first it will
# wander aimlessly until it randomly comes across the reward.

from LearningAgent import LearningAgent


class SarsaAgent(LearningAgent):
    agent_type = "SARSA"

    def __init__(self):
        self.actions = []
        self.q_table = {}

    # See Agent.py
    def traverse(self, environment, index, csv_writer):
        print("Sarsa Agent:")
        # Initialize possible actions based on environment size.
        for node in environment.nodes:
            self.actions.append(node.state)
        time = 0

        # For each episode, the initial state is the starting state in the environment,
        # the reward is zero'd, the alpha chosen corresponds to the number of the episode.\
        total_reward = 0
        for episode in range(self.number_of_episodes):
            self.current_state = environment.starting_node
            alpha = self.decaying_alphas[episode]
            action = self.choose_action(self.current_state)
            # For each step, it chooses a new action, determines the next state, reward, and if the next state is
            # terminal or not. Then the Sarsa function is calculated and the agent moves to the next state.
            for step in range(self.number_of_steps):
                time = time + 1
                next_state, reward, terminal_state = self.act(self.current_state, action, environment)
                next_action = self.choose_action(next_state)
                total_reward += reward
                self.q(self.current_state)[action] = self.q(self.current_state, action) + alpha * (
                        reward + self.gamma * self.q(next_state, next_action) - self.q(self.current_state, action))
                self.current_state = next_state
                action = next_action
                self.write_to_csv(csv_writer, episode + 1, self.current_state, total_reward, time, action, index,
                                  self.agent_type)
                if terminal_state:
                    print("Agent obtained reward.")
                    break
            print("Episode " + str(episode + 1) + ": " + "Reward = " + str(total_reward))
            print("Steps taken: " + str(step + 1) + "\n")
        print("Total time-steps: " + str(time))
        return time

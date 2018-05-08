# The QVAgent relies on the reinforcement learning algorithm: QV-Learning to traverse the environment.

# The QVAgent is a LearningAgent because it utilizes some reinforcement learning algorithm.
from LearningAgent import LearningAgent


class QVAgent(LearningAgent):
    # Explicitly state the reinforcement learning algorithm for the output.csv file.
    agent_type = "QV-learning"

    # Constructor is needed for initializing more than one agent.
    def __init__(self):
        self.actions = []
        self.q_table = {}
        self.v_table = {}

    # Exclusive to QVAgent.py.
    # If a state has a reward, the value is 1. If the state doesn't have a reward, the value is 0.
    # If the state isn't in the v table yet, add it.
    # This works similarly to the method q found in LearningAgent.py.
    def v(self, state=None):
        if state is None:
            return self.v_table
        if state not in self.v_table:
            self.v_table[state] = 0
        return self.v_table[state]

    # See Agent.py
    def traverse(self, environment, index, csv_writer):
        print("QV-learning Agent:")
        # Initialize possible actions based on environment size.
        for node in environment.nodes:
            self.actions.append(node.state)
        time = 0

        # For each episode, the initial state is the starting state in the environment,
        # the reward is zero'd, the alpha chosen corresponds to the number of the episode.\
        for episode in range(self.number_of_episodes):
            self.current_state = environment.starting_node
            alpha = self.decaying_alphas[episode]
            action = self.choose_action(self.current_state)
            # For each step, it chooses a new action, determines the next state, reward, and if the next state is
            # terminal or not. Then the QV function is calculated and the agent moves to the next state.
            for step in range(self.number_of_steps):
                time = time + 1
                next_state, reward, terminal_state = self.act(self.current_state, action, environment)
                next_action = self.choose_action(next_state)
                self.total_reward += reward
                self.v()[self.current_state] = self.v(self.current_state) + (alpha * (
                        reward + (self.gamma * self.v(next_state)) - self.v(self.current_state)))
                self.q(self.current_state)[action] = self.q(self.current_state, action) + alpha * (
                        reward + self.gamma * self.v(next_state) - self.q(self.current_state, action))
                self.current_state = next_state
                action = next_action
                self.write_to_csv(csv_writer, episode + 1, self.current_state, self.total_reward, time, action, index,
                                  self.agent_type)
                if terminal_state:
                    print("Agent obtained reward.")
                    break
            print("Episode " + str(episode + 1) + ": " + "Reward = " + str(self.total_reward))
            print("Steps taken: " + str(step + 1) + "\n")
        print("Total time-steps: " + str(time))
        return time

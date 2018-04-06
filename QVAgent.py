# The QVAgent relies on QV-learning to obtain a reward. The agent either randomly explores the environment or
# chooses the best action from experience. The agent gains experience from randomly exploring, so at first it will
# wander aimlessly until it randomly comes across the reward.

# Random is required for the RNG.
import numpy as np
import random
from LearningAgent import LearningAgent


class QVAgent(LearningAgent):
    agent_type = "QV-learning"

    def __init__(self):
        self.actions = []
        self.q_table = {}
        self.v_table = {}

    # If the current state hasn't been experienced yet, add it and create a 0 column for it.
    # If the current state has been experienced, return the state and action value.
    def q(self, state, action=None):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        if action is None:
            return self.q_table[state]
        return self.q_table[state][action]

    # If a state has a reward, the value is 1. If the state doesn't have a reward, the value is 0.
    # If the state isn't in the v table yet, add it.
    def v(self, state=None):
        if state is None:
            return self.v_table
        if state not in self.v_table and state.reward is False:
            self.v_table[state] = 0
        elif state not in self.v_table and state.reward is True:
            self.v_table[state] = 1
        return self.v_table[state]

    # If the RNG rolls less than epsilon, randomly choose an action based on available actions.
    # Otherwise, choose an action based on experience (refer to q_table).
    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            action = random.choice(self.actions)
            # print("RNG rolled " + str(action) + ".", end="", flush=True)
            return action
        else:
            action = np.argmax(self.q(state))
            #  print("Best action from experience is " + str(action) + ".", end="", flush=True)
            return action

    # See Agent.py
    def traverse(self, environment, index, csv_writer):
        print("QV-learning Agent:")
        # Initialize possible actions based on environment size.
        for node in environment.nodes:
            self.actions.append(node.state)
        time = 0

        # Based on current state and action, decide where to go next, if the agent has reached a terminal state,
        # and what reward is obtained.
        def act(state, action):
            random_surge = random.uniform(0, 1)
            if state == environment.starting_node and random_surge < self.probability_of_surge:
                random_advance = random.randint(1, len(environment.nodes) - 1)
                state = environment.nodes[random_advance]
                terminal_state = False
                reward = 0
                print("Agent surged to node " + str(state.state))
            # If action is 1, the agent can progress to the next state.
            elif action == 1:
                state = state.next
                print("Agent moved to node " + str(state.state))
                terminal_state = False
                reward = 0
            # Else, the agent is returned to the starting state of the environment.
            else:
                reward = 0
                state = environment.starting_node
                print("Agent moved to starting state.")
                terminal_state = False
            # If current state is a reward, give reward.
            if state.reward is True:
                reward = 100
                terminal_state = True
            return state, reward, terminal_state

        # For each episode, the initial state is the starting state in the environment,
        # the reward is zero'd, the alpha chosen corresponds to the number of the episode.\
        total_reward = 0
        for episode in range(self.number_of_episodes):
            self.current_state = environment.starting_node
            alpha = self.decaying_alphas[episode]
            action = self.choose_action(self.current_state)
            # For each step, it chooses a new action, determines the next state, reward, and if the next state is
            # terminal or not. Then the QV function is calculated and the agent moves to the next state.
            for step in range(self.number_of_steps):
                time = time + 1
                next_state, reward, terminal_state = act(self.current_state, action)
                next_action = self.choose_action(next_state)
                total_reward += reward
                self.v()[self.current_state] = self.v(self.current_state) + (alpha * (
                        reward + (self.gamma * self.v(next_state)) - self.v(self.current_state)))
                self.q(self.current_state)[action] = self.q(self.current_state, action) + alpha * (
                        reward + self.gamma * self.v(next_state) - self.q(self.current_state, action))
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

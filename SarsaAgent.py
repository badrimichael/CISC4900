# The SarsaAgent relies on Sarsa to obtain a reward. The agent either randomly explores the environment or
# chooses the best action from experience. The agent gains experience from randomly exploring, so at first it will
# wander aimlessly until it randomly comes across the reward.

# Numpy is required as the q_table is a matrix. Random is also required for the RNG.
import numpy as np
from Agent import Agent
import random


# Just like all other Agents, there is an initial reward of 0, a current_state field,
# and a probability to surge.
class SarsaAgent(Agent):
    current_state = None
    probability_of_surge = 0
    reward = 0

    # Constructor to initialize the variables needed for the Q-learning algorithm.
    def __init__(self):
        # Actions list holds all of the possible actions. For an environment of m states, the actions are 0 - m-1.
        self.actions = []
        # Number of episodes to attempt. This can be any number.
        self.number_of_episodes = 25
        # The number of steps (actions) to take per episode. This can be any number, does not have to equal number
        # of episodes.
        self.number_of_steps = 25
        # The alpha variable in the Q-learning equation decreases as the episodes increase. The minimum value is
        # when alpha stops decreasing. Alpha is the learning rate.
        self.minimum_alpha = 0.02
        # Gamma is the discount factor.
        self.gamma = 1
        # A list of alphas starts from 1.0 and decays based on the number of episodes until minimum_alpha is reached.
        self.decaying_alphas = np.linspace(1.0, self.minimum_alpha, self.number_of_episodes)
        # Epsilon determines whether or not the action will be random or chosen from experience.
        # This can be any value less than 1. If it is 1, it will always choose a random action.
        self.epsilon = 0.4
        # Q_table is initialized as an empty dictionary.
        self.q_table = {}

    # See Agent.py
    def set_current_state(self, current_state):
        self.current_state = current_state

    # See Agent.py
    def set_reward(self, reward_value):
        self.reward = reward_value + self.reward

    # If the current state hasn't been experienced yet, add it and create a 0 column for it.
    # If the current state has been experienced, return the state and action value.
    def q(self, state, action=None):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        if action is None:
            return self.q_table[state]
        return self.q_table[state][action]

    # If the RNG rolls less than epsilon, randomly choose an action based on available actions.
    # Otherwise, choose an action based on experience (refer to q_table).
    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            action = random.choice(self.actions)
            print("RNG rolled " + str(action))
            return action
        else:
            action = np.argmax(self.q(state))
            print("Best action from experience is " + str(action))
            return action

    # See Agent.py
    def traverse(self, environment):
        print("Sarsa Agent:")
        # Initialize possible actions based on environment size.
        for node in environment.nodes:
            self.actions.append(node.state)

        # Based on current state and action, decide where to go next, if the agent has reached a terminal state,
        # and what reward is obtained.
        def act(state, action):
            # If action is 1, the agent can progress to the next state.
            if action == 1:
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
            # If current state is a terminal state, give reward.
            if state.reward is True:
                reward = 100
                terminal_state = True
            return state, reward, terminal_state

        # For each episode, the initial state is the starting state in the environment,
        # the reward is zero'd, the alpha chosen corresponds to the number of the episode.
        for episode in range(self.number_of_episodes):
            state = environment.starting_node
            total_reward = 0
            alpha = self.decaying_alphas[episode]
            action = self.choose_action(state)

            # For each step, it chooses a new action, determines the next state, reward, and if the next state is
            # terminal or not. Then the Sarsa function is calculated and the agent moves to the next state.
            for step in range(self.number_of_steps):
                next_state, reward, terminal_state = act(state, action)
                next_action = self.choose_action(next_state)
                total_reward += reward
                self.q(state)[action] = self.q(state, action) + alpha * (
                        reward + self.gamma * self.q(next_state, next_action) - self.q(state, action))
                if terminal_state:
                    print("Agent obtained reward.")
                    break
                state = next_state
                action = next_action
            print("Episode " + str(episode + 1) + ": " + "Reward = " + str(total_reward))
            print("Steps taken: " + str(step + 1) + "\n")

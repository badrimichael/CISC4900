# Learning agents utilize some reinforcement learning algorithm to reach the terminal state of the environment.
# This abstraction helps when changing a value such as epsilon or gamma, because the changes are applied to all
# learning agents.

from abc import ABC
from Agent import Agent
import numpy as np
import random


class LearningAgent(Agent, ABC):
    # The current value of the Agent's total reward.
    reward = 0

    # The alpha variable in the Q-learning equation decreases as the episodes increase. The minimum value is
    # when alpha stops decreasing. Alpha is the learning rate.
    minimum_alpha = 0.02

    # The discount factor.
    gamma = 0.9

    # A list of alphas starts from 1.0 and decays based on the number of episodes until minimum_alpha is reached.
    decaying_alphas = np.linspace(1.0, minimum_alpha, Agent.number_of_episodes)

    # Epsilon determines whether or not the action will be random or chosen from experience.
    # This can be any value less than 1. If it is 1, it will always choose a random action.
    epsilon = 0.1

    # Q_table is initialized as an empty dictionary.
    q_table = {}

    # Initialize q table with values or update them.
    # If the current state hasn't been experienced yet, add it and create a 0 column for it.
    # If the current state has been experienced, return the state and action value.
    def q(self, state, action=None):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        if action is None:
            return self.q_table[state]
        return self.q_table[state][action]

    # Chooses action based on state.
    # If the RNG rolls less than epsilon, randomly choose an action based on available actions.
    # Otherwise, choose an action based on experience (refer to q_table).
    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            action = random.choice(self.actions)
            return action
        else:
            action = np.argmax(self.q(state))
            return action

    # Based on current state and action, decide where to go next, if the agent has reached a terminal state,
    # and what reward is obtained.
    def act(self, state, action, environment):
        random_surge = random.uniform(0, 1)
        if state == environment.starting_node and random_surge < self.probability_of_surge:
            random_advance = random.randint(1, len(environment.nodes) - 2)
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

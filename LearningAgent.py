# Learning agents utilize some reinforcement learning algorithm to reach the terminal state of the environment.
# This abstraction helps when changing a value such as epsilon or gamma, because the changes are applied to all
# learning agents.

from abc import ABC
from Agent import Agent
import numpy as np


class LearningAgent(Agent, ABC):

    # The current value of the Agent's total reward.
    reward = 0

    # The alpha variable in the Q-learning equation decreases as the episodes increase. The minimum value is
    # when alpha stops decreasing. Alpha is the learning rate.
    minimum_alpha = 0.02

    # The discount factor.
    gamma = 0.8

    # A list of alphas starts from 1.0 and decays based on the number of episodes until minimum_alpha is reached.
    decaying_alphas = np.linspace(1.0, minimum_alpha, Agent.number_of_episodes)

    # Epsilon determines whether or not the action will be random or chosen from experience.
    # This can be any value less than 1. If it is 1, it will always choose a random action.
    epsilon = 0.2

    # Q_table is initialized as an empty dictionary.
    q_table = {}


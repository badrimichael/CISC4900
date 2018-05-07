# Learning agents utilize some reinforcement learning algorithm to reach the terminal state of the environment.
# This abstraction helps when changing a value such as epsilon or gamma, because the changes are applied to all
# learning agents. The concrete methods defined here are actions that can be taken by any learning agent.

from abc import ABC
from Agent import Agent
import numpy as np
import random


class LearningAgent(Agent, ABC):
    # The initial reward held by an agent is always zero
    # since it has not had the chance to traverse an environment.
    reward = 0

    # The learning rate (alpha) in the Bellman equation decreases as the episodes increase.
    # We specify a minimum alpha to ensure alpha does not decrease below this value.
    minimum_alpha = 0.02

    # A list of learning rates (alphas) starts from 1.0 and decays based
    # on the number of episodes until minimum_alpha is reached.
    decaying_alphas = np.linspace(1.0, minimum_alpha, Agent.number_of_episodes)

    # The discount factor in the Bellman equation is known as gamma.
    gamma = 0.9

    # Epsilon determines whether or not the action will be random or chosen from experience.
    # This can be any value less than 1. If it is 1, it will always choose a random action.
    epsilon = 0.1

    # Q_table is initialized as an empty dictionary.
    # This table is initialized with values in the q method.
    q_table = {}

    # Probability of randomly turning an action of 1 to an action of 0.
    random_fail = 0

    # Defines the correct action needed to advance a state in the environment.
    # It starts off as 1, and can be changed using the set method below.
    correct_action = 1

    # Set method for the correct action.
    def set_correct_action(self, new_action):
        self.correct_action = new_action

    # When called, this method chooses a random action to replace the current correct action.
    # The possible actions that can be chosen are all actions in the list except the current
    # correct action.
    def choose_random_action(self):
        new_action = random.choice(self.actions)
        if new_action != self.correct_action:
            return new_action
        else:
            self.choose_random_action()

    # Learning agents can write their activities to an output file.
    @staticmethod
    def write_to_csv(writer, episode, state, total_reward, time, action, index, agent_type):
        file = open('output.csv', 'a')
        writer.writerow(
            {'Episode': episode, 'State': str(state.state), 'Reward': total_reward, 'Time': time, 'Action': action,
             'Agent': index, 'Agent Type': agent_type})
        file.close()

    # Initialize q table with values or update them.
    # If the current state hasn't been experienced yet, add it and zero the values for it.
    # If the current state has been experienced, return the state and action value.
    # If the action passed is None, return all of the values corresponding to the state value.
    def q(self, state, action=None):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        if action is None:
            return self.q_table[state]
        return self.q_table[state][action]

    # Chooses an action based on state.
    # If the RNG rolls less than epsilon, randomly choose an action based on available actions.
    # Otherwise, choose an action based on experience.
    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        else:
            return np.argmax(self.q(state))

    # Based on current state and action, decide: where to go next,
    # if the agent has reached a terminal state, and what reward is obtained.
    # If the action is 1, there is a chance to change that action to 0.
    # If the action remains 1, move to the next state.
    # If the action is 0 or has been changed to 0, return to the beginning of the environment.
    # If the agent has moved to the last state, give it a reward.
    def act(self, state, action, environment):
        if action == self.correct_action:
            if random.uniform(0, 1) < self.random_fail:
                action = 0
                print("Action 1 -> 0.")
        if state == environment.starting_node and random.uniform(0, 1) < self.probability_of_surge:
            random_advance = random.randint(1, len(environment.nodes) - 2)
            state = environment.nodes[random_advance]
            terminal_state = False
            reward = 0
            print("Agent surged to node " + str(state.state))
        # If action is 1, the agent can progress to the next state.
        elif action == self.correct_action:
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

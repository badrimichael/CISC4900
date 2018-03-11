# This program creates an environment comprised of nodes and different agents to navigate these environments.
# The goal of the agent is to learn how to maximize the reward value through reinforcement learning algorithms.
# The actions of the agents will be saved in a file for analysis.

# This purpose of this main method is to be as simple as possible. The environment(s) and agent(s)
# will be created here and agents can be reused for multiple environments (see Agent.py and Environment.py).
# This follows standard object oriented programming styles in which the main method tends to be the least busy.
# This current main method is essentially a test to ensure environments are created properly and agents act as intended.

from Environment import Environment
from RandomAgent import RandomAgent
from OptimalAgent import OptimalAgent
from QAgent import QAgent
from SarsaAgent import SarsaAgent
import csv


# Creates csv file and initializes it with header information.
def create_csv():
    file = open('output.csv', 'w')
    header_names = ['Agent', 'Episode', 'Time', 'State', 'Action', 'Reward']
    csv_writer = csv.DictWriter(file, fieldnames=header_names, lineterminator='\n')
    csv_writer.writeheader()
    return csv_writer


# Create an environment consisting of n nodes where n is the argument of the constructor.
environment = Environment(4)

# Stores agents in a list. One agent will traverse at a time.
agents = []

# Creates a random agent with probability of surging as the argument.
# Creates an optimal agent.
# agent = RandomAgent(0.01)
# agent2 = OptimalAgent()

# Initialize DictWriter object for csv file.
writer = create_csv()

# Creates an agent that learns with Q-learning and an agent that learns with SARSA.
q_agent = QAgent()
sarsa_agent = SarsaAgent()

# Add both to the agents list.
agents.append(q_agent)
agents.append(sarsa_agent)

# For each agent in the list of agents, begin traversal.
for agent in agents:
    agent.traverse(environment, agents.index(agent) + 1, writer)

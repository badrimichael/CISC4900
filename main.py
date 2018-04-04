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
from ExpectedSarsaAgent import ExpectedSarsaAgent
import csv
import matplotlib.pyplot as mpl


# Creates csv file and initializes it with header information.
def create_output_csv():
    file = open('output.csv', 'w')
    header_names = ['Agent', 'Agent Type', 'Episode', 'Time', 'State', 'Action', 'Reward']
    csv_writer = csv.DictWriter(file, fieldnames=header_names, lineterminator='\n')
    csv_writer.writeheader()
    return csv_writer


# Stores agents in a list. One agent will traverse at a time.
agents = []

# Initialize DictWriter object for csv file.
writer = create_output_csv()

# Prompt user for number of agents of each type and environment size.
print("For each input, enter an integer and press the ENTER key to confirm.")
optimal_count = int(input("How many Optimal agents would you like to simulate?\n"))
random_count = int(input("How many Random agents would you like to simulate?\n"))
q_count = int(input("How many Q-learning agents would you like to simulate?\n"))
sarsa_count = int(input("How many SARSA agents would you like to simulate?\n"))
expected_sarsa_count = int(input("How many Expected SARSA agents would you like to simulate?\n"))
environment_size = int(input("How many nodes would you like the environment to have?\n"))

# Calculate the total number of agents.
total_agent_count = optimal_count + random_count + q_count + sarsa_count + expected_sarsa_count

# Populate agents list.
for _ in range(optimal_count):
    agents.append(OptimalAgent())
for _ in range(random_count):
    agents.append(RandomAgent())
for _ in range(q_count):
    agents.append(QAgent())
for _ in range(sarsa_count):
    agents.append(SarsaAgent())
for _ in range(expected_sarsa_count):
    agents.append(ExpectedSarsaAgent())

# Create an environment consisting of environment_size nodes where environment_size is the argument of the constructor.
environment = Environment(environment_size)

# For each agent in the list of agents, begin traversal.
print("\nRunning...")
for agent in agents:
    agent.traverse(environment, agents.index(agent) + 1, writer)
print("Agents done traversing. Check output.csv for record of simulation.")

total_reward_q = []
total_reward_sarsa = []
total_reward_expected_sarsa = []

with open('output.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row[1] == "Q-learning":
            total_reward_q.append(float(row[6]))
        if row[1] == "SARSA":
            total_reward_sarsa.append(float(row[6]))
        if row[1] == "Expected SARSA":
            total_reward_expected_sarsa.append(float(row[6]))

mpl.xlabel('Time steps')
mpl.ylabel('Total Reward')
timesteps_q = list(range(len(total_reward_q)))
timesteps_sarsa = list(range(len(total_reward_sarsa)))
timesteps_expected_sarsa = list(range(len(total_reward_expected_sarsa)))

mpl.plot(timesteps_q, total_reward_q, label='Q-Learning')
mpl.plot(timesteps_sarsa, total_reward_sarsa, label='SARSA')
mpl.plot(timesteps_expected_sarsa, total_reward_expected_sarsa, label='Expected SARSA')
mpl.legend()
if sarsa_count == q_count == expected_sarsa_count == 1:
    mpl.show()

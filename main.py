# Project Title: Simulations of Reinforcement Learning in an Ecological Task
# Name: Michael Badri, Brooklyn College Department of Computer and Information Science
# Supervisor: Dr. Stefano Ghirlanda, Brooklyn College Department of Psychology

# The goal of this project is to simulate the ecological task of behavior chaining using reinforcement learning
# algorithms

# The purpose of this main method is to be as simple as possible. The environment(s) and agent(s)
# will be created here and agents can be reused for multiple environments (see Agent.py and Environment.py).
# This follows standard object oriented programming styles in which the main method tends to be the least busy.
# The output.csv file used for analysis and graphing is created with its header information here.

from Environment import Environment
from RandomAgent import RandomAgent
from OptimalAgent import OptimalAgent
from QAgent import QAgent
from SarsaAgent import SarsaAgent
from ExpectedSarsaAgent import ExpectedSarsaAgent
from QVAgent import QVAgent
import csv
import time
from Plotter import Plotter


def main():
    # Creates csv output file.
    file = open('output.csv', 'w')

    # Stores agents in a list. One agent will traverse at a time
    #  to ensure output file will be parsed properly.
    agents = []
    agent_record = {}

    # Initialize DictWriter object for csv file.
    writer = format_output_csv(file)

    # Prompt user for number of agents of each type and environment size.
    print("For each input, enter an positive integer and press the ENTER key to confirm.\n" +
          "If you simulate any Optimal or Random agents, a graph will not be generated.\n" +
          "To generate an average graph, simulate the same number of Q-Learning, SARSA, Expected-SARSA,"
          " and QV-Learning agents.\n")

    optimal_count = int(input("How many Optimal agents would you like to simulate?\n"))
    random_count = int(input("How many Random agents would you like to simulate?\n"))
    q_count = int(input("How many Q-learning agents would you like to simulate?\n"))
    sarsa_count = int(input("How many SARSA agents would you like to simulate?\n"))
    expected_sarsa_count = int(input("How many Expected SARSA agents would you like to simulate?\n"))
    qv_count = int(input("How many QV-learning agents would you like to simulate?\n"))
    environment_size = int(input("How many states would you like the environment to have?\n"))

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
    for _ in range(qv_count):
        agents.append(QVAgent())

    # Create an environment consisting of environment_size nodes where
    # environment_size is the argument of the constructor.
    environment = Environment(environment_size)

    # For each agent in the list of agents, begin traversal.
    print("\nRunning...")
    starting_time = int(time.time())
    for agent in agents:
        agent_record[agents.index(agent) + 1] = agent.traverse(environment, agents.index(agent) + 1, writer)
    print("Agents done traversing. Check output.csv for record of simulation.")
    print("Traversal process took " + str(int(time.time()) - starting_time) + " seconds.")
    file.close()

    # If certain conditions are met, produce graphs.
    if sarsa_count == q_count == expected_sarsa_count == qv_count == 1:
        plotter = Plotter()
        plotter.one_simulation_graph()
    elif sarsa_count == q_count == expected_sarsa_count == qv_count:
        plotter = Plotter()
        plotter.average_graph(agent_record, q_count, sarsa_count, expected_sarsa_count, qv_count)


# Adds header information to csv file.
def format_output_csv(file):
    header_names = ['Agent', 'Agent Type', 'Episode', 'Time', 'State', 'Action', 'Reward']
    csv_writer = csv.DictWriter(file, fieldnames=header_names, lineterminator='\n')
    csv_writer.writeheader()
    return csv_writer


# Allows for top-down design.
if __name__ == "__main__":
    main()

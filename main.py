# Project Title: Simulations of Reinforcement Learning in an Ecological Task
# Author: Michael Badri, Brooklyn College Department of Computer and Information Science
# Supervisor: Dr. Stefano Ghirlanda, Brooklyn College Department of Psychology

# The goal of this project is to simulate the ecological task of chaining using reinforcement learning
# algorithms.

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


def main():
    # Creates csv output file.
    file = open('output.csv', 'w')

    # Stores agents in a list. One agent will traverse at a time
    # to ensure output file will be parsed properly.
    agents = []
    agent_record = {}

    # Initialize DictWriter object for csv file.
    writer = format_output_csv(file)

    # Prompt user for number of agents of each type and environment size.
    print("Project Title: Simulations of Reinforcement Learning in an Ecological Task\n" +
          "Author: Michael Badri, Brooklyn College Department of Computer and Information Science\n" +
          "Supervisor: Dr. Stefano Ghirlanda, Brooklyn College Department of Psychology\n\n" +
          "Chaining Simulation Program: "
          "For each agent input, enter an integer greater than or equal to 0 and press the ENTER key to confirm.\n" +
          "The environment size input must be an integer greater than 2.\n" +
          "Output CSV file will be created in the current directory. For large simulations, ensure you have enough "
          "available disk space.\n" +
          "Source code is available on GitHub: https://github.com/badrimichael/CISC4900\n" +
          "Supplementary graphing software also available on GitHub: https://github.com/badrimichael/CISC4900-R\n")

    optimal_count = int(input("How many Optimal agents would you like to simulate?\n"))
    random_count = int(input("How many Random agents would you like to simulate?\n"))
    q_count = int(input("How many Q-learning agents would you like to simulate?\n"))
    sarsa_count = int(input("How many SARSA agents would you like to simulate?\n"))
    expected_sarsa_count = int(input("How many Expected SARSA agents would you like to simulate?\n"))
    qv_count = int(input("How many QV-learning agents would you like to simulate?\n"))
    environment_size = int(input("How many states would you like the environment to have?\n"))

    total_number_of_agents = optimal_count + random_count + q_count + sarsa_count + expected_sarsa_count + qv_count

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
    print(str(total_number_of_agents) + " agents have completed traversal of environment size " + str(
        environment_size) + ".\n" + "Check output.csv for record of simulation.\n" +
          "Traversal process took " + str(int(time.time()) - starting_time) + " seconds.")
    file.close()


# Adds header information to csv file.
def format_output_csv(file):
    header_names = ['Agent', 'Agent Type', 'Episode', 'Time', 'State', 'Action', 'Reward']
    csv_writer = csv.DictWriter(file, fieldnames=header_names, lineterminator='\n')
    csv_writer.writeheader()
    return csv_writer


# Allows for top-down design.
if __name__ == "__main__":
    main()

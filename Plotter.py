# The Plotter is capable of creating different types of graphs. The external module responsible for graphing is
# matplotlib. Numpy is needed for averaging and pandas is needed for parsing the csv file quickly. The output
# csv generated in main.py is required to generate a graph. Each graph type has its own static method responsible
# for generating the graph.

import matplotlib.pyplot as mpl
import numpy as np
import time
from pandas import read_csv


class Plotter(object):
    # This method generates a graph when there are more than one agent of each type.
    # The entire output.csv file is read and split into lists for each type of learning agent.
    # This list is then split again into individual agents per type of learning agent.
    # These nested lists are converted to numpy arrays and averaged to produce a one-dimensional
    # list that is then graphed versus the minimum time-step of all simulated agents.
    @staticmethod
    def average_graph(agent_record, q_count, sarsa_count, expected_sarsa_count, qv_count):

        # Store the starting time for later calculating compute time.
        starting_time = int(time.time())
        print("\nGenerating average graph...")

        # Lambda to determine the minimum time-step value from the entire record of
        # simulated agents. This value is saved into a variable for later.
        print("Calculating minimum time-step...")
        key_min = min(agent_record.keys(), key=(lambda k: agent_record[k]))
        min_timesteps = agent_record[key_min]

        # In order to parse the output.csv file for multiple agents of each type,
        # there must be a list of numbers that correspond to the agent number in output.csv.
        number_of_agents = list(x + 1 for x in range(len(agent_record)))

        # All agents are put into a list.
        agent_list = []

        # Each agent will then be put into another list based on the type of learning agent it is.
        q_agents = []
        sarsa_agents = []
        expected_sarsa_agents = []
        qv_agents = []

        # Open the output.csv file in read mode.
        # Read all reward values into a temporary list and then append that list to agent_list.
        # At the end of the for loop, agent_list will be a nested list of every agent's rewards, sorted by
        # their agent number or index.
        print("Reading output.csv...")
        df = read_csv('output.csv', skiprows=1, delimiter=',', )
        print("Parsing output.csv...")
        for _ in number_of_agents:
            agent_temp = []
            for row in df.itertuples():
                if int(row[1]) == _:
                    agent_temp.append(int(row[7]))
            agent_list.append(agent_temp)

        # Slow, built in python csv method.
        # for _ in number_of_agents:
        #     agent_temp = []
        #     with open('output.csv', 'r') as csvfile:
        #         plots = csv.DictReader(csvfile, delimiter=',')
        #         for row in plots:
        #             if int(row['Agent']) == _:
        #                 agent_temp.append(int(row['Reward']))
        #         agent_list.append(agent_temp)

        #  The program always simulates the exact number of agents input by the user.
        #  This allows us to cleverly move agent data from agent_list to the corresponding learning agent list.
        #  Since Q-learning agents are always first, just transfer the first q_count agents on the top of agent_list.
        for _ in range(q_count):
            q_agents.append(agent_list.pop())

        for _ in range(sarsa_count):
            sarsa_agents.append(agent_list.pop())

        for _ in range(expected_sarsa_count):
            expected_sarsa_agents.append(agent_list.pop())

        for _ in range(qv_count):
            qv_agents.append(agent_list.pop())

        # Slice the nested lists to the min_timestep.
        print("Slicing nested lists...")
        q_temp = []
        for agent in q_agents:
            sliced_agent = agent[:min_timesteps]
            q_temp.append(sliced_agent)
        q_agents = q_temp

        sarsa_temp = []
        for agent in sarsa_agents:
            sliced_agent = agent[:min_timesteps]
            sarsa_temp.append(sliced_agent)
        sarsa_agents = sarsa_temp

        expected_sarsa_temp = []
        for agent in expected_sarsa_agents:
            sliced_agent = agent[:min_timesteps]
            expected_sarsa_temp.append(sliced_agent)
        expected_sarsa_agents = expected_sarsa_temp

        qv_temp = []
        for agent in qv_agents:
            sliced_agent = agent[:min_timesteps]
            qv_temp.append(sliced_agent)
        qv_agents = qv_temp

        # Convert the lists to np arrays and take the average.
        print("Converting lists and taking the average...")
        average_q = np.mean(np.array([np.array(a) for a in q_agents]), axis=0)
        average_sarsa = np.mean(np.array([np.array(b) for b in sarsa_agents]), axis=0)
        average_expected_sarsa = np.mean(np.array([np.array(c) for c in expected_sarsa_agents]), axis=0)
        average_qv = np.mean(np.array([np.array(d) for d in qv_agents]), axis=0)

        # Title of the graph.
        mpl.title("Average of " + str(q_count) + " Simulations")

        # Axis labels for the graph.
        mpl.xlabel('Time steps')
        mpl.ylabel('Total Reward')

        # In this case, every average list will be plotted against the same number of timesteps.
        timesteps = list(range(min_timesteps))

        # Plot everything with labels.
        print("Plotting....")
        mpl.plot(timesteps, average_q, label='Q-Learning')
        mpl.plot(timesteps, average_sarsa, label='SARSA')
        mpl.plot(timesteps, average_expected_sarsa, label='Expected SARSA')
        mpl.plot(timesteps, average_qv, label='QV-Learning')

        # Display the legend.
        mpl.legend()

        # Show the graph and print compute time.
        print("Graphing process took " + str(int(time.time()) - starting_time) + " seconds.")
        print("Done generating average graph.")
        mpl.show()

    # This method generates a histogram for each reinforcement learning algorithm.
    # The histogram shows how many timesteps it takes to reach a certain reward value for multiple agents.
    @staticmethod
    def histogram(agent_record, q_count, sarsa_count, expected_sarsa_count, qv_count):

        # Store the starting time for later calculating compute time.
        starting_time = int(time.time())
        print("\nGenerating histogram...")

        # The specified reward value to track.
        reward_value = 25000

        # In order to parse the output.csv file for multiple agents of each type,
        # there must be a list of numbers that correspond to the agent number in output.csv.
        number_of_agents = list(x + 1 for x in range(len(agent_record)))

        # All of the data is put in a list at first, then is filtered into a list for the specific algorithm.
        agent_list = []

        # Open the output.csv file in read mode.
        # Read all timesteps into agent_list.
        print("Reading output.csv...")
        df = read_csv('output.csv', skiprows=1, delimiter=',', )
        print("Parsing output.csv...")
        for _ in number_of_agents:
            for row in df.itertuples():
                if int(row[1]) == _ and int(row[7]) == reward_value:
                    agent_list.append(int(row[4]))
                    break

        # The data in agent_list will be split into these lists.
        q_agents = []
        sarsa_agents = []
        expected_sarsa_agents = []
        qv_agents = []

        for _ in range(q_count):
            q_agents.append(agent_list.pop())

        for _ in range(sarsa_count):
            sarsa_agents.append(agent_list.pop())

        for _ in range(expected_sarsa_count):
            expected_sarsa_agents.append(agent_list.pop())

        for _ in range(qv_count):
            qv_agents.append(agent_list.pop())

        # Histograms are generated per learning algorithm.
        if q_count > 0:
            mpl.hist(q_agents, list(x * 1000 for x in range(1, int((max(q_agents)) / 1000 + 2))), histtype="bar",
                     rwidth=0.5)
            mpl.title(str(reward_value) + " total reward with" + str(q_count) + " Q-Learning")
            mpl.xlabel("Time-step")
            mpl.ylabel("Number of Times")
            mpl.show()

        if sarsa_count > 0:
            mpl.hist(sarsa_agents, list(x * 1000 for x in range(1, int((max(sarsa_agents)) / 1000 + 2))),
                     histtype="bar",
                     rwidth=0.5)
            mpl.title(str(reward_value) + " total reward with" + str(sarsa_count) + " SARSA")
            mpl.xlabel("Time-step")
            mpl.ylabel("Number of Times")
            mpl.show()

        if expected_sarsa_count > 0:
            mpl.hist(expected_sarsa_agents,
                     list(x * 1000 for x in range(1, int((max(expected_sarsa_agents)) / 1000 + 2))),
                     histtype="bar", rwidth=0.5)
            mpl.title(str(reward_value) + " total reward with" + str(expected_sarsa_count) + " Expected SARSA")
            mpl.xlabel("Time-step")
            mpl.ylabel("Number of Times")
            mpl.show()

        if qv_count > 0:
            mpl.hist(qv_agents, list(x * 1000 for x in range(1, int((max(qv_agents)) / 1000 + 2))), histtype="bar",
                     rwidth=0.5)
            mpl.title(str(reward_value) + " total reward with" + str(qv_count) + " QV-Learning")
            mpl.xlabel("Time-step")
            mpl.ylabel("Number of Times")
            mpl.show()

        # Print compute time.
        print("Graphing process took " + str(int(time.time()) - starting_time) + " seconds.")

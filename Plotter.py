# The Plotter plots total reward vs. time-step. There are two scenarios: either one of each learning agent is graphed or
# multiple learning agents of each type are averaged and graphed. The external module responsible for graphing is
# matplotlib. Also needed is numpy, which is responsible for averaging the total rewards of multiple agents. The output
# csv generated in main.py is required to generate a graph.

import csv
import matplotlib.pyplot as mpl
import numpy as np
import time
import pandas


class Plotter(object):
    # This method only generates a graph when one of each type of learning agent is simulated.
    # That is, one Q-learning agent, one SARSA agent, one Expected SARSA agent,
    # and one QV-Learning agent. The total reward data is read from the output.csv file and appended
    # into empty lists; one for each learning agent. This data is then graphed versus the time-steps.
    @staticmethod
    def one_simulation_graph():
        print("Generating one simulation graph...")
        # The total reward per time-step is read from the output.csv file
        # and appended into lists for each agent type.
        total_reward_q = []
        total_reward_sarsa = []
        total_reward_expected_sarsa = []
        total_reward_qv = []

        # Open the file to read it.
        with open('output.csv', 'r') as csvfile:
            # Each value is separated by a comma.
            plots = csv.reader(csvfile, delimiter=',')
            # Skips header row.
            next(csvfile)
            # For each row, identify what kind of agent and according
            # to the type, append the total reward value to the
            # corresponding list.
            for row in plots:
                if row[1] == "Q-learning":
                    total_reward_q.append(float(row[6]))
                if row[1] == "SARSA":
                    total_reward_sarsa.append(float(row[6]))
                if row[1] == "Expected SARSA":
                    total_reward_expected_sarsa.append(float(row[6]))
                if row[1] == "QV-learning":
                    total_reward_qv.append(float(row[6]))

        # Title of the graph.
        mpl.title("One Simulation")

        # Axis labels for the graph.
        mpl.xlabel('Time steps')
        mpl.ylabel('Total Reward')

        # Each agent runs for a certain number of time-steps.
        # These numbers may or may not be different.
        timesteps_q = list(range(len(total_reward_q)))
        timesteps_sarsa = list(range(len(total_reward_sarsa)))
        timesteps_expected_sarsa = list(range(len(total_reward_expected_sarsa)))
        timesteps_qv = list(range(len(total_reward_qv)))

        print("Plotting...")
        # Plot the x and y values for each agent and label the plot.
        mpl.plot(timesteps_q, total_reward_q, label='Q-Learning')
        mpl.plot(timesteps_sarsa, total_reward_sarsa, label='SARSA')
        mpl.plot(timesteps_expected_sarsa, total_reward_expected_sarsa, label='Expected SARSA')
        mpl.plot(timesteps_qv, total_reward_qv, label='QV-Learning')

        # Display the legend.
        mpl.legend()

        # Show the graph on the screen.
        print("Done generating one simulation graph.")
        mpl.show()

    # This method generates a graph when there are more than one agent of each type.
    # The entire output.csv file is read and split into lists for each type of learning agent.
    # This list is then split again into individual agents per type of learning agent.
    # These nested lists are converted to numpy arrays and averaged to produce a one-dimensional
    # list that is then graphed versus the minimum time-step of all simulated agents.
    @staticmethod
    def average_graph(agent_record, q_count, sarsa_count, expected_sarsa_count, qv_count):
        starting_time = int(time.time())
        print("Generating average graph...")
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
        print("Parsing output.csv...")
        # Slow, bult in csv method.
        # for _ in number_of_agents:
        #     agent_temp = []
        #     with open('output.csv', 'r') as csvfile:
        #         plots = csv.DictReader(csvfile, delimiter=',')
        #         for row in plots:
        #             if int(row['Agent']) == _:
        #                 agent_temp.append(int(row['Reward']))
        #         agent_list.append(agent_temp)

        # Quicker pandas read csv. (6 times faster).
        df = pandas.read_csv('output.csv', skiprows=1, delimiter=',', )
        for _ in number_of_agents:
            agent_temp = []
            for row in df.itertuples():
                if int(row[1]) == _:
                    agent_temp.append(int(row[7]))
            agent_list.append(agent_temp)

        #  The program always simulates the exact number of agents input by the user.
        #  This allows us to cleverly move agent data from agent_list to the corresponding learning agent list.
        #  Since Q-learning agents are always first, just transfer the first q_count agents on the top of agent_list.
        # for _ in range(q_count):
        #     q_agents.append(agent_list[_])
        # SARSA agents are always second, so start reading agents in after q_count elements of the list, and read until
        #  the sarsa_count + q_count index. Repeat for the remaining agents.
        # for _ in range(q_count, sarsa_count + q_count):
        #     sarsa_agents.append(agent_list[_])
        # for _ in range(q_count + sarsa_count, sarsa_count + q_count + expected_sarsa_count):
        #     expected_sarsa_agents.append(agent_list[_])
        # for _ in range(sarsa_count + q_count + expected_sarsa_count,
        #                sarsa_count + q_count + expected_sarsa_count + qv_count):
        #     qv_agents.append(agent_list[_])

        # Simplified version of the above code using pop().
        for _ in range(q_count):
            q_agents.append(agent_list.pop())

        for _ in range(sarsa_count):
            sarsa_agents.append(agent_list.pop())

        for _ in range(expected_sarsa_count):
            expected_sarsa_agents.append(agent_list.pop())

        for _ in range(qv_count):
            qv_agents.append(agent_list.pop())

        print("Slicing nested lists...")
        # Slice the nested lists to the min_timestep.
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

        print("Converting lists and taking the average...")
        # Convert the lists to np arrays and take the average.
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

        print("Plotting....")
        # Plot everything with labels.
        mpl.plot(timesteps, average_q, label='Q-Learning')
        mpl.plot(timesteps, average_sarsa, label='SARSA')
        mpl.plot(timesteps, average_expected_sarsa, label='Expected SARSA')
        mpl.plot(timesteps, average_qv, label='QV-Learning')

        # Display the legend.
        mpl.legend()

        # Show the graph.
        end_time = int(time.time())
        print("Process took " + str(end_time - starting_time) + " seconds.")
        print("Done generating average graph.")
        mpl.show()

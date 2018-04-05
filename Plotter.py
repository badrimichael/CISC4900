import csv
import matplotlib.pyplot as mpl
import numpy as np


class Plotter(object):
    @staticmethod
    def one_simulation_graph():
        total_reward_q = []
        total_reward_sarsa = []
        total_reward_expected_sarsa = []
        total_reward_qv = []

        with open('output.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            next(csvfile)  # Skips header row.
            for row in plots:
                if row[1] == "Q-learning":
                    total_reward_q.append(float(row[6]))
                if row[1] == "SARSA":
                    total_reward_sarsa.append(float(row[6]))
                if row[1] == "Expected SARSA":
                    total_reward_expected_sarsa.append(float(row[6]))
                if row[1] == "QV-learning":
                    total_reward_qv.append(float(row[6]))

        mpl.xlabel('Time steps')
        mpl.ylabel('Total Reward')
        timesteps_q = list(range(len(total_reward_q)))
        timesteps_sarsa = list(range(len(total_reward_sarsa)))
        timesteps_expected_sarsa = list(range(len(total_reward_expected_sarsa)))
        timesteps_qv = list(range(len(total_reward_qv)))

        mpl.title("One Simulation of Each")
        mpl.plot(timesteps_q, total_reward_q, label='Q-Learning')
        mpl.plot(timesteps_sarsa, total_reward_sarsa, label='SARSA')
        mpl.plot(timesteps_expected_sarsa, total_reward_expected_sarsa, label='Expected SARSA')
        mpl.plot(timesteps_qv, total_reward_qv, label='QV-Learning')
        mpl.legend()
        mpl.show()

    @staticmethod
    def average_graph(agent_record, q_count, sarsa_count, expected_sarsa_count, qv_count):

        key_min = min(agent_record.keys(), key=(lambda k: agent_record[k]))
        min_timesteps = agent_record[key_min]

        number_of_agents = list(x + 1 for x in range(len(agent_record)))
        agent_list = []
        q_agents = []
        sarsa_agents = []
        expected_sarsa_agents = []
        qv_agents = []

        for _ in number_of_agents:
            temp = []
            with open('output.csv', 'r') as csvfile:
                plots = csv.DictReader(csvfile, delimiter=',')
                for row in plots:
                    if int(row['Agent']) == _:
                        temp.append(int(row['Reward']))
                agent_list.append(temp)

        for _ in range(q_count):
            q_agents.append(agent_list[_])
        for _ in range(q_count, sarsa_count + q_count):
            sarsa_agents.append(agent_list[_])
        for _ in range(q_count + sarsa_count, sarsa_count + q_count + expected_sarsa_count):
            expected_sarsa_agents.append(agent_list[_])
        for _ in range(sarsa_count + q_count + expected_sarsa_count,
                       sarsa_count + q_count + expected_sarsa_count + qv_count):
            qv_agents.append(agent_list[_])

        temp = []
        for agent in q_agents:
            sliced_agent = agent[:min_timesteps]
            temp.append(sliced_agent)
        q_agents = temp

        temp = []
        for agent in sarsa_agents:
            sliced_agent = agent[:min_timesteps]
            temp.append(sliced_agent)
        sarsa_agents = temp

        temp = []
        for agent in expected_sarsa_agents:
            sliced_agent = agent[:min_timesteps]
            temp.append(sliced_agent)
        expected_sarsa_agents = temp

        temp = []
        for agent in qv_agents:
            sliced_agent = agent[:min_timesteps]
            temp.append(sliced_agent)
        qv_agents = temp

        average_q = np.mean(np.array([np.array(a) for a in q_agents]), axis=0)
        average_sarsa = np.mean(np.array([np.array(b) for b in sarsa_agents]), axis=0)
        average_expected_sarsa = np.mean(np.array([np.array(c) for c in expected_sarsa_agents]), axis=0)
        average_qv = np.mean(np.array([np.array(d) for d in qv_agents]), axis=0)

        mpl.xlabel('Time steps')
        mpl.ylabel('Total Reward')

        timesteps = list(range(min_timesteps))

        mpl.title("Average of " + str(q_count) + " Simulations")
        mpl.plot(timesteps, average_q, label='Q-Learning')
        mpl.plot(timesteps, average_sarsa, label='SARSA')
        mpl.plot(timesteps, average_expected_sarsa, label='Expected SARSA')
        mpl.plot(timesteps, average_qv, label='QV-Learning')
        mpl.legend()
        mpl.show()

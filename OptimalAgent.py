# The optimal agent moves from one state to another without any obstacles.
# It will always move to the next state in the environment nodes list.
# Since it is guaranteed to move forward, it is guaranteed to obtain rewards.

from Agent import Agent


class OptimalAgent(Agent):

    # See Agent.py
    # The optimal agent is guaranteed to move
    # from one state to another and is incapable
    # of surging forward.
    # WILL ALWAYS GET TO END UNLESS MORE NODES THAN NUMBER OF STEPS!
    def traverse(self, environment, index, csv_writer):
        print("Optimal Agent:")
        time = 0
        for episode in range(self.number_of_episodes):
            self.current_state = environment.starting_node
            reward = 0
            terminal_state = False
            for step in range(self.number_of_steps):
                time = time + 1
                self.current_state = self.current_state.next
                print("Agent moved to node " + str(self.current_state.state))
                if self.current_state.reward is True:
                    reward = 100
                    terminal_state = True
                self.write_to_csv(csv_writer, episode + 1, self.current_state, reward, time, 1, index)
                if terminal_state:
                    print("Agent obtained reward.")
                    break
            print("Episode " + str(episode + 1) + ": " + "Reward = " + str(reward))
            print("Steps taken: " + str(step + 1) + "\n")
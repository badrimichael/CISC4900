# The optimal agent moves from one state to another without any obstacles.
# It will always move to the next state in the environment nodes list.
# Since it is guaranteed to move forward, it is guaranteed to obtain rewards.

from Agent import Agent


# See Agent.py.
# Incapable of surging therefore zero probability
# to surge forward.
class OptimalAgent(Agent):
    probability_of_surge = 0
    current_state = None
    reward = False

    # Constructor to initialize the variables needed for the Optimal Agent.
    def __init__(self):
        # Actions list holds all of the possible actions. For an environment of m states, the actions are 0 - m-1.
        self.actions = []

        # Number of episodes to attempt. This can be any number.
        self.number_of_episodes = 25

        # The number of steps (actions) to take per episode. This can be any number, does not have to equal number
        # of episodes.
        self.number_of_steps = 50

    # See Agent.py
    # The optimal agent is guaranteed to move
    # from one state to another and is incapable
    # of surging forward.
    # WILL ALWAYS GET TO END UNLESS MORE NODES THAN NUMBER OF STEPS!
    def traverse(self, environment, index, csv_writer):
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
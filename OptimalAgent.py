# The optimal agent moves from one state to another without any obstacles.
# It will always move to the next state in the environment nodes list.
# Since it is guaranteed to move forward, it is guaranteed a reward.

from Agent import Agent


# See Agent.py.
# Incapable of surging therefore zero probability
# to surge forward.
class OptimalAgent(Agent):
    probability_of_surge = 0
    current_state = None
    reward = False

    # See Agent.py.
    def set_current_state(self, current_state):
        self.current_state = current_state

    # See Agent.py.
    def set_reward(self, reward_value):
        self.reward = reward_value

    # See Agent.py
    # The optimal agent is guaranteed to move
    # from one state to another and is incapable
    # of surging forward.
    def traverse(self, environment):
        self.current_state = environment.starting_node
        print("Optimal agent entered environment. (State 0)")
        while self.reward is False:
            self.set_current_state(self.current_state.next)
            self.set_reward(self.current_state.reward)
            print("Optimal agent moved to state " + str(self.current_state.state) + ".")
        else:
            print("Optimal agent obtained reward.\n")

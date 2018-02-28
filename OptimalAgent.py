# The optimal agent moves from one state to another without any obstacles.
# It will always move to the next state in the environment nodes list.
# Since it is guaranteed to move forward, it is guaranteed a reward.

from Agent import Agent


# See Agent.py.
# Incapable of surging therefore zero probability
# to surge forward.
class OptimalAgent(Agent):
    probability_of_surge = 0
    current_node = None
    reward = False

    # See Agent.py.
    def set_current_node(self, current_node):
        self.current_node = current_node

    # See Agent.py.
    def set_reward(self):
        self.reward = True

    # See Agent.py
    # The optimal agent is guaranteed to move
    # from one state to another and is incapable
    # of surging forward.
    def traverse(self, environment):
        self.current_node = environment.starting_node
        print("Optimal agent entered environment. (State 0)")
        while self.reward is False:
            self.set_current_node(self.current_node.next)
            self.reward = self.current_node.reward
            print("Optimal agent moved to state " + str(self.current_node.state) + ".")
        else:
            print("Optimal agent obtained reward.\n")

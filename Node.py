# The Node class describes doubly-linked nodes that are the building blocks of an environment. Nodes are simple,
# they point to the node in front and behind them, hold a number representing their state, and a boolean that
# indicates whether or not the node has a reward. Only the last node in the environment has a reward for an agent.
# A basic node is only given a state through the constructor. The previous, next, and reward fields are determined
# by the environment.


class Node(object):
    state = None
    next = None
    prev = None
    reward = False

    # Constructor that assigns a state
    # to a node.
    def __init__(self, state):
        self.state = state

    # Set methods for nodes.
    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    # Set reward of node to True.
    def add_reward(self):
        self.reward = True

    # Print the node's state.
    def print(self):
        print("Node " + str(self.state))

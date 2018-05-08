# The Node class describes a node intended for a singly-linked list that are the building blocks of an environment.
# Nodes are simple: they point to the node in front of them, hold a number representing their state,
# and a boolean that indicates whether or not the node has a reward. Some nodes have reward values and others do not.
# A basic node is only given a state through the constructor. The next, and reward fields are determined
# by the environment.


class Node(object):
    state = None
    next = None
    reward = False

    # Constructor that assigns a state
    # to a node.
    def __init__(self, state):
        self.state = state

    # Set next node in sequence.
    def set_next(self, next):
        self.next = next

    # Set reward of node to True.
    def add_reward(self):
        self.reward = True

    # Print the node's state.
    # Like overriding toString() in Java.
    def __str__(self):
        return "Node " + str(self.state)

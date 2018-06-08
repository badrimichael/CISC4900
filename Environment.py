# The environment class creates an environment of Nodes (see Node.py) based on Markov Decision Processes or finite
# automata. Nodes are automatically created based on the constructor argument. These nodes are held in a list of nodes.


from Node import Node
import random


class Environment(object):
    # Empty list of nodes to be populated.
    nodes = []

    # Empty list of possible actions that can be taken by an agent in this particular environment.
    actions = []

    # Starting node of a nonexistent environment is None.
    starting_node = None

    # Probability of randomly turning an action of 1 to an action of 0.
    # This value must be a float between 0 and 1 if you want actions to change.
    random_fail_percentage = 0

    # Defines the correct action needed to advance a state in the environment.
    # It starts off as 1, and can only be changed by the environment if learned_reward_value triggers a change.
    correct_action = 1

    # Defines whether or not the agent has learned the correct sequence.
    # Can be any positive integer.
    learned_reward_value = 0

    # Defines a probability that the action will change per time step.
    random_action_change_percentage = 0

    # Constructor that instantiates nodes based on num_of_states
    # argument. The next field of each node is determined here.
    # Reward is added to the final node in the environment.
    # The nodes and actions lists are required in the constructor, so their contents can be serialized.
    def __init__(self, num_of_states, random_fail_percentage, learned_reward_value, random_action_change_percentage):
        self.nodes = []
        self.actions = []
        nodes = self.nodes
        for state_num in range(num_of_states):
            nodes.append(Node(state_num))
        for node in nodes:
            if node.state == 0:
                node.set_next(nodes[1])
            elif node.state == num_of_states - 1:
                node.add_reward()
            else:
                node.set_next(nodes[node.state + 1])
        self.starting_node = nodes[0]
        self.random_fail_percentage = random_fail_percentage
        self.learned_reward_value = learned_reward_value
        self.random_action_change_percentage = random_action_change_percentage
        for node in self.nodes:
            self.actions.append(node.state)

    # Processes environment obstacles that rely on terminal state being reached.
    def process_terminal_state_obstacles(self, total_reward):
        if self.learned_reward_value > 0:
            if total_reward % self.learned_reward_value == 0:
                self.set_correct_action(self.choose_random_action())

    # Set method for the correct action.
    def set_correct_action(self, new_action):
        self.correct_action = new_action

    # When called, this method chooses a random action to replace the current correct action.
    # The possible actions that can be chosen are all actions in the list except the current correct action.
    def choose_random_action(self):
        new_action = self.correct_action
        while new_action == self.correct_action:
            new_action = random.choice(self.actions)
        print("Action changed.")
        return new_action

    def random_action_change(self):
        if random.uniform(0, 1) < self.random_action_change_percentage:
            self.set_correct_action(self.choose_random_action())

    # Prints each node in nodes list.
    def print(self):
        for node in self.nodes:
            print(node)

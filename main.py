# This program creates an environment comprised of nodes and different agents to navigate these environments.
# The goal of the agent is to obtain the reward on the last node in the sequence. Initially, random numbers determine
# whether or not an agent progresses through the environment. Later on, the agent will learn from previous experiences
# using different learning algorithms to reduce the reliance of luck in obtaining the reward.

# This purpose of this main method is to be as simple as possible. The environment(s) and agent(s)
# will be created here and agents can be reused for multiple environments (see Agent.py and Environment.py).
# This follows standard object oriented programming styles in which the main method tends to be the least busy.
# This current main method is essentially a test to ensure environments are created properly and agents act as they
# were intended to.

from Environment import Environment
from Agent import Agent


# Create an environment consisting of 10 nodes.
environment = Environment(10)
# Creates an agent with probability of surging as the argument.
agent = Agent(0.01)
# Previously created agent begins traversal of previously created environment.
agent.traverse(environment)



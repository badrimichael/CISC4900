# CISC4900
Simulations of Reinforcement Learning in an Ecological Task (Simulation Program) written in Python.

CISC 4900 – SPRING 2018

Student Information

Name: MICHAEL BADRI

E-Mail Address: badrimichael@gmail.com

Date: 5/13/18

Supervisor Information

Name: STEFANO GHIRLANDA    

Prior Relationship to Student: NONE

Phone Number: xxxxxxxxxxx

Address: xxxxxxxxxxxxxx

PROJECT TITLE

Simulations of Reinforcement Learning in an Ecological Task

INTRODUCTION

 This overall goal of this project is to simulate different reinforcement learning algorithms and compare the results. QV-learning is an underresearched and (relatively) unexplored reinforcement learning algorithm that is believed to model, to a certain degree, how animals learn because it utilizes parameters that are often ignored in other algorithms. We want to compare the performance of QV-learning with different, more studied reinforcement learning algorithms in an environment that models the ecological task of chaining.

DESCRIPTION OF PROBLEM

Animals learn behavioral sequences through a process called chaining, where smaller, less meaningful behaviors are linked together to form more complex behaviors. The rewards in their environment act as the motivating factors to learn these behaviors, so that given a familiar environment, an animal would be able to consistently obtain the reward. For example, a reward can be something that prolongs the survival of the animal, such as food or shelter. It must piece together different behaviors to learn how to successfully forage for food; such as locating, obtaining, and finally: eating. Depending on the environment, the animal may have to dig underground or pick fruit from a tree; but once it learns how to perform one of these behaviors, it can consistently obtain fruit from the same environment (as long as it has more food). We can model this task using a Markov decision process and it would look something like this:


**Figure 1:** A, B, C, D are states, integers are actions, and arrows indicate the resulting movement of a chosen action.

The action assigned to 1 is a desired action because it leads to the next state that is closer to state D, which contains a reward. The action assigned to 0 is an undesired action since it only leads back to the beginning of the sequence. In addition to modeling this task, we can simulate it using reinforcement learning algorithms. One such algorithm is QV-learning, which is believed to be a good model for how animals learn because this algorithm takes the value of a state into consideration when learning, a parameter that other algorithms may ignore. We would like to simulate QV-learning alongside other reinforcement learning algorithms in an environment modeled after chaining and observe the results.

DESCRIPTION OF SOLUTION

We simulate chaining with reinforcement learning algorithms.Reinforcement learning is a type of machine learning, where a software agent attempts to learn how to traverse an environment through gaining experience. The experience is generated with the Bellman equation implemented via dynamic programming and stored in some data structure, such as a dictionary. Every time the agent &quot;decides&quot; to take action, it refers to this dictionary to determine the best possible action to take. After the action is performed, the dictionary value corresponding to the taken action is updated positively or negatively depending on whether or not that action led to a reward. The agent has finally learned the behavior when it can move from the starting state to the final, terminal state (containing the reward) based on pure experience.

The agents traverse environments that are modeled after Markov decision processes (Figure 1). Each environment is a sequence of states (similar to a linked list), where the correct action triggers the agent&#39;s movement to the next state and where an incorrect action returns the agent to the starting state. Upon reaching a terminal state or exhausting their allotted steps, the agent returns to the beginning of the environment with the knowledge obtained from previous traversals; ready to commence the next episode (traversal). If enough episodes are simulated, the agent will learn the correct sequence of actions needed reach the reward at the end of the environment.

To determine whether or not a certain reinforcement learning algorithm performs better or worse than another, a record is kept of all actions during a simulation and obstacles are added to the environment. The record is used to generate graphs necessary for analysis, meanwhile the obstacles force the agents to adapt to changes that impede learning. Combined, these two aspects of the software help us determine QV-learning&#39;s effectiveness in traversing an environment modeled after chaining. It is important to note that QV-learning is unique because its implementation of the Bellman equation relies on a parameter known as state value; this value is closer to 1 if the agent is more likely to obtain a reward by starting on that state, otherwise the value is much lower than 1.

**Figure 2:** Value parameter stored in v\_table in QVAgent.py, Bellman equation for QV-learning.

WORK PERFORMED

 Two programs have been completed and documented. The first program is a Python program that simulates the traversal of reinforcement learning agents and benchmark agents through a random walk environment of _n_ states modeled after a Markov decision process. The following reinforcement learning algorithms can be utilized by learning agents: Q-learning, SARSA, Expected SARSA, and of course, QV-learning. When the simulation program is initialized, the user can specify how many agents can be simulated and how many states the environment will contain. (The program has been tested to successfully simulate 4000 total agents, with one agent completing its simulation every second. If obstacles are added to the environment, this time increases.) To reduce learning time, overall simulation running time, and output file size, we specify an entry pattern. An entry pattern changes the way a learning agent enters the environment; in this case, we give a learning agent a 10% chance to jump to a random state in the environment, excluding the terminal state at the end containing the reward. This drastically speeds up the learning time and makes sense in the context of chaining, since this introduces a factor of &quot;luck.&quot; Optional obstacles that can be added before the simulation begins are: a user defined probability that a correct action will be changed to an incorrect action and a user defined total reward interval that will change the current correct action into a different action, forcing the learning agent to learn a new sequence of actions to obtain a reward. The simulation program also records every movement taken by an agent into an output CSV file, to be used by the second program. Simulations with and without obstacles have been recorded for 400, 800, 2000, and 4000 total agents.

 The second program is written in R and utilizes ggplot2 to generate histograms and frequency polygons. The user adds output files to the program directory and runs the script, which parses the file. The first output is a histogram for each learning algorithm. The histogram shows how long it takes for a certain reinforcement learning algorithm to reach a user defined reward value. The next and final output is a frequency polygon that plots data from each of the histograms on a single set of axes. This script can be used repeatedly for different output files and the user can easily edit aspects of the graphs due to the versatility of ggplot2.

RESULTS (Full resolution graphs available on 4900-R repository on GitHub)

SUMMARY

 It is worth looking into QV-learning as it bears some resemblance to the way animals acquire behaviors. The potential benefits from studying such an algorithm could be numerous for applications of psychology and computer science. By comparing the performance of QV-learning to the performance of more studied reinforcement learning algorithms, we can observe where it currently stands among them. In the context of an ecological task such as chaining, QV-learning suffers when the environment has many obstacles. However, in a less complicated environment, it is comparable to Q-learning and Expected-SARSA. The currently completed programs can be expanded further to encompass more learning algorithms or more varied environments to further test the abilities of QV-learning.

TASKS PROPOSED, BUT NOT COMPLETED

1.) Obtaining actual animal learning data to compare with simulation results.

- This turned out to be unnecessary because Professor Ghirlanda and I refined the scope of the project to simply compare the results of four different reinforcement learning algorithms to each other. This refined idea is more relevant to my CISC background and easier to implement.

2.) Creating more varied environments, with multiple rewards and paths.

- The ecological task we are simulating requires only a &quot;random walk environment.&quot; Such an environment is detailed in Chapter 6 of Barto and Sutton&#39;s _Reinforcement Learning: An Introduction._ There was no need for different environments; work began on them but the implementation was abandoned.

**All other tasks specified in earlier reports were successfully implemented.**

SOURCES

Enquist, M., Lind, J., &amp; Ghirlanda, S. (2016). The power of associative learning and the ontogeny of optimal behaviour. _Royal Society Open Science,_ _3_(11), 160734. doi:10.1098/rsos.160734

Seijen, H. V., Hasselt, H. V., Whiteson, S., &amp; Wiering, M. (2009). A theoretical and empirical analysis of Expected Sarsa. _2009 IEEE Symposium on Adaptive Dynamic Programming and Reinforcement Learning_. doi:10.1109/adprl.2009.4927542

Sutton, R. S., &amp; Barto, A. G. (2012). _Reinforcement learning: An introduction_. Cambridge, MA: The MIT Press.

Wiering, M. A., and D. Leone. _QV(Lambda)-Learning: A New On-Policy Reinforcement Learning Algorithm_. 2005.

Wiering, M. A., &amp; Hasselt, H. V. (2009). The QV family compared to other reinforcement learning algorithms. _2009 IEEE Symposium on Adaptive Dynamic Programming and Reinforcement Learning_. doi:10.1109/adprl.2009.4927532

PROGRAM AND SYSTEM DOCUMENTATION

**1.)** Simulation program written in Python 3.6.4: [https://github.com/badrimichael/CISC4900](https://github.com/badrimichael/CISC4900)

- Includes: Agent.py, Environment.py, ExpectedSarsaAgent.py, LearningAgent.py, Node.py, OptimalAgent.py, QAgent.py, QVAgent.py, RandomAgent.py, SarsaAgent.py, main.py.

- This program requires the external module: NumPy.

- The source code is very well documented in the repository.

Input

The program prompts the user to input integers that specify how many agents of each type to simulate. The user can enter any integer greater than or equal to 0 for the agent prompts. After the number of agents are specified, the user must input the size of the environment; the user must enter an integer greater than 2. The simulation begins after the size of the environment is specified and the user presses the ENTER key. The simulation runs until all agents have finished traversing the environment.

**Figure 7** : Sample input from CLI.

Output

Output is a CSV file that includes the following header information: Agent number, Agent type, episode number, time-step, current state, total reward, action chosen. Console output consists of agent movement, total agents successfully simulated, and simulation running time in seconds.


**Figure 8** : Sample output from console.

**2.)** Graphing program written in R: [https://github.com/badrimichael/CISC4900-R](https://github.com/badrimichael/CISC4900-R)

- Includes: frequency polygon.R, histogram.R.

- These scripts require the external module: ggplot2.

- Source code is commented in the repository.

Input

- Relocate or copy output CSV files from the Python simulation program directory (that only contains simulation data of learning agents) into directory containing R scripts and run each script once.

- The user may edit the path or file name of the output CSV file in the script, but in its current state, the script checks the directory it is located in for a file named &#39;output.csv.&#39;

- The user may edit the parameter called &#39;reward\_value&#39; in either script to generate graphs that correspond to that reward value. Note that any previous data frames must be overwritten or deleted.

- There may be errors that claim that there are Inf (empty) values for certain agents, this simply means that the agent completed its entire simulation without obtaining a reward value equal to the reward\_value parameter. The ggplot2 module automatically discards these values when graphing, so the user needs to take no further action.

Output

- Output is one histogram per learning algorithm and one frequency polygon per output file.

- These graphs are automatically generated as they are the final lines of code in the script. There is no console output.

Sample output for Program 1 from output.csv:

Agent, Agent Type, Episode, Time, State, Action, Reward
1,Q-learning,1,1,0,0,0

1,Q-learning,1,2,0,3,0

1,Q-learning,1,3,0,0,0

1,Q-learning,1,4,0,0,0

1,Q-learning,1,5,0,0,0

1,Q-learning,1,6,0,0,0

1,Q-learning,1,7,0,0,0

1,Q-learning,1,8,0,0,0

1,Q-learning,1,9,0,0,0

1,Q-learning,1,10,0,0,0

1,Q-learning,1,11,0,0,0

1,Q-learning,1,12,0,0,0

1,Q-learning,1,13,0,0,0

1,Q-learning,1,14,0,0,0

…

20,QV-learning,497,7228,3,1,44900

20,QV-learning,497,7229,4,0,45000

20,QV-learning,498,7230,1,1,45000

20,QV-learning,498,7231,2,1,45000

20,QV-learning,498,7232,3,1,45000

20,QV-learning,498,7233,4,0,45100

20,QV-learning,499,7234,1,1,45100

20,QV-learning,499,7235,2,1,45100

20,QV-learning,499,7236,3,1,45100

20,QV-learning,499,7237,4,0,45200

20,QV-learning,500,7238,1,1,45200

20,QV-learning,500,7239,2,1,45200

20,QV-learning,500,7240,3,1,45200

20,QV-learning,500,7241,4,0,45300


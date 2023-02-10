Agent takes an action and there is either a reward or punishment from that environment.

# Challenges

## Exploration-Exploitation Dilemma
- Exploration means the agent is exploring potential hypotheses for how to choose actions, which inevitably will lead to some negative reward from the environment.
- Exploitation means how the agent exploits the limited knowledge about what it has already learned.
- The challenge is in how the agent balances the two competing requirements to achieve optimal results

# Unsupervised Learning
- Categorized and unlabelled data
- Useful for these types of problems:
	- Clustering: identifying similarities in groups
	- Anomaly detection: Identifying abnormalities in our data
- Often used to preprocess data, for example during the EDA stage, it can be used to cluster groups of data.

# Episodic vs Continuing Tasks
## Episodic Tasks
- Tasks that end at some time step $T$
- Each sequence from the initial state and action to the end is called an episode
- The agent can then review the cumulative reward it received for that episode, learn from this new information, and adjust its parameters accordingly.

## Continuing Tasks
 - Tasks where the interaction continues without an endpoint
	 - Ex: Trading in the financial markets
- In this case, the agent must learn how to operate in its environment and simultaneously maximize it's expected reward


# Bellman Equation
The question to solve is:
Given the state an agent is in, assuming it takes the best possible action now and at each subsequent step, what long-term reward can it expect?

The Bellman Equation helps us evaluate the expected reward relative to the advantage or disadvantage of each state.


## Bellman Equation for Deterministic Environments
- $V(s) = max_a(R(s,a) + \gamma V(s'))$
- The value of a given state is equal to max action, which means of all the available actions in the state we're in, we pick the one that maximizes value.
- We take the reward of the optimal action $a$ in state $s$ and add a multiplier of gamma, which is the discount factor which diminishes our reward over time.
- Each time we take an action we get back the next state $s'$
- Then take $s'$ and put it back into the value function $V(s)$
- We continue until we get the terminal state and we know the value of the state we're in, assuming we choose the optimal action.
- The catch is we have to know what the optimal action which will maximize the expected long term rewards is at each step
- Before deep learning, this was done by trying out all actions in a huge search tree.
- Deep neural networks instead, let us estimate the value of the state and intelligently guess which action will maximize it.

# Discount Factor ($\gamma$)
- If $\gamma$ = 1, meaning there is no discounting, we have the problem of **sparse rewards**
- Every other state that isn't a reward state is 0, so with no discount all the states end up with equal values of 1 and don't teach the model anything
- A lower value encourages short-term thinking
- A higher value emphasizes long-term rewards
- Successful values often range from 0.9 to 0.99

# Reinforcement Learning of Optimal Policies
In the RL framework, we do not know the MDP model


Goal: Learn the optimal policy (mapping)
$$\pi^*: S \rightarrow A* $$
that maximizes some combination of future reinforcements (rewards) received over time.
There are two basic approaches:
## Model based learning
- Learn the MDP model (probabilities, rewards) first
- Solve the MDP afterwards
- One way to solve such a problem is to first learn the MDP and then solve it using algorithms such as value-iteration or policy-iteration, both using the  Bellman Equation
## Model-free learning
- Learn how to act directly
- No need to learn the parameters of the MDP

# Valuation Models (Quantify how good the mapping is)
## Finite Horizon Model
- $E(\sum^{T}_{t=0}r_t) ]$ 
- Time horizon: $T>0$

## Infinite horizon discounted model
-  $E(\sum^{\infty}_{t=0}\gamma^t r_t)$ 
- $\[ \sum_{n=1}^{\infty} 2^{-n} = 1 \]$

# Markov Decision Processes (MDP)
An important framework for representing the reinforcement learning problem of an AI agent learning in an environment. This framework allows actions and rewards. MDP is defined by 5 components
- A set of possible states
- An initial state
- A set of actions
- A transition model
- A reward function
The goal is to find a **policy** that selects the action with the highest reward.
The agent perceives its environment by having information about the state $s$ at each time step $t$.
An important feature of reinforcement learning is that an agent's actions may themselves have an impact on the state of the environment. 
- For example, placing a buy or sell order in the financial markets has an impact on the price of the instrument.
- This creates a feedback loop in which the agent's actions may themselves have an impact on the state of the environment. 


# Q-Learning

But how, realistically, would an AI-driven agent make the best possible decision in every situation within the constraints of their environment?

The answer would be to simply choose the action that would yield the highest reward in the context of their **state.** In more complex environments, the state context is extremely important; consider, for instance, a character in a game trying to decide whether or not to jump. If they were in front of a short wall, jumping would allow them to clear it and progress in the game. However, if they were in front of a cliff, they would die. The set of total states can also be called the **observation space**, as the context is often determined by what the agent can “observe” as its setting.

Based on these two spaces, we can now create a 2-way table of actions and states: imagine every state being its own row, and each state being a vector of actions that the agent can take in that state.


https://ucladatares.medium.com/rlette-casino-roulette-through-reinforcement-learning-67e865843f0d
https://towardsdatascience.com/introduction-to-reinforcement-learning-markov-decision-process-44c533ebf8da

# MDP vs Q-Learning
A Markov Decision Process (MDP) models a sequential decision-making problem. The most important characteristic of an MDP is that the state transition and reward function depend on only the current state and the applied action (for more details about MDPs: [Markov decision process - Wikipedia](https://en.wikipedia.org/wiki/Markov_decision_process "en.wikipedia.org")).

Notice that the model is composed of a reward function R and a state transition function P. In case you have those two functions (that is, you can predict which reward will be received and which will be the next state for any state-action pair), the MDP can be solved through an Dynamic Programming method.

However, for most cases, we cannot precisely predict R and P. If those functions are not known, Q-Learning is an algorithm that can be use to solve MDPs with unknown reward and transition functions.

The main idea of Q-Learning is to “explore” all possibilities of state-action pairs and estimate the long-term reward that will be received by applying an action in a state (the Q(s,a) value). Eventually, Q-Learning converges to the optimal actuation given some restrictions.
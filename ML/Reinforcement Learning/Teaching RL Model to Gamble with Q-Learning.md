---
title:  "Teaching RL Model to Game with Q Learning"
tags:
- 
created: 2023-02-04
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Teaching RL Model to Gamble with Q Learning
- Create simulation environment
- Algorithm uses a set of S states for each simulating scenario with a set of A actions.
- An agent takes these actions to permeate through the states

# Off-policy vs On-policy learning
First of all, there's no reason that an agent has to do the _greedy action_; Agents can _explore_or they can follow _options_. This is not what separates on-policy from off-policy learning.

The reason that Q-learning is off-policy is that it updates its Q-values using the Q-value of the next state 𝑠′ and the _greedy action_ 𝑎′. In other words, it estimates the _return_ (total discounted future reward) for state-action pairs assuming a greedy policy were followed despite the fact that it's not following a greedy policy.


https://stats.stackexchange.com/questions/184657/what-is-the-difference-between-off-policy-and-on-policy-learning

First of all, what does policy (denoted by 𝜋) actually mean?  
Policy specifies an action 𝑎a, that is taken in a state 𝑠s (or more precisely, 𝜋 is a probability, that an action 𝑎a is taken in a state 𝑠s).

Second, what types of learning do we have?

1.  Evaluate 𝑄(𝑠,𝑎) function: predict sum of future discounted rewards, where 𝑎a is an action and 𝑠s is a state.
2.  Find 𝜋 (actually, 𝜋(𝑎|𝑠)), that yields a maximum reward.

Back to the original question. On-policy and off-policy learning is only related to the first task: evaluating 𝑄(𝑠,𝑎)).

The difference is this:  
In **on-policy** learning, the 𝑄(𝑠,𝑎) function is learned from actions that we took using our current policy 𝜋(𝑎|𝑠).  
In **off-policy** learning, the 𝑄(𝑠,𝑎) function is learned from taking different actions (for example, random actions). We don't even need a policy at all!

**On-policy** methods estimate the value of a policy while using it for control. 

In **off-policy** methods, the policy used to generate behaviour, called the _behaviour_ policy, may be unrelated to the policy that is evaluated and improved, called the _estimation_ policy. 

An advantage of this separation is that the estimation policy may be deterministic (e.g. greedy), while the behaviour policy can continue to sample all possible actions.

The letter Q stands for Quality and the learning model is based on a Q table (Quality table) which is the policy of actions that the model can use in the environment for each state. Thus, we have a table [state, action] that represents a policy where each action has a quality value (Q value) for each state.
![[Pasted image 20230204154315.png]]

# Q-learning
Q-learning is a Reinforcement Learning off policy model that aims to find the best action to take based on the current state, in this case without a defined action policy. This model is considered an off-policy model because the Q-learning function learns through actions that are outside the current policy, in other words, its learning follows in an exploratory way by taking random actions to create an action policy that maximizes the total reward of the episode.
# Implementation

```python

```



# Source
https://levelup.gitconnected.com/reinforcement-learning-teaching-the-machine-to-gamble-with-q-learning-bc6790ee66c2

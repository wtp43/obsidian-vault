---
dg-publish: true
title:  "Reinforcement Learning"
tags:
- ml
created: 2023-02-05
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# Reinforcement Learning Environment
- The agent's world in which it lives and interacts
- The agent can't influence the rules/dynamics of the environment by those actions

[![../../_images/AE_loop_dark.png](https://gymnasium.farama.org/_images/AE_loop_dark.png)](https://gymnasium.farama.org/_images/AE_loop_dark.png)

# Action Space
- Set of actions that are permissible for the agent in a given environment
## Discrete Action Space
- Move up, down
## Continuous Action Space
- bet amount (percentage)

# Types of Environments
## Deterministic Environment
- The next state can always be determined based on the current state and agent's action

## Stochastic Environment
- Next state cannot always be determined by the current state performing a certain action
- Ex: Suppose our agent's world of driving a car is not perfect.
	- When an agent applies a break, there is a small probability that the break may fail and the car does not stop.

## Single Agent vs Multi Agent

## Fully Observable vs Partially Observable
- In a fully observable environment, the agent is always aware of the complete state of the environment at any given point in time. (Ex: Chess)
- In a partially observable environment, the agent cannot always see the complete state of the environment at any given point in time. (Ex: Poker)

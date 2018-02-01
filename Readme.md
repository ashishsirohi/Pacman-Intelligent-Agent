The Pacman Projects
===================

### Intro
Fall 2017 semester at ASU was lit for me as I took the Introduction to Artificial Intelligence course taught by Prof. S. Kambhampati. I thoroughly enjoyed all the AI theory we learnt and along the way did some cool projects and few of them were [The Pacman Projects](http://ai.berkeley.edu/project_overview.html) created by the [University of California, Berkeley](http://berkeley.edu/).

![Animated gif pacman game](http://ai.berkeley.edu/images/pacman_game.gif)

### Project 1: Search in Pacman
From the [project 1 page](http://ai.berkeley.edu/search.html): *In this project, your Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. You will build general search algorithms and apply them to Pacman scenarios.*

In this part, I implemented the following search Algorithms:</br>
Breadth First Search
Depth First Search
Uniform Cost Search
A* Search with Heauristic

Some sample scenarios to try with are:

```
$ python pacman.py -l bigMaze -p SearchAgent -a fn=dfs -z .5
$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

$ python pacman.py -l openMaze -p SearchAgent -a fn=dfs -z .5
$ python pacman.py -l openMaze -p SearchAgent -a fn=bfs -z .5

$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
$ python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

$ python pacman.py -l trickySearch -p SearchAgent -a fn=bfs,prob=FoodSearchProblem
$ python pacman.py -l trickySearch -p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic
```

### Project 2: 
From the [project 2 page](http://ai.berkeley.edu/multiagent.html): *In this project, you will design agents for the classic version of Pacman, including ghosts. Along the way, you will implement both minimax and expectimax search and try your hand at evaluation function design.*

Some sample scenarios to try with are:
```
python pacman.py --frameTime 0 -p ReflexAgent -k 2
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
```


### Project 3: Reinforcement Learning
From the [project 3 page](http://ai.berkeley.edu/reinforcement.html): *In this project, you will implement value iteration and Q-learning. You will test your agents first on Gridworld (from class), then apply them to a simulated robot controller (Crawler) and Pacman.*

Some sample scenarios to try with are:

```
$ cd pacman-projects/p3_reinforcement_learning

$ python gridworld.py -a q -k 100 
$ python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid
$ python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic
```
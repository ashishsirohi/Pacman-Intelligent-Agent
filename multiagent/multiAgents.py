 # multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        """print "successorGameState", successorGameState
        print "newPos", newPos
        print "newFood", newFood
        print "newGhostStates", newGhostStates
        print "newScaredTimes", newScaredTimes"""

        """Initially score is zero"""
        score = 0
        for ghost in newGhostStates:
            """Calculating manhattan distance between the new position and ghost new position"""
            dist = manhattanDistance(newPos, ghost.getPosition())
            if dist<=1:
                """Ghost is within 1 move, checking for scared timer"""
                if ghost.scaredTimer==0:
                    """Based in pacman ghost rules in pacman.py, -500 point if scared timer is off and ghost is on the next move"""
                    score -= 500
                else:
                    """Gets 200 points if scared timer is on and pacman and ghost collides"""
                    score += 200
            else:
                if ghost.scaredTimer > 0:
                    """trying to go towards ghost becase scared timer is on"""
                    score += 200.0/dist

        oldFood = currentGameState.getFood()
        oldFoodList = oldFood.asList()
        for food in oldFoodList:
            """Calculating manhattan distance between the old food position and pacman new position"""
            dist = manhattanDistance(food, newPos)
            if dist==0:
                """That was the last food, pacman gets maximum point as game is over else gets 10 points for eating 1 food"""
                if currentGameState.getNumFood == 0:
                    score += 500
                else:
                    score += 10
            else:
                """trying to go towards the food"""
                score += 1.0/dist

        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        #print gameState.getNumAgents()
        #print self.depth
        "Finding and returning best move"
        bestMove = self.maxFunc(gameState, self.depth)
        return bestMove
    "Function to find the perform the max step"
    def maxFunc(self, gameState, depth):
        if self.terminalCheck(gameState, depth):
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(self.index)
        scores = []
        for move in legalMoves:
            scores.append(self.minFunc(gameState.generateSuccessor(self.index, move), 1, depth))

        bestScore = max(scores)
        if depth == self.depth:
            "Based on the best available score, finding move"
            indices = [index for index in range(len(scores)) if scores[index] == bestScore]
            return legalMoves[indices[0]]
        return bestScore
    "function to perform the min step"
    def minFunc(self, gameState, agent, depth):
        if self.terminalCheck(gameState, depth):
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(agent)
        scores = []
        if(agent < gameState.getNumAgents() - 1):
            for move in legalMoves:
                scores.append(self.minFunc(gameState.generateSuccessor(agent, move), agent+1, depth))
        else:
            for move in legalMoves:
                scores.append(self.maxFunc(gameState.generateSuccessor(agent, move), depth-1))
        return min(scores)

    "function to check terminal state condition"
    def terminalCheck(self, gameState, depth):
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return True
        else:
            return False


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        """legalMoves = gameState.getLegalActions(0)
        scores = [self.minFunc(gameState.generateSuccessor(0,move), 1, self.depth, float("-inf"), float("inf")) for move in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)
        return legalMoves[chosenIndex]"""
        #return self.maxFunc(gameState, self.depth, float("-inf"), float("inf"))
        legalMoves = gameState.getLegalActions(0)
        score = float("-inf")
        index = 0
        bestindex = 0
        alpha = float("-inf")
        beta = float("inf")
        "Based on alpha-beta, finding best move and updating alpha-beta accordingly"
        for move in legalMoves:
            interscore = self.minFunc(gameState.generateSuccessor(0, move), 1, self.depth, alpha, beta)
            if score <= interscore:
                score = interscore
                bestindex = index
            if score >= beta:
                return legalMoves[bestindex]
            alpha = max(alpha,score)
            index = index + 1
        return legalMoves[bestindex]

    "Function to find the perform the max step wiht alpha-beta pruning"
    def maxFunc(self, gameState, depth, alpha, beta):
        if self.terminalCheck(gameState, depth):
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(0)
        v = float("-inf")
        for move in legalMoves:
            v = max(v, self.minFunc(gameState.generateSuccessor(self.index, move), 1, depth, alpha, beta))
            if v > beta:
                return v
            alpha = max(v, alpha)
        return v

    "function to perform the min step with alpha-beta pruning"
    def minFunc(self, gameState, agent, depth, alpha, beta):
        if self.terminalCheck(gameState, depth):
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(agent)
        v = float("inf")
        if(agent < gameState.getNumAgents() - 1):
            for move in legalMoves:
                v = min(v, self.minFunc(gameState.generateSuccessor(agent, move), agent+1, depth, alpha, beta))
                if v < alpha:
                    return v
                beta = min(beta, v)
        else:
            for move in legalMoves:
                v = min(v, self.maxFunc(gameState.generateSuccessor(agent, move), depth-1, alpha, beta))
                if v < alpha:
                    return v
                beta = min(beta, v)
        return v

    "function to check terminal state condition"
    def terminalCheck(self, gameState, depth):
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return True
        else:
            return False

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

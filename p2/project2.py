"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1:
Partner 2:
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""


def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    ##### Your implementation goes here. #####
    if alg == 'BFS':
        return bfs(maze)
    ##### Your implementation goes here. #####
    if alg == 'DFS':
        return dfs(maze)

def bfs(maze):
    # initialize
    for vertex in maze.adjList:
        vertex.visited = False
        vertex.prev = None
    queue = Queue()

    maze.start.visited = True
    queue.push(maze.start)
    while not queue.isEmpty():
        curr = queue.pop()
        #print("curr", curr)
        #print("prev", curr.prev)
        #print()
        for neighbor in curr.neigh:
            if not neighbor.visited:
                neighbor.visited = True
                queue.push(neighbor)
                neighbor.prev = curr

    # find path
    maze.path = []
    current = maze.exit
    while current is not None:
        #print("current", current)
        #print("prev", current.prev)
        #print()
        maze.path = [current.rank] + maze.path
        current = current.prev
    #print("path", maze.path)
    return maze.path

def dfs(maze):
    # initialize
    for vertex in maze.adjList:
        vertex.visited = False
        vertex.prev = None
    stack = Stack()

    maze.start.visited = True
    stack.push(maze.start)
    while not stack.isEmpty():
        curr = stack.pop()
        #print("curr", curr)
        for neighbor in curr.neigh:
            if not neighbor.visited:
                neighbor.visited = True
                stack.push(neighbor)
                neighbor.prev = curr

    # find path
    maze.path = []
    current = maze.exit
    while current is not None:
        maze.path = [current.rank] + maze.path
        current = current.prev
    #print("path", maze.path)
    return maze.path

"""
Main function.
"""
if __name__ == "__main__":
    # testStack()
    # testQueue()
    testMazes(False)
    #testMazes(True)

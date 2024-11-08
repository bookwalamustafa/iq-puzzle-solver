import heapq
import util
import random

class Node:
    def __init__(self, state, parent=None, g_value=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.g_value = g_value
        self.heuristic = heuristic 

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return list(path_back[::-1])

    def __lt__(self, other):
        return (self.g_value + self.heuristic) < (other.g_value + other.heuristic)

class Agent:
    def random_walk(self, state, n=8):
        current_node = Node(state)
        states_visited = [current_node.state]

        for i in range(n-1):
            actions = state.get_actions()
            if actions == []:
                break
            
            action = random.choice(actions)
            new_state = state.execute(action)
            current_node = Node(new_state, current_node)
            states_visited.append(new_state)
            state = new_state
            
        util.pprint(states_visited)
        return ""
    
    def _search(self, state, push_to_open, pop_from_open, heuristic=None):
        OPEN = []
        CLOSED = set() 
        Start = Node(state)
        open_state_strings = set()
        push_to_open(OPEN, Start)
        open_state_strings.add(str(Start.state))
        counter = 0

        while OPEN:
            N = pop_from_open(OPEN)
            counter += 1

            util.pprint(N.path())

            if N.state.is_goal():
                print(counter)
                return ""

            open_state_strings.remove(str(N.state))
            CLOSED.add(str(N.state))
            
            for action in N.state.get_actions():
                M = N.state.execute(action)
                M_str = str(M)

                if (M_str not in CLOSED) and (M_str not in open_state_strings):
                    g_value = N.g_value + 1
                    new_node = Node(M, N, g_value)
                    if heuristic:
                        new_node.heuristic = heuristic(M)
                    push_to_open(OPEN, new_node) 
                    open_state_strings.add(M_str)

    def bfs(self, state):
        self._search(state, lambda OPEN, node: OPEN.append(node), lambda OPEN: OPEN.pop(0))

    def dfs(self, state):
        self._search(state, lambda OPEN, node: OPEN.insert(0, node), lambda OPEN: OPEN.pop(0))

    def a_star(self, state, heuristic):
        self._search(state, lambda OPEN, node: heapq.heappush(OPEN, node), lambda OPEN: heapq.heappop(OPEN), heuristic)
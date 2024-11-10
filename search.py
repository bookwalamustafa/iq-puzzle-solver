import util
from iq import State, DEFAULT_STATE
from agent import Agent

def heuristic(state):
    return (state.count_pegs())

if __name__ == "__main__":
    cmd = util.get_arg(1)
    
    string = util.get_arg(2) or DEFAULT_STATE
    state = State(string)
    
    agent = Agent()

    if cmd == 'random':
        agent.random_walk(state)
    elif cmd == 'bfs':
        agent.bfs(state)
    elif cmd == 'dfs':
        agent.dfs(state)
    elif cmd == 'a_star':
        agent.a_star(state, heuristic)
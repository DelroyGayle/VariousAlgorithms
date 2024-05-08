"""
The Tower of Hanoi puzzle consists of 3 towers and some discs.

The objective is to bring all discs
from the leftmost tower to the rightmost tower.


Some rules:
* You can only move 1 disc at a time at any point
* Only smaller discs can exist on top of larger discs
* You can only move the disc at the top of each tower

Use Python to solve the Tower of Hanoi puzzle
(preferably with the least possible number of moves)

This solution is based on Liu Zuo Lin's solution which also uses
the Djikstra's shortest path algorithm to find the shortest path
from 'start state' to 'end state'
Source: https://levelup.gitconnected.com/youre-probably-a-excellent-programmer-if-you-can-solve-this-d78fb1ce73d3

Version 1
"""


def get_all_next_states(state):
    states_list = []
    # All the feasible disc moves
    for from_move, to_move in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]:
        from_tower, to_tower = state[from_move], state[to_move]
        if len(from_tower) == 0:
            continue
        piece = from_tower[-1]
        if len(to_tower) == 0 or to_tower[-1] > piece:
            """
            Proceed with a disc move
            Get the topmost piece
            For example, from this state
            [(3, 2, 1), (), ()]
            There are two possible moves
            ((3, 2), (1,), ()) - Disc from left tower to middle tower
            and
            ((3, 2), (), (1,)) - Disc from left tower to right tower

            """
            *others, top = from_tower

            # Convert tuple to a list in order to assign the appropriate towers
            new_state = list(state)
            # Topmost piece removed
            new_state[from_move] = tuple(others)
            # Then added here
            new_state[to_move] += (piece,)

            states_list.append(tuple(new_state))
    # EG [((3, 2), (1,), ()), ((3, 2), (), (1,))]
    return states_list


def search(state):
    queue = [state]
    dict = {state: {'mincost': 0, 'previous': None}}
    while queue:
        # QUEUE - First In - First Out - Breadth First Search
        current = queue.pop(0)
        current_mincost = dict[current]['mincost']

        all_next_states = get_all_next_states(current)
        for neighbour in all_next_states:
            if neighbour not in dict:
                # i.e. This neighbour has not been visited
                dict[neighbour] = (
                    {'mincost': current_mincost + 1, 'previous': current}
                )
                queue.append(neighbour)
            else:
                if dict[neighbour]['mincost'] > current_mincost + 1:
                    # Replace with a cheaper, that is, a shorter route
                    # Each neighbour has its previous route attached
                    dict[neighbour] = (
                        {'mincost': current_mincost + 1, 'previous': current}
                    )
                    queue.append(neighbour)
                # Otherwise do not add the route

    return dict


start_state = ((3, 2, 1), (), ())

end_state = ((), (), (3, 2, 1))

dict = search(start_state)
steps = [end_state]
while True:
    new = dict[steps[-1]]['previous']
    if new is None:
        break
    steps.append(new)

for step in steps[::-1]:
    print(step)

"""
Output:

((3, 2, 1), (), ())
((3, 2), (), (1,))
((3,), (2,), (1,))
((3,), (2, 1), ())
((), (2, 1), (3,))
((1,), (2,), (3,))
((1,), (), (3, 2))
((), (), (3, 2, 1))
"""

import json
from collections import deque

# Game board with a 3 x 3 grid
def game_board():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

# This allows the player ) to start with the board game and depth list
def game_state():
    return {'player': 'O', 
            'board': game_board(), 
            'depth': 0}

# Every moves is generated with player, board, and the depth
def generate_moves(state):
    moves = []
    player = state['player']
    board = state['board']
    depth = state['depth']

    # Looping to find if the cells shows any empty cells
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                # MAke that same board for the next state
                next_board = [row.copy() for row in board]
                #any player that starts goes to that next board
                next_board[row][col] = player

                # The next state is created to show either player X or O with the amount of depth being played
                next_state = {'player': 'O' if player == 'X' else 'X', 'board': next_board, 'depth': depth + 1}

                #append the generated moves to that next state
                moves.append(next_state)
    #return the result of the moves
    return moves

# Print the current node and its adjacent nodes shown on the console
def print_node(node):
    print("current node:")
    for row in node['board']:
        print("|" + "|".join(row) + "|")
    
  

    print("current adjacent node(s):")

    # Print the possible next moves being generated for printing adjacent nodes
    moves = generate_moves(node)
    for move in moves:
        for row in move['board']:
            print("|" + "|".join(row) + "|")
        print()

# Save the game tree as a JSON file
def save_game_tree(tic_tac_toe_tree):
    with open('game_tree.json', 'w') as json_file:
        json.dump(tic_tac_toe_tree, json_file)

def main():
    # Queue for Breadth First Search
    queue = deque()
    #append the queue from the game_state board
    queue.append(game_state())

    # List to store the game tree
    game_tree = []

    # Maximum depth to explore
    max_depth = 3  

    #while in the queue
    while queue:
        #the current state is the queue that pop from the far left
        current_state = queue.popleft()

        # Check if the maximum depth is reached
        if current_state['depth'] >= max_depth:
            # Skip generating moves beyond the maximum depth
            continue  
        #the possible moves being generated is created for the current state and appened to the queue
        moves = generate_moves(current_state)
        for move in moves:
            queue.append(move)
        #from the empty game_tree is appened to the current sate
        game_tree.append(current_state)
    
    # Print the first node in the game tree which is the empty node
    if game_tree:
        print_node(game_tree[0])
    #save the game tree to the JSON file 
    save_game_tree(game_tree)
    print("Game tree generated and saved as 'game_tree.json'.")

if __name__ == "__main__":
    main()

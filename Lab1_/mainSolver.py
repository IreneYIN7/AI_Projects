import sys
import argparse
import math
from GameTreeChecker import graphChecker, build_game_tree


def minimax(node, depth, alpha, beta, max_player):
    if depth == 0 or not node.children:
        return node.score

    if max_player:
        value = -math.inf
        for child in node.children:
            value = max(value, minimax(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                print(f"{node.label} has been pruned")
                break
        return value
    else:
        value = math.inf
        for child in node.children:
            value = min(value, minimax(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                print(f"{node.label} has been pruned")
                break
        return value

def run_minimax(game_tree, depth, max_player, use_ab):
    alpha = -math.inf
    beta = math.inf
    value = minimax(game_tree, depth, alpha, beta, max_player)
    if max_player:
        print(f"max({game_tree.label}) chooses {max(game_tree.children, key=lambda node: minimax(node, depth-1, alpha, beta, False))} for {value}")
    else:
        print(f"min({game_tree.label}) chooses {min(game_tree.children, key=lambda node: minimax(node, depth-1, alpha, beta, True))} for {value}")

def main():
    parser = argparse.ArgumentParser(description="Solves a minimax game tree with alpha-beta pruning and max-value cutoff.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose output mode")
    parser.add_argument('-ab', '--alpha_beta', action='store_true', help="Use alpha-beta pruning to speed up search")
    parser.add_argument('max_value', type=int, help="Maximum value for the game tree")
    parser.add_argument('player', choices=['max', 'min'], help="The player at the root of the game tree")
    parser.add_argument('graph_file', type = argparse.FileType('r'), nargs="?", help="The file containing the game tree")
    args = parser.parse_args()

    # Parse the game tree
    graph_str = open(args.graph_file).read().strip()
    game_tree = build_game_tree(graph_str)
    checker = graphChecker(graph_str)
    print(game_tree.label)
    print(game_tree.children)
    print(game_tree.score)
    # Run minimax on the game tree
    # if args.alpha_beta:
    #     if args.player == 'max':
    #         score, action = alpha_beta_max(game_tree, args.max_value, verbose=args.verbose)
    #     else:
    #         score, action = alpha_beta_min(game_tree, -args.max_value, verbose=args.verbose)
    # else:
    #     if args.player == 'max':
    #         score, action = minimax_max(game_tree, args.max_value, verbose=args.verbose)
    #     else:
    #         score, action = minimax_min(game_tree, -args.max_value, verbose=args.verbose)

    # # Print the result
    # print(f"{args.player}({game_tree.label}) chooses {action} for {score}")

if __name__ == '__main__':
    main()

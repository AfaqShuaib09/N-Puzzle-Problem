from Puzzle_board import *
import copy
import heapq

moves = ['Down', 'Left', 'Up', 'Right']


def generate_required_board1(dimension):
    gen_board = []
    for i in range(dimension):
        gen_board.append(list())
    size = dimension * dimension
    for i in range(size):
        gen_board[int(i / dimension)].append(str(i))
    return gen_board


def generate_required_board2(dimension):
    gen_board = []
    for i in range(dimension):
        gen_board.append(list())
    size = dimension * dimension
    for i in range(size):
        gen_board[int(i / dimension)].append(str((i + 1) % size))
    return gen_board


def get_input_from_file(filename):
    file_lines = None
    try:
        file = open(filename, 'r')
        file_lines = file.readlines()
        file.close()
    except Exception as e:
        print("Exception Occured:", str(e))
    finally:
        return file_lines


def write_output_to_file(filename, writing_str, mode='w'):
    try:
        file = open(filename, mode)
        file.write(writing_str)
        file.close()
    except Exception as e:
        print("Failed to write", str(e))


def is_present(board, lst):
    for temp_board in lst:
        if temp_board.is_boards_equal(board):
            return True
    return False


def generate_path_str(path, found):
    os = ''
    if found:
        count = len(path)
        for i in path:
            count = count - 1
            if i == 'D':
                os = os + moves[0]
            elif i == 'R':
                os = os + moves[1]
            elif i == 'U':
                os = os + moves[2]
            elif i == 'L':
                os = os + moves[3]
            if count != 0:
                os = os + '-> '
    else:
        os = os + "No path found"
    return os


def Astar_search_v1(line):
    path = ''
    found = False
    ls = line.rstrip().split(',')
    req_board1 = generate_required_board1(int(m.sqrt(len(ls))))
    req_board2 = generate_required_board2(int(m.sqrt(len(ls))))
    ls_visited_states = []
    ls_new_unvisited_st = []
    p_board = Puzzle_board(ls)
    if p_board.is_boards_equal(req_board1) or p_board.is_boards_equal(req_board2):
        return path, 0
    level_no = 0
    level = 0
    heapq.heappush(ls_new_unvisited_st, (p_board.get_misplaced_tiles(req_board1) + level_no, level_no, p_board))
    # Searching for a Solution goal state no. 1 (req_board1)
    while len(ls_new_unvisited_st) != 0 and not found:
        heuristic, level, board = heapq.heappop(ls_new_unvisited_st)
        if board.is_boards_equal(req_board1):
            path = board.path
            found = True
            break
        if not is_present(board.board, ls_visited_states):
            ls_visited_states.append(copy.deepcopy(board))
            temp_board = copy.deepcopy(board)
            temp_board.move_down()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st, (
                    level + 1 + temp_board.get_misplaced_tiles(req_board1), level + 1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_right()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st, (
                    level + 1 + temp_board.get_misplaced_tiles(req_board1), level + 1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_up()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st, (
                    level + 1 + temp_board.get_misplaced_tiles(req_board1), level + 1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_left()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st, (
                    level + 1 + temp_board.get_misplaced_tiles(req_board1), level + 1, copy.deepcopy(temp_board)))
    if not found:
        # If solution not found for goal state 1 Searching for a Solution goal state no. 2 (req_board1)
        del ls_visited_states[:]
        heapq.heappush(ls_new_unvisited_st, (p_board.get_misplaced_tiles(req_board1) + level_no, level_no, p_board))
        while len(ls_new_unvisited_st) != 0 and not found:
            heuristic, level, board = heapq.heappop(ls_new_unvisited_st)
            if board.is_boards_equal(req_board2):
                path = board.path
                found = True
                break
            if not is_present(board.board, ls_visited_states):
                ls_visited_states.append(copy.deepcopy(board))
                temp_board = copy.deepcopy(board)
                temp_board.move_down()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st, (
                        level + 1 + temp_board.get_misplaced_tiles(req_board1), level + 1, copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_right()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st, (
                        level + 1 + temp_board.get_misplaced_tiles(req_board1), level + 1, copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_up()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st, (
                        level + 1 + temp_board.get_misplaced_tiles(req_board1), level + 1, copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_left()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st, (
                        level + 1 + temp_board.get_misplaced_tiles(req_board1), level + 1, copy.deepcopy(temp_board)))
    if found:
        return generate_path_str(path, found), level
    else:
        return generate_path_str(path,found), -1


def Astar_search_v2(line):
    path = ''
    found = False
    ls = line.rstrip().split(',')
    dimension = int(m.sqrt(len(ls)))
    req_board1 = generate_required_board1(dimension)
    req_board2 = generate_required_board2(dimension)
    ls_visited_states = []
    ls_new_unvisited_st = []
    p_board = Puzzle_board(ls)
    if p_board.is_boards_equal(req_board1) or p_board.is_boards_equal(req_board2):
        return path, 0
    level_no = 0
    level = 0
    heapq.heappush(ls_new_unvisited_st, (p_board.get_manhattan_distance(dimension, 1) + level_no, level_no, p_board))
    # Searching for a Solution goal state no. 1 (req_board1)
    while len(ls_new_unvisited_st) != 0 and not found:
        heuristic, level, board = heapq.heappop(ls_new_unvisited_st)
        if board.is_boards_equal(req_board1):
            path = board.path
            found = True
            break
        if not is_present(board.board, ls_visited_states):
            ls_visited_states.append(copy.deepcopy(board))
            temp_board = copy.deepcopy(board)
            temp_board.move_down()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st, (
                    level + 1 + temp_board.get_manhattan_distance(dimension, 1), level + 1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_right()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st, (
                    level + 1 + temp_board.get_manhattan_distance(dimension, 1), level + 1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_up()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st, (
                    level + 1 + temp_board.get_manhattan_distance(dimension, 1), level + 1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_left()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st, (
                    level + 1 + temp_board.get_manhattan_distance(dimension, 1), level + 1, copy.deepcopy(temp_board)))
    if not found:
        # If solution not found for goal state 1 Searching for a Solution goal state no. 2 (req_board1)
        del ls_visited_states[:]
        heapq.heappush(ls_new_unvisited_st,
                       (p_board.get_manhattan_distance(dimension, 2) + level_no, level_no, p_board))
        while len(ls_new_unvisited_st) != 0 and not found:
            heuristic, level, board = heapq.heappop(ls_new_unvisited_st)
            if board.is_boards_equal(req_board2):
                path = board.path
                found = True
                break
            if not is_present(board.board, ls_visited_states):
                ls_visited_states.append(copy.deepcopy(board))
                temp_board = copy.deepcopy(board)
                temp_board.move_down()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st, (
                        level + 1 + temp_board.get_manhattan_distance(dimension, 2), level + 1,
                        copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_right()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st, (
                        level + 1 + temp_board.get_manhattan_distance(dimension, 2), level + 1,
                        copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_up()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st, (
                        level + 1 + temp_board.get_manhattan_distance(dimension, 2), level + 1,
                        copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_left()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st, (
                        level + 1 + temp_board.get_manhattan_distance(dimension, 2), level + 1,
                        copy.deepcopy(temp_board)))
    if found:
        return generate_path_str(path, found), level
    else:
        return generate_path_str(path,found), -1


def greedy_search_v1(line):
    path = ''
    found = False
    ls = line.rstrip().split(',')
    req_board1 = generate_required_board1(int(m.sqrt(len(ls))))
    req_board2 = generate_required_board2(int(m.sqrt(len(ls))))
    ls_visited_states = []
    ls_new_unvisited_st = []
    p_board = Puzzle_board(ls)
    if p_board.is_boards_equal(req_board1) or p_board.is_boards_equal(req_board2):
        return path, 0
    cost = 0
    level_no = 0
    level = 0
    heapq.heappush(ls_new_unvisited_st, (p_board.get_misplaced_tiles(req_board1),level_no, p_board))
    # Searching for a Solution goal state no. 1 (req_board1)
    while len(ls_new_unvisited_st) != 0 and not found:
        heuristic, level, board = heapq.heappop(ls_new_unvisited_st)
        if board.is_boards_equal(req_board1):
            path = board.path
            found = True
            break
        if not is_present(board.board, ls_visited_states):
            ls_visited_states.append(copy.deepcopy(board))
            temp_board = copy.deepcopy(board)
            temp_board.move_down()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st,
                               (temp_board.get_misplaced_tiles(req_board1), level+1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_right()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st,
                               (temp_board.get_misplaced_tiles(req_board1),level+1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_up()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st,
                               (temp_board.get_misplaced_tiles(req_board1),level+1,copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_left()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st,
                               (temp_board.get_misplaced_tiles(req_board1),level+1,copy.deepcopy(temp_board)))
    if not found:
        # If solution not found for goal state 1 Searching for a Solution goal state no. 2 (req_board1)
        del ls_visited_states[:]
        heapq.heappush(ls_new_unvisited_st, (p_board.get_misplaced_tiles(req_board1),level_no, p_board))
        while len(ls_new_unvisited_st) != 0 and not found:
            heuristic, level ,board = heapq.heappop(ls_new_unvisited_st)
            if board.is_boards_equal(req_board2):
                path = board.path
                found = True
                break
            if not is_present(board.board, ls_visited_states):
                ls_visited_states.append(copy.deepcopy(board))
                temp_board = copy.deepcopy(board)
                temp_board.move_down()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st,
                                   (temp_board.get_misplaced_tiles(req_board1),level+1,copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_right()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st,
                                   (temp_board.get_misplaced_tiles(req_board1),level+1, copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_up()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st,
                                   (temp_board.get_misplaced_tiles(req_board1),level+1, copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_left()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st,
                                   (temp_board.get_misplaced_tiles(req_board1),level+1,copy.deepcopy(temp_board)))
    if found:
        return generate_path_str(path, found), level
    else:
        return generate_path_str(path,found), -1


def greedy_search_v2(line):
    path = ''
    found = False
    ls = line.rstrip().split(',')
    dimension = int(m.sqrt(len(ls)))
    req_board1 = generate_required_board1(dimension)
    req_board2 = generate_required_board2(dimension)
    ls_visited_states = []
    ls_new_unvisited_st = []
    p_board = Puzzle_board(ls)
    if p_board.is_boards_equal(req_board1) or p_board.is_boards_equal(req_board2):
        return path, 0
    cost = 0
    level_no = 0
    level = 0
    heapq.heappush(ls_new_unvisited_st, (p_board.get_manhattan_distance(dimension, 1), level_no, p_board))
    # Searching for a Solution goal state no. 1 (req_board1)
    while len(ls_new_unvisited_st) != 0 and not found:
        heuristic, level, board = heapq.heappop(ls_new_unvisited_st)
        if board.is_boards_equal(req_board1):
            path = board.path
            found = True
            break
        if not is_present(board.board, ls_visited_states):
            ls_visited_states.append(copy.deepcopy(board))
            temp_board = copy.deepcopy(board)
            temp_board.move_down()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st,
                               (temp_board.get_manhattan_distance(dimension, 1),level+1,copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_right()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st,
                               (temp_board.get_manhattan_distance(dimension, 1),level+1,copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_up()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st,
                               (temp_board.get_manhattan_distance(dimension, 1),level+1, copy.deepcopy(temp_board)))
            temp_board = copy.deepcopy(board)
            temp_board.move_left()
            if not is_present(temp_board.board, ls_visited_states):
                heapq.heappush(ls_new_unvisited_st,
                               (temp_board.get_manhattan_distance(dimension, 1), level+1,copy.deepcopy(temp_board)))
    if not found:
        # If solution not found for goal state 1 Searching for a Solution goal state no. 2 (req_board1)
        del ls_visited_states[:]
        heapq.heappush(ls_new_unvisited_st, (p_board.get_manhattan_distance(dimension, 2),level_no, p_board))
        while len(ls_new_unvisited_st) != 0 and not found:
            heuristic, level,board = heapq.heappop(ls_new_unvisited_st)
            if board.is_boards_equal(req_board2):
                path = board.path
                found = True
                break
            if not is_present(board.board, ls_visited_states):
                ls_visited_states.append(copy.deepcopy(board))
                temp_board = copy.deepcopy(board)
                temp_board.move_down()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st,
                                   (temp_board.get_manhattan_distance(dimension, 2),level+1,copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_right()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st,
                                   (temp_board.get_manhattan_distance(dimension, 2), level+1, copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_up()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st,
                                   (temp_board.get_manhattan_distance(dimension, 2),level+1 ,copy.deepcopy(temp_board)))
                temp_board = copy.deepcopy(board)
                temp_board.move_left()
                if not is_present(temp_board.board, ls_visited_states):
                    heapq.heappush(ls_new_unvisited_st,
                                   (temp_board.get_manhattan_distance(dimension, 2),level+1 ,copy.deepcopy(temp_board)))
    if found:
        return generate_path_str(path, found), level
    else:
        return generate_path_str(path,found), -1

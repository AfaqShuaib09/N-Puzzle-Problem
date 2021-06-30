from informed_search_algo import *


def run_NPuzzle_program():
    mode = 'w'
    file_input = get_input_from_file('input.txt')
    for line in file_input:
        ls = line.rstrip().split(',')
        state = ''
        for i in ls:
            state = state + str(i) + ','
        state = state.rstrip(',')
        print(state)
        path, cost = Astar_search_v1(line)
        a_star_path = "A* Search with no. Of misplaced tiles: " + str(path) + ', Cost: ' + str(cost)
        print(a_star_path)
        path, cost = Astar_search_v2(line)
        a_star_path_2 = "A* Search with total Manhattan Distance: " + str(path) + ', Cost: ' + str(cost)
        print(a_star_path_2)
        path, cost = greedy_search_v1(line)
        greedy_search_path = "Greedy Search with no. Of misplaced tiles : " + str(path) + ', Cost: ' + str(cost)
        print(greedy_search_path)
        path, cost = greedy_search_v2(line)
        greedy_search_path_2 = "Greedy Search with total Manhattan Distance : " + str(path) + ', Cost: ' + str(cost)
        print(greedy_search_path_2)

        write_output_to_file('output.txt',state + '\n' + a_star_path + '\n' + a_star_path_2 + '\n' + greedy_search_path
                             + '\n' + greedy_search_path_2 + '\n', mode)
        mode = 'a'


# Main function Calling
run_NPuzzle_program()




#!/usr/bin/env python3
import time

#generate a graph from user input
def generate_graph(line):
    #line in format: "# of subsets,# of vertices in subset 1, # of vertices in subset 2,..."
    k = line[0]
    graph = []

    for i in range(k):
        subset_size = line[i+1]
        graph.append([f'{chr(i+65)}{c+1}'for c in range(subset_size)])

    return graph

#generate all possible edges between nodes in adjacent subgroups
def generate_edges(graph):
    edges = []
    for i in range(len(graph) - 1):
        for u in graph[i]:
            for v in graph[i + 1]:
                edges.append((u, v))

    return edges

#use backtracking to brute force all possible combinations of these edges
def find_edge_combinations(edges):
    def backtrack(start, cur_combo):
        #if we've reached the end, add result 
        if start >= len(edges):
            results.append(cur_combo[:])
            return
        
        #for the rest of the possible edges, add if both vertices are free
        for i in range(start, len(edges)):
            u, v = edges[i]
            if u not in used and v not in used:
                
                used.add(u)
                used.add(v)
                cur_combo.append(edges[i])
                
                # move to next edge recursively
                backtrack(i + 1, cur_combo)
                
                # backtrack
                cur_combo.pop()
                used.remove(u)
                used.remove(v)

    results = []
    used = set()
    backtrack(0, [])
    return results

def main():

    #open input and output files
    input = open("DP_Test_Input.txt", "r")
    output = open("DP_Test_Output.txt", "w")

    output.write("Output from DumbPartite.py\n")
    output.write("Input in format: # of subsets,# of vertices in subset 1, # of vertices in subset 2,...\n\n")

    for line in input:

        output.write(f"Input:\t{line}\n")

        # for runtime argument passage
        # #get input
        # k = int(input("Enter the number of subsets: "))
    
        # if k < 2:
        #     print("There needs to be at least 2 subsets for a k-partite graph")
        #     return

        #process input line
        line = [int(x) for x in line.split(",")]

        numv = sum(line[1:])

        output.write(f"Vertices:\t{numv}\n")
        
        graph = generate_graph(line)

        #start timer
        start = time.time()
        end = -1

        #test each matching for perfectness
        for combo in find_edge_combinations(generate_edges(graph)):
          #a matching is perfect if every vertex is matched, with none repeated (genereate_edges will not produce repeats)
            if len(combo) == sum([len(subgroup) for subgroup in graph])/2:
                output.write("Perfect matching found:\t")
                output.write(f"{combo}\n")

                #end timer
                end = time.time()
                break
    
        if end == -1:
            end = time.time()
            output.write("No perfect matching found\n")

        output.write(f"Run time: {end-start} seconds\n\n")

    input.close()
    output.close()
    return
    


if __name__ == "__main__":
    main()

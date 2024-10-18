# lwatson3-toc-fa24-project01
My DumbPartite solver project for Theory of Computing

**Team name:** lwatson3
**Link to github repository:** https://github.com/luca-watson/lwatson3-toc-fa24-project01

**Which project options were attempted:** DumbPartite solver

**Approximately total time spent on project:** 5 hours

**The language you used, and a list of libraries you invoked:** Python3, n/a

**How would a TA run your program (did you provide a script to run a test case?):** Edit the input file according to the input format, and run the script as usual. I did provide test cases

**A brief description of the key data structures you used, and how the program functioned:** The program reads in a line of csv data from the file, processes it and creates a nested-list representation of a graph from it. The program then generates a list of all possible edges by pairing up edges from adjacent subsets of the graph. It then uses a backtracing recursive algorithm to generate all possible matches from this list, and then checks them to see if they are a perfect matching. This, along with other information, is written to the output file.

**A discussion as to what test cases you added and why you decided to add them (what did they tell you about the correctness of your code):** I added a set of test cases with a perfect matching, and one without, each with a varying number of vertices. The set with a perfect match tended to take slightly less time than the set without them, and both sets took increasing amounts of time as the number of vertices increased. This made sense, as my algorithm is of an exponential time order, and thus verified the correctness of my code.

**Where did the data come from? (course website, handcrafted, a data generator, other)**: I generated it myself

**An analysis of the results, such as if timings were called for, which plots showed what? What was the approximate complexity of your program?:** The results were as expected. Time increased exponential with the number of vertices in the graph, and the graphs with perfect matches tended to take slightly less time the those without them.

**A description of how you managed the code development and testing:** I began by deciding how to represent a graph as a data structure, then developed helper functions to process input data, and generate a list of all possible vertices from the graph representation. The bulk of my time spent on the code was spent on the algorithm that generates all possible matchings, which I developed after doing some research on backtracing algorithms. After this, I came up with some graphs that would produce good outcomes for graphing, and then performed the testing and graphing.

**Did you do any extra programs, or attempted any extra test cases:** No

from construct_boolean_function_from_sign_matrix import construct_boolean_function
from PyBoolNet import InteractionGraphs as IGs
from PyBoolNet import QuineMcCluskey as QMC
from PyBoolNet import StateTransitionGraphs as STGs

###############################
n = 4
sign_matrix = [[0] * n for i in range(n)]

sign_matrix[0][1] = 1
sign_matrix[0][2] = 1
sign_matrix[0][3] = 1
sign_matrix[1][0] = -1
sign_matrix[2][1] = -1
sign_matrix[3][0] = -1
###############################

bool_func = construct_boolean_function(sign_matrix)
new_bool_func = [None for func in bool_func]

def get_f_i(bool_func, i):
    def f_i(x0, x1, x2, x3):
        return bool_func[f_i.i]([x0, x1, x2, x3])
    f_i.i = i
    return f_i

for i in range(n):
    print(i)
    new_bool_func[i] = get_f_i(bool_func,i)

variable_to_boolean_function = {"x"+str(i): new_bool_func[i] for i in range(len(bool_func))}
print(variable_to_boolean_function)
print(5*"###")
#print(bool_func[0]([1,1,0,1]))
prime_implicants = QMC.functions2primes(variable_to_boolean_function)
# Create the interaction graph
igraph = IGs.primes2igraph(prime_implicants)

# Construct the state transition graph
state_transition_graph = STGs.primes2stg(prime_implicants, "asynchronous")

STGs.stg2image(state_transition_graph, "stg.pdf", LayoutEngine="dot")
IGs.create_image(prime_implicants, "igraph.pdf")

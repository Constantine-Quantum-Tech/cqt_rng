from itertools import groupby, permutations
import numpy as np

def get_subm_idx(inp_state_array):
    indices = []
    for i in range(len(inp_state_array)):
        indices.extend([i] * inp_state_array[i])
    return indices

def decompose(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 1], [2]]
    elif n == 3:
        return [[3], [2, 1], [1, 1, 1]]
    elif n == 4:
        return [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    elif n == 5:
        return [[5], [4, 1], [3, 1, 1], [3, 2], [2, 1, 1, 1], [2, 2, 1], [1, 1, 1, 1, 1]]
    else:
        raise NotImplemented("Works only for n < 6 :)!")

def generate_output_states(total_photons, dim):
    output_states = []
    for i in decompose(total_photons):
        diff = [0] * (dim - len(i))
        i.extend(diff)
        l = list(permutations(i))
        l.sort()
        cleaned = list(l for l,_ in groupby(l))
        for c in cleaned:
            s = [str(i) for i in c]
            output_states.append("".join(s))
    return output_states
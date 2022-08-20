from itertools import product
import numpy as np
import matplotlib.pyplot as plt
from cqt_rng.post_processors import VonNeumannPP

def study_boson_sampler(probs):
    output_dict = dict()
    key = list(probs.keys())[0]

    all_output_states = []
    all_output_states.extend(probs[key][0])

    all_state_prob = []
    for i in range(len(all_output_states)):
        prob = probs[key][2][i] + probs[key][2][i]
        all_state_prob.append(prob)

    all_output_states_arr = []

    for i in all_output_states:
        s = [int(j) for j in i]
        all_output_states_arr.append(np.array(s))

    for i1, i2 in product(range(len(all_output_states_arr)), repeat=2):
        new_prob  = all_state_prob[i1] * all_state_prob[i2]
        output = VonNeumannPP().postprocess(all_output_states_arr[i1], all_output_states_arr[i2])
        output_str = "".join(output.astype(str))
        old_prob = output_dict.get(output_str)
        
        if old_prob:
            output_dict[output_str] = old_prob + new_prob
        else:
            if new_prob != 0:
                output_dict[output_str] = new_prob
    return output_dict

def plot_probs(probs):
    for k in probs.keys():
        labels, values = probs[k][0], probs[k][1]
        plt.bar(labels, values)
        plt.xticks(rotation=90)
        plt.grid()
        plt.title(f"Input state: {k}")
        plt.show()

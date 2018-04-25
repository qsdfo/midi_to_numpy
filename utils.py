import numpy as np

def get_pianoroll_time(pianoroll):
    T_pr_list = []
    for k, v in pianoroll.items():
        T_pr_list.append(v.shape[0])
    if not len(set(T_pr_list)) == 1:
        print("Inconsistent dimensions in the new PR")
        return None
    return T_pr_list[0]

def get_pitch_dim(pianoroll):
    N_pr_list = []
    for k, v in pianoroll.items():
        N_pr_list.append(v.shape[1])
    if not len(set(N_pr_list)) == 1:
        print("Inconsistent dimensions in the new PR")
        raise NameError("Pr dimension")
    return N_pr_list[0]

def dict_to_matrix(pianoroll):
    T_pr = get_pianoroll_time(pianoroll)
    N_pr = get_pitch_dim(pianoroll)
    rp = np.zeros((T_pr, N_pr), dtype=np.int16)
    for k, v in pianoroll.items():
        rp = np.maximum(rp, v)
    return rp
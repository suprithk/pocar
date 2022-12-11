import numpy as np
from matplotlib import pyplot as plt


def plot_tn_over_time(tot_eval_data):
    agent_names = list(tot_eval_data.keys())
    for an in agent_names:
        tot_over_time = np.mean(tot_eval_data[an]['tot_tn_over_time'], axis=0)
        timesteps = np.arange(tot_over_time.shape[0])

        for group in range(tot_over_time.shape[1]):
            plt.plot(timesteps, tot_over_time[:, group], label=f'{an}: Group {group + 1}')

    plt.title('Number of True Negatives (Rejected Loans That Would Have Not Been Repaid) Over Time')
    plt.xlabel('Timestep ')
    plt.ylabel('# TN')
    plt.legend()
    plt.show()
    plt.close()

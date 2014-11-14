import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import cPickle
from argparse import ArgumentParser

def _unpickle(file_path):
    data = None
    with open(file_path, 'rb') as f:
        data = cPickle.load(f)
    return data

def draw_zstat(file_path, output=None, topk=None):
    rank_precision = _unpickle(file_path)
    if topk is not None:
        rank_precision = rank_precision[0:topk]

    plt.plot(rank_precision, linewidth=2.0, color='#111111')
    plt.xlabel('Rank', fontsize=12, fontweight='bold')
    plt.ylabel('Precision', fontsize=12, fontweight='bold')
    plt.ylim(0.0, 1.0)

    if output is not None:
        plt.savefig(output)
    else:
        plt.show()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--topk', type=int)
    args = parser.parse_args()

    draw_zstat('../material/noise_prediction_rank_precision.pkl',
               './noise_prediction_rank_precision.pdf', args.topk)

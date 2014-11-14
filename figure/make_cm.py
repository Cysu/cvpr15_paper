import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import cPickle
from argparse import ArgumentParser

_label_names = [
    'T-Shirt', 'Shirt', 'Knitwear', 'Chiffon', 'Sweater', 'Coat', 'Windbreaker',
    'Jacket', 'Down Coat', 'Suit', 'Shawl', 'Dress', 'Vest', 'Underwear']

def _unpickle(file_path):
    data = None
    with open(file_path, 'rb') as f:
        data = cPickle.load(f)
    return data

def draw_cm(file_path, output=None):
    cm = _unpickle(file_path)
    freq = cm.sum(axis=0)
    freq = freq * 1.0 / freq.sum()
    cm = cm * 1.0 / cm.sum(axis=0)
    n = cm.shape[0]
    acc = sum(np.diag(cm) * freq)
    print acc

    plt.matshow(cm, cmap=plt.cm.Greys, aspect='auto')
    axes = plt.gca()
    for i in xrange(n):
        for j in xrange(n):
            v = int(cm[i, j] * 100)
            if v == 0: continue
            if v >= 50:
                axes.text(j, i, '{}'.format(v), fontweight='bold',
                          va='center', ha='center', color='#ffffff')
            else:
                axes.text(j, i, '{}'.format(v),
                          va='center', ha='center', color='#111111')

    # plt.title('Average Accuracy {:.2%}'.format(acc))
    plt.xlabel('True Label', fontsize=8)
    plt.ylabel('Weak Label', fontsize=8)
    axes.set_xticks([i for i in xrange(n)])
    axes.set_yticks([i for i in xrange(n)])
    axes.set_yticklabels(_label_names, fontsize=7)

    x_tl = []
    for i, (name, freq) in enumerate(zip(_label_names, freq)):
        if i % 2 == 0:
            x_tl.append('{}\n\n{:.1%}'.format(name, freq))
        else:
            x_tl.append('\n{}\n{:.1%}'.format(name, freq))
    axes.set_xticklabels(x_tl, fontsize=7)

    if output is not None:
        plt.savefig(output)
    else:
        plt.show()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--cm-file', help="Pickled confusion matrix file")
    parser.add_argument('--output', help="Output file path")
    args = parser.parse_args()

    if args.cm_file is None:
        draw_cm('../material/cm_strong_weak_labels.pkl',
                './cm_strong_weak_labels.pdf')
        draw_cm('../material/cm_strong_label_model_prediction.pkl',
                './cm_strong_label_model_prediction.pdf')
    else:
        draw_cm(args.cm_file, args.output)

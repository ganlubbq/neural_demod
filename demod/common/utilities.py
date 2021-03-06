import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def graph_confusion_matrix(cm, save_name, title='Confusion Matrix'):
    norm_conf = []
    for i in cm:
        a = 0
        tmp_arr = []
        a = sum(i, 0)
        for j in i:
            tmp_arr.append(float(j)/float(a+1e-10))
        norm_conf.append(tmp_arr)

    fig = plt.figure(figsize=(16,16))
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    res = ax.imshow(np.array(norm_conf), cmap=plt.cm.jet, 
                    interpolation='nearest')

    width, height = cm.shape

    for x in xrange(width):
        for y in xrange(height):
            ax.annotate(str(cm[x][y]), xy=(y, x), 
                        horizontalalignment='center',
                        verticalalignment='center')

    cb = fig.colorbar(res)
    plt.xticks(range(width), range(width))
    plt.yticks(range(height), range(height))
    plt.title(title)
    plt.tight_layout()
    plt.savefig(save_name, format='png')
    plt.close()




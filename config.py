import matplotlib.pyplot as plt


# prostě plotovací fce, abych nemusel milionkrát psát plt., plt.,.....
def plot(x, y, legend = ['x', 'y'], lim = ['', '', '', '']):

    plt.figure()
    plt.plot(x, y)
    plt.xlabel(legend[0])
    plt.ylabel(legend[1])
    if lim[0] != '':
        plt.xlim(lim[0], lim[1])
        plt.ylim(lim[2], lim[3])
    plt.show()

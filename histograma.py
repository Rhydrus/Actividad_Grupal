import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns


def crear_histogram(data):
    num_rows = 5
    num_cols = 6

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 15))
    axes = axes.ravel()  # Flatten the axes array

    for i, column in enumerate(data.columns):
        sns.histplot(data[column], ax=axes[i], kde=True)
        axes[i].set_title(column)
        axes[i].set_xlabel('')

    # Hide any remaining empty subplots
    for i in range(len(data.columns), num_rows * num_cols):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

def boxplot(data):
    num_rows = 5
    num_cols = 6

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 15))
    axes = axes.ravel()  # Flatten the axes array

    for i, column in enumerate(data.columns):
        sns.boxplot(x=data[column], ax=axes[i], showmeans=True, color='red')
        axes[i].set_title(column)
        axes[i].set_xlabel('')

    # Hide any remaining empty subplots
    for i in range(len(data.columns), num_rows * num_cols):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()



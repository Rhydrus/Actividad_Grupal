import matplotlib.pyplot as plt
import seaborn as sns
import math

def Matriz(data):
    Filas_count = len(data.columns)
    Filas = Filas_count
    contador = 1
    Columnas = 0
    while Filas_count >= 1:
        Filas_count = Filas_count / contador
        contador += 1
        Columnas += 1

    num_rows = math.ceil(Filas / Columnas)
    num_cols = math.floor(Columnas)
    return num_rows, num_cols
def histogram_all(data):

    num_rows,num_cols = Matriz(data)

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

def boxplot_all(data):

    num_rows, num_cols = Matriz(data)

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



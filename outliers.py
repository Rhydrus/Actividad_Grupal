from pyod.models.mad import MAD

def otliers(data,columna_nombre):
    data_filtered = data.copy()
    mad = MAD(threshold=3.5)
    for columna in columna_nombre:
        # Convert the 'Max' column into a 2D numpy array
        max_reshaped = data[columna].values.reshape(-1, 1)

        # Generate inline and outlier labels
        labels = mad.fit(max_reshaped).labels_
        median_value = data[columna].median()

        # Identify outliers and replace them with the median
        outliers_indices = labels == 1
        taxis_imputed = data.copy()
        taxis_imputed.loc[outliers_indices, columna] = median_value

        data_filtered[columna] = taxis_imputed[columna]
        print(f'{columna}-Numero de outliers: {labels.sum()}')

    return data_filtered

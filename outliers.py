from pyod.models.mad import MAD

def otliers(data,columna_nombre):
    mad = MAD(threshold=3.5)

    # Convert the 'total' column into a 2D numpy array
    total_reshaped = data[columna_nombre].values.reshape(-1, 1)

    # Generate inline and outlier labels
    labels = mad.fit(total_reshaped).labels_
    data_filtered = data[columna_nombre].copy()
    data_filtered = data_filtered[labels == 0]
    data[columna_nombre] = data_filtered
    return data

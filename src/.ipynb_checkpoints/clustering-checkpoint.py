from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def scale_features(rfm):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(rfm[['Recency','Frequency','Monetary']])
    return scaled

def apply_kmeans(data, k=4):
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)
    return model, labels
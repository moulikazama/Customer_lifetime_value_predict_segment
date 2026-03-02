from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def scale_features(data):
    scaler = StandardScaler()
    num_col = data.select_dtypes(include=['int64','float64'])
    scaled = scaler.fit_transform(num_col)
    return scaled

def apply_kmeans(data, k):
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)
    return model, labels

def sil_score(data, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(data)
    score = silhouette_score(data, labels)
    print(f"K={k}, Silhouette Score={score}")
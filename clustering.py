import random

def argmin(array):
    min_index = 0
    min_value = array[0]

    for i in range(1, len(array)):
        if array[i] < min_value:
            min_index = i
            min_value = array[i]

    return min_index

def k_means_fit(data, n_clusters, max_iter=100):
    centroids = random.sample(data, n_clusters)# 초기 클러스터 중심 선택

    for _ in range(max_iter):# 각 데이터 포인트에 가장 가까운 클러스터 할당
        labels = []
        for point in data:
            distances = []
            for center in centroids:
                temp = 0
                for i in range(0,12):
                    temp += (float(point[i]) - float(center[i])) ** 2
                distances.append(temp)
            closest_cluster = min(range(n_clusters), key=lambda x: distances[x])
            labels.append(closest_cluster)

        # 새로운 클러스터 중심 계산
        new_centroids = []
        for k in range(n_clusters):
            cluster_points = [list(map(float, point)) for point, label in zip(data, labels) if label == k]
            if cluster_points:
                new_centroids.append([sum(coords) / len(cluster_points) for coords in zip(*cluster_points)])
            else:
                # 클러스터에 할당된 데이터가 없을 경우 무작위 중심 선택
                new_centroids.append(random.choice(data))

        # 중심 변화가 없을 경우 알고리즘 종료
        if centroids == new_centroids:
            break

        centroids = new_centroids

    return labels, centroids

def k_medoids_fit(data, n_clusters, max_iter=100):
    # 초기 클러스터 중심 선택
    centroids = random.sample(data, n_clusters)

    for _ in range(max_iter):
        labels = []
        for point in data:
            distances = []
            for center in centroids:
                temp = 0
                for i in range(0, 12):
                    temp += (float(point[i]) - float(center[i])) ** 2
                distances.append(temp)
            closest_cluster = argmin(distances)
            labels.append(closest_cluster)

        new_centroids = []
        for k in range(n_clusters):
            cluster_points = [point for point, label in zip(data, labels) if label == k]
            if cluster_points:
                cluster_distances = []
                for center in cluster_points:
                    temp = 0
                    for i in range(0,12):
                        temp += abs(float(point[i]) - float(center[i]))
                    cluster_distances.append(temp)
                medoid_index = argmin(cluster_distances)
                new_centroids.append(cluster_points[medoid_index])
            else:
                new_centroids.append(random.choice(data))

        if centroids == new_centroids:
            break

        centroids = new_centroids

    return labels, centroids
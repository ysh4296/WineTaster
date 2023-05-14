def calculate_distance(point1, point2):
    # 두 데이터 포인트 간의 거리를 계산하는 함수
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += (float(point1[i]) - float(point2[i])) ** 2
    return squared_distance ** 0.5

def calculate_silhouette_coefficient(data, labels):
    num_samples = len(data)
    silhouette_values = []

    for i in range(num_samples):
        point = data[i]
        cluster_label = labels[i]

        # 클러스터 내 평균 거리 계산
        intra_cluster_distances = []
        for j in range(num_samples):
            if labels[j] == cluster_label and i != j:
                intra_cluster_distances.append(calculate_distance(point, data[j]))
        if intra_cluster_distances:
            mean_intra_cluster_distance = sum(intra_cluster_distances) / len(intra_cluster_distances)
        else:
            mean_intra_cluster_distance = 0

        # 가장 가까운 다른 클러스터의 평균 거리 계산
        inter_cluster_distances = []
        for j in range(num_samples):
            if labels[j] != cluster_label:
                inter_cluster_distances.append(calculate_distance(point, data[j]))
        if inter_cluster_distances:
            mean_inter_cluster_distance = sum(inter_cluster_distances) / len(inter_cluster_distances)
        else:
            mean_inter_cluster_distance = 0

        # 실루엣 계수 계산
        silhouette_value = (mean_inter_cluster_distance - mean_intra_cluster_distance) / max(mean_intra_cluster_distance, mean_inter_cluster_distance)
        silhouette_values.append(silhouette_value)

    # 전체 데이터 포인트의 실루엣 계수 평균 계산
    silhouette_avg = sum(silhouette_values) / num_samples

    return silhouette_avg, silhouette_values

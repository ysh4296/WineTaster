import csv
import matplotlib.pyplot as plt
from clustering import k_means_fit,k_medoids_fit
from evaluating import calculate_silhouette_coefficient

def save_array_as_csv(array, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(array)
    print(f"Array saved as {filename}")

def plot_silhouette_values(silhouette_values,method_name):
    cluster_numbers = range(2, len(silhouette_values) + 2)
    plt.plot(cluster_numbers, silhouette_values)
    plt.xlabel('Cluster Number')
    plt.ylabel('Silhouette Value')
    plt.title("Silhouette Values for " + method_name + " Cluster Numbers")
    plt.show()

def find_kmeans_optimal_clusters(data, max_clusters):
    best_score = -1
    best_clusters = 2
    silhouette_list = []
    for n_clusters in range(2, max_clusters + 1):
        labels,centroids = k_means_fit(data,n_clusters,100)
        save_array_as_csv([labels],"20175429-" + str(n_clusters-1) + ".csv")
        silhouette_avg, silhouette_values = calculate_silhouette_coefficient(data, labels)
        silhouette_list.append(silhouette_avg)
        if silhouette_avg > best_score:
            best_score = silhouette_avg
            best_clusters = n_clusters
    return best_clusters, silhouette_list

def find_kmedoids_optimal_clusters(data, max_clusters):
    best_score = -1
    best_clusters = 2
    silhouette_list = []
    for n_clusters in range(2, max_clusters + 1):
        labels,centroids = k_medoids_fit(data,n_clusters,100)
        save_array_as_csv([labels], "20175429-" + str(n_clusters+19) + ".csv")
        silhouette_avg, silhouette_values = calculate_silhouette_coefficient(data, labels)
        silhouette_list.append(silhouette_avg)
        if silhouette_avg > best_score:
            best_score = silhouette_avg
            best_clusters = n_clusters
    return best_clusters, silhouette_list

csv_file_path = "WineData.csv"

# 데이터를 저장할 리스트 초기화
data = []

# CSV 파일 불러오기
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # 첫 번째 행을 헤더로 처리하고 싶지 않은 경우, 아래 한 줄의 주석을 제거합니다.
    header = next(csv_reader)
    for row in csv_reader:
        data.append(row)

best_clusters, silhouette_list = find_kmeans_optimal_clusters(data,20)
plot_silhouette_values(silhouette_list,"k_means")
best_clusters, silhouette_list = find_kmedoids_optimal_clusters(data,20)
plot_silhouette_values(silhouette_list,"k_medoids")
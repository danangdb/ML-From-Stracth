from ml_from_scratch.neighbors import KNeighborClassifier

clf = KNeighborClassifier()
print(clf._compute_distance(p1 = np.array([0,3]),
                      p2 = np.array([4,])))
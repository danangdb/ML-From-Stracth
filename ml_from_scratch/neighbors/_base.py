import numpy as np

class NearestNeighbor:
    """
    Nearest neighbor base
    (tidak untuk dijalankan langsung, tapi jalankan fungsi turunan)

    Parameters
    n_neighbors : int, default=5
        Jumlah tetangga terdekat suatu titik
    
      p : int, default = 2
        power dari minskowki distance
        - p=1 -> manhattan
        - p=2 -> euclidean
    """

    def __init__(
            self,
            n_neighbors=5,
            p=2
        ):

            self.n_neighbors = n_neighbors
            self.p = p    
    
    def _compute_distance(self, p1, p2):
         """
         Hitung distance antara dua titik menggunakan minkowski distance

         Parameters
         ---------
         p1 : array-like of shape(n_features)
            titik pertama

        p2 : array-like of shape (n_features)
            titik kedua

        Returns
        ------
        dist : float
            Jarak minkowski dari dua buah titik
         """

         #cari selisi absolut antara p1 dan p2
         abs_diff = np.abs(p1 - p2)

         #kita pangkatkan selisih dan jumlahkan elemen-elemnnya
         sigma_diff = np.sum(abs_diff**self.p)

         #akarkan hasil sigma
         dist = sigma_diff**(1/self.p)

         return dist

    
    def check_base(self):
        print("Base function bisa diakses")
from ._base import NearestNeighbor


class KNeighborClassifier(NearestNeighbor):
     """
    Parameters
    --------
    n_neighbors : int, default=5
        Jumlah tetangga terdekat suatu titik
    
    weights : {'uniforms, 'distance'}, default='uniforms'
        Bobot untuk melakkan prediksi
        'uniform'
            setiap tetangga akan punya bobot yang sama
        'distance'
            semakin dekat tetangga dengan titik target, maka semakin besar bobotnya

            w = 1/d(data, target)

    p : int, default = 2
        power dari minskowki distance
        - p=1 -> manhattan
        - p=2 -> euclidean
    """
    #def __init__(self):
    #    super().__init__(
    #          n_neighbors=5,
    #           p=2
    #    )

    def check_class(self):
        print("Classifier function bisa diakses")
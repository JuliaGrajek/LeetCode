import numpy as np

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        list_of_sums: List[int]
        sorted_strengths: List[int]

        list_of_sums = np.sum(mat, axis=1)

        sort_index = np.argsort(list_of_sums, kind='mergesort')
   
        return sort_index[0:k]

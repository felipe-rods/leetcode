class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pair_index = {}
        
        # Para o índice e o número atual da lista
        for index, num in enumerate(nums):
            # Se o alvo menos o número está na pair_index:
            if target - num in pair_index:
                # retorna índice e o índice par do alvo - número
                return [index, pair_index[target - num]]
            # caso contrário, adiciona o número e o índice ao pair_index
            pair_index[num] = index

                 
solution = Solution()
print(solution.twoSum([1, 2, 3, 6, 7], 5))

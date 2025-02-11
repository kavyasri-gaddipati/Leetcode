class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # Sort to handle duplicates and make pruning easier
        result = []
        
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])  # Append a copy of path
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                if candidates[i] > target:
                    break  # Stop if the number exceeds target
                
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()  # Backtrack
        
        backtrack(0, target, [])
        return result
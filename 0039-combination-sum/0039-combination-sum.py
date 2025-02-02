class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path, remaining_target):
            # If the remaining target is 0, we found a valid combination
            if remaining_target == 0:
                result.append(path[:])  # Add a copy of the current path to the result
                return
            
            # Iterate through candidates starting from the current index
            for i in range(start, len(candidates)):
                # If the current candidate exceeds the remaining target, skip it
                if candidates[i] > remaining_target:
                    continue
                
                # Include the current candidate in the path
                path.append(candidates[i])
                
                # Recurse with the same candidate (since it can be used multiple times)
                backtrack(i, path, remaining_target - candidates[i])
                
                # Backtrack: remove the last candidate to try other combinations
                path.pop()
        
        result = []  # To store all valid combinations
        backtrack(0, [], target)  # Start the backtracking process
        return result
class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        n = len(arr)
        st = set()  # To keep unique quadruplets

        # First loop - pick first number
        for i in range(n):
            # Second loop - pick second number
            for j in range(i + 1, n):
                seen = set()  # Store numbers between j and k

                # Third loop - pick third number
                for k in range(j + 1, n):
                    # Find required fourth number
                    required = target - arr[i] - arr[j] - arr[k]

                    # If found in seen → valid quadruplet
                    if required in seen:
                        temp = tuple(sorted([arr[i], arr[j], arr[k], required]))
                        st.add(temp)

                    # Add current number to seen
                    seen.add(arr[k])

        # Convert set to list of lists
        return [list(quad) for quad in st]

        
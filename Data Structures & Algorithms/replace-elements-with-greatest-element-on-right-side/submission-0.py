class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = arr[len(arr) - 1]
        output = [-1] * len(arr)
        for i in range(len(arr) - 2, -1, -1):
            if i == len(arr) - 1:
                continue
            else:
                if arr[i + 1] < largest:
                    output[i] = largest
                elif arr[i + 1] > largest:
                    largest = arr[i + 1]
                    output[i] = largest
                else:
                    output[i] = largest
        return(output)


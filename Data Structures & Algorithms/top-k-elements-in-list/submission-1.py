class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        array = []
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        if len(hashmap) == k:
            return list(hashmap.keys())
        else:
            array = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)[:k]

        return array
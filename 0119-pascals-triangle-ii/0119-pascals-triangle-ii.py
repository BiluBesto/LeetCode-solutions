class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        if rowIndex == 0:
            return result
        cur_set = []
        for i in range(1,rowIndex+1):
            prev_set = result[i-1]
            cur_set = [1]

            for j in range(1,i):
                cur_set.append(prev_set[j-1] + prev_set[j])
            cur_set.append(1)
            result.append(cur_set)
        return cur_set
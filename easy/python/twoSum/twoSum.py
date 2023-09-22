# Ref: https://www.nileshblog.tech/leet-code-two-sum-problem-solution-java-cpp-javascript-python/#1_Brute_Force_Approach_Python

class TwoSum():
    # def twoSum(self, nums, target):
    #     '''
    #     brute force
    #     '''
    #     l_index = 0
    #     r_index = 1

    #     init_sum = nums[l_index] + nums[r_index]
    #     while init_sum != target:
    #         if r_index == len(nums) - 1:
    #             l_index += 1
    #             r_index = l_index + 1
    #         else:
    #             r_index += 1

    #         init_sum = nums[l_index] + nums[r_index]

    #     return [l_index, r_index]

    def twoSum(self, nums, target):
        '''
        hash table
        '''
        num_index_map = {}

        for i, num in enumerate(nums):
            if target - num in num_index_map:
                return [num_index_map[target - num], i]
            num_index_map[num] = i
        return []


if __name__ == '__main__':
    TwoSum = TwoSum()
    nums = [-1, -2, -3, -4, -5]
    target = -8
    result = TwoSum.twoSum(nums, target)
    print(result)  # Ans: [2, 4]

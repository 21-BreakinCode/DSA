class TwoSum {
    twoSum = (nums, target) => {
        let numIndexMap = {}

        for (let i = 0; i < nums.length; i++) {
            let num = nums[i]
            const diff = target - num
            if (diff in numIndexMap) {
                return [numIndexMap[diff], i]
            }
            numIndexMap[num] = i
        }

        return []
    }
}

module.exports = { TwoSum }

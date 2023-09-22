const { TwoSum } = require('./twoSum')

test('Two Sum general', () => {
    const TwoSumInstance = new TwoSum()
    const nums = [2, 7, 11, 15]
    const target = 9
    const expected = [0, 1]

    expect(
        TwoSumInstance.twoSum(nums, target)
    ).toEqual(expected)
})

test('Two Sum same number', () => {
    const TwoSumInstance = new TwoSum()
    const nums = [3, 3]
    const target = 6
    const expected = [0, 1]

    expect(
        TwoSumInstance.twoSum(nums, target)
    ).toEqual(expected)
})

test('Two Sum negative numbers', () => {
    const TwoSumInstance = new TwoSum()
    const nums = [-1, -2, -3, -4, -5]
    const target = -8
    const expected = [2, 4]

    expect(
        TwoSumInstance.twoSum(nums, target)
    ).toEqual(expected)
})

test('Two Sum unsorted numbers', () => {
    const TwoSumInstance = new TwoSum()
    const nums = [3, 2, 4]
    const target = 6
    const expected = [1, 2]

    expect(
        TwoSumInstance.twoSum(nums, target)
    ).toEqual(expected)
})

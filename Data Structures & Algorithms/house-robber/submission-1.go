func rob(nums []int) int {
    n := len(nums)
    
    if n == 1 {
        return nums[0]
    } else if n == 2 {
        return max(nums[0], nums[1])
    }

    memo := make(map[int]int)
    memo[0] = nums[0]
    memo[1] = max(nums[0], nums[1])

    return helper(n - 1, nums, memo)
}

func helper(i int, nums []int, memo map[int]int) int {
    if val, ok := memo[i]; ok {
        return val
    }

    memo[i] = max(nums[i] + helper(i - 2, nums, memo), helper(i - 1, nums, memo))
    return memo[i]
}

func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}
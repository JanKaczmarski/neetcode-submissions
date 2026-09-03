func rob(nums []int) int {
    n := len(nums)

    if n == 1 {
        return nums[0]
    } else if n == 2 {
        if nums[1] > nums[0] {
            return nums[1]
        }
        return nums[0]
    }

    dp := make([]int, n)
    dp[0] = nums[0]
    if nums[1] > nums[0] {
        dp[1] = nums[1]
    } else {
        dp[1] = nums[0]
    }
    
    prev := dp[0]
    curr := dp[1]

    for i := 2; i < n; i++ {
        new_curr := nums[i] + prev 
        if curr > new_curr {
            new_curr = curr
        }
        prev, curr = curr, new_curr
    }

    return curr
}

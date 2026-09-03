func rob(nums []int) int {
    n := len(nums)
    memo := make([]int, n)
    
    var dp func(int) int
    dp = func(i int) int {
        if i < 0 {
            return 0
        }

        if val := memo[i]; val != 0 {
            return val
        }

        memo[i] = max(
            dp(i - 1),
            nums[i] + dp(i - 2),
        )

        return memo[i]
    }

    return dp(n - 1)

}
func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}
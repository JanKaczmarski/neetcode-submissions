func fourSum(nums []int, target int) [][]int {
	// 1. Sort the input nums, when taking i or j skip to he next element if:
	// i < n-1 && nums[i] == nums[i+1]
	// 1`. lock on i-th element and find 3SUM
	// 2. lock on j-th (j > i) element and find 2SUM
	// 3. find 2SUM using 2 pointers
	sort.Ints(nums)
	return nSum(nums, target, 4)
}

func nSum(nums []int, target int, n int) [][]int {
	res := make([][]int, 0)

	if len(nums) < n || n < 2 {
		return res
	}

	// base case
	if n == 2 {
		l, r := 0, len(nums) - 1
		
		for l < r {
			sum := nums[l] + nums[r]

			if sum < target {
				l++
			} else if sum > target {
				r--
			} else {
				res = append(res, []int{nums[l], nums[r]})
				l++
				r--

				for l < r && nums[l] == nums[l-1] {
					l++
				}
				for l < r && nums[r] == nums[r+1] {
					r--
				}
			}
		}

		return res
	}

	// select 1 number and solved reducen nSUM
	for i := 0; i <= len(nums) - n; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		reducedResults := nSum(nums[i+1:], target - nums[i], n-1)

		for _, reduced := range reducedResults {
			combination := make([]int, 0, n)
			combination = append(combination, nums[i])
			combination = append(combination, reduced...)
			res = append(res, combination)
		}
	}

	return res
}
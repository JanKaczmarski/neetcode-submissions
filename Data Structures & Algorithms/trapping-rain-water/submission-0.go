func trap(height []int) int {
	// with prefix sum

	n := len(height)
	leftSum := make([]int, n)
	rightSum := make([]int, n)
	minLeftRight := make([]int, n)

	leftSum[0] = 0
	rightSum[n - 1] = 0
	for i := 1; i < n; i++ {
		if height[i - 1] > leftSum[i - 1] {
			leftSum[i] = height[i - 1]
		} else {
			leftSum[i] = leftSum[i - 1]
		}
	}
	for i := n - 2; i >= 0; i-- {
		if height[i + 1] > rightSum[i + 1] {
			rightSum[i] = height[i + 1]
		} else {
			rightSum[i] = rightSum[i + 1]
		}
	}

	for i := range n {
		if leftSum[i] <= rightSum[i] {
			minLeftRight[i] = leftSum[i]
		} else {
			minLeftRight[i] = rightSum[i]
		}
	}

	res := 0
	for i := range n {
		hereWater := minLeftRight[i] - height[i]
		if hereWater > 0 {
			res += hereWater
		}
	}

	return res
}

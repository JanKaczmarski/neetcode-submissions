func findJudge(n int, trust [][]int) int {
	// create trustScore coutning how many ppl trust i-th person
	// judge will have score n-1
	// the read the result
	trustScores := make([]int, n + 1)
	personVoted := make([]bool, n + 1)
	
	for _, trustRecord := range trust {
		trustScores[trustRecord[1]] += 1
		personVoted[trustRecord[0]] = true
	}

	for i, tScore  := range trustScores {
		if tScore == n-1 && !personVoted[i] {
			return i
		}
	}
	return -1
}

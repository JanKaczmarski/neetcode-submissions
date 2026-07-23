
type lockWithDepth struct {
	lock  string
	depth int
}

func openLock(deadends []string, target string) int {
	// 1. each lock combination is a vertex in a graph
	// 2. from a combination we can move to 8 different ones
	// except those that are in deadends
	// 3. we have undirected graph this way.
	// 4. Running BFS from "0000" on this grap will yield the result

	// says if given lock was already visited
	visited := make(map[string]bool)

	for _, deadend := range deadends {
		visited[deadend] = true
	}

	const start = "0000"

	// start lock in deadend
	if visited[start] {
		return -1
	}

	initLock := lockWithDepth{
		lock: start,
		depth: 0,
	}

	q := []lockWithDepth{initLock}
	visited[start] = true

	for len(q) > 0 {
		current := q[0]
		q = q[1:]

		if current.lock == target {
			return current.depth
		}

		for _, nextLock := range getNextLocks(current.lock) {
			if visited[nextLock] {
				continue
			}

			visited[nextLock] = true

			q = append(q, lockWithDepth{
				lock:  nextLock,
				depth: current.depth + 1,
			})
		}
	}

	return -1

}

func getNextLocks(lock string) []string {
	res := make([]string, 0, 8)
	modifiedLock := []byte(lock)

	for idx := range modifiedLock {
		originalDigit := modifiedLock[idx]
		digit := int(originalDigit - '0')

		prevDigit := (digit + 9) % 10
		nextDigit := (digit + 1) % 10

		// rotate this wheel backward
		modifiedLock[idx] = byte(prevDigit) + '0'
		res = append(res, string(modifiedLock))

		// rotate this wheel forward
		modifiedLock[idx] = byte(nextDigit) + '0'
		res = append(res, string(modifiedLock))

		// restore before modifying another wheel
		modifiedLock[idx] = originalDigit
	}

	return res
}

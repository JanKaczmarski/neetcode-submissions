func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := make([][]int, numCourses)
	inDegree := make([]int, numCourses)

	for i := range prerequisites {
		course := prerequisites[i][0]
		prereq := prerequisites[i][1]

		graph[prereq] = append(graph[prereq], course)
		inDegree[course]++
	}

	queue := make([]int, 0)
	
	for course := 0; course < numCourses; course++ {
		if inDegree[course] == 0 {
			queue = append(queue, course)
		}
	}

	completed := 0

	for head := 0; head < len(queue); head++ {
		course := queue[head]
		completed++

		for _, dependent := range graph[course] {
			inDegree[dependent]--

			if inDegree[dependent] == 0 {
				queue = append(queue, dependent)
			}
		}
	}

	return completed == numCourses
}

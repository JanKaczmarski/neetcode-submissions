func findOrder(numCourses int, prerequisites [][]int) []int {
	// Khan's algorithm with incoming edges and depends counter
	// if depends countetr == 0 then remove the lement and add it to the
	// processing sequece
	// IF no vertex is available to take (depdns_counter >=1 for all vertexes)
	// return empty array (imposibility to complete all tasks)

	// Invariants
	// graph[vertex] = []dependies - for each vertex keep the vertexes
	// that depend on it
	// dependecies[vertex] - how many dependencies are left for this vertex

	graph := make([][]int, numCourses)
	dependencies := make([]int, numCourses)
	for i := range numCourses {
		graph[i] = make([]int, 0)
	}

	for i := range prerequisites {
		vertex := prerequisites[i][0]
		dependency := prerequisites[i][1]

		graph[dependency] = append(graph[dependency], vertex)
		dependencies[vertex]++
	}

	queue := make([]int, 0, numCourses)
	res := make([]int, 0)

	for vertex := range numCourses {
		if dependencies[vertex] == 0 {
			queue = append(queue, vertex)
		}
	}

	for head := 0; head < len(queue); head++ {
		vertex := queue[head]

		res = append(res, vertex)
		for _, dependie := range graph[vertex] {
			dependencies[dependie]--
			if dependencies[dependie] == 0 {
				queue = append(queue, dependie)
			}
		}
	}

	if len(res) != numCourses {
		return []int{}
	}

	return res
}

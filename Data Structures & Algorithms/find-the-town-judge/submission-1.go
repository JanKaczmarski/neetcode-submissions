func findJudge(n int, trust [][]int) int {
	// create a relationship graph based on trust, then read the judge from the graph
	// based on incoming and outcoming edges
	//
	
	// how many edges are going into vertex
	vertexSize := make([]int, n + 1)

	graph := make([][]int, n + 1)
	for i := range graph {
		graph[i] = make([]int, 0)
	}

	for _, thisTrust := range trust {
		vertexSize[thisTrust[1]] += 1
		graph[thisTrust[0]] = append(graph[thisTrust[0]], thisTrust[1])
	}

	for i := range graph {
		if len(graph[i]) == 0 && vertexSize[i] == n - 1 {
			return i
		}
	}

	return -1
}

type MyQueue struct {
	pushs *stack
	pops *stack
}

func Constructor() MyQueue {
	return MyQueue{
		newStack(),
		newStack(),
	}
}

func (this *MyQueue) Push(x int) {
	this.pushs.push(x)
}

func (this *MyQueue) Pop() int {
	// move all from pushs to pops (reverse order of elements)
	for !this.pushs.empty() {
		elem := this.pushs.pop()
		this.pops.push(elem)
	}

	// last elment on push stack - first in queue
	res := this.pops.pop()

	for !this.pops.empty() {
		elem := this.pops.pop()
		this.pushs.push(elem)
	}

	return res
}

func (this *MyQueue) Peek() int {
	for !this.pushs.empty() {
		elem := this.pushs.pop()
		this.pops.push(elem)
	}

	res := this.pops.peek()

	for !this.pops.empty() {
		elem := this.pops.pop()
		this.pushs.push(elem)
	}

	return res
}

func (this *MyQueue) Empty() bool {
	return this.pushs.empty()
}


type stack struct {
	arr []int
}

func newStack() *stack {
	return &stack{make([]int, 0)}
}

func (s *stack) push(x int) {
	s.arr = append(s.arr, x)
}

func (s *stack) pop() int {
	n := len(s.arr)
	res := s.arr[n - 1]
	s.arr = s.arr[:n - 1]

	return res
}

func (s *stack) peek() int {
	return s.arr[len(s.arr) - 1]
}

func (s *stack) empty() bool {
	return len(s.arr) == 0
}
/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param2 := obj.Pop();
 * param3 := obj.Peek();
 * param4 := obj.Empty();
 */

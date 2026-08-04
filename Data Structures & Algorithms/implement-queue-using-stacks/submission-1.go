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
	if this.pops.empty() {
		for !this.pushs.empty() {
			elem := this.pushs.pop()
			this.pops.push(elem)
		}
	}

	return this.pops.pop()
}

func (this *MyQueue) Peek() int {
	if this.pops.empty() {
		for !this.pushs.empty() {
			elem := this.pushs.pop()
			this.pops.push(elem)
		}
	}

	return this.pops.peek()
}

func (this *MyQueue) Empty() bool {
	return this.pushs.empty() && this.pops.empty()
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

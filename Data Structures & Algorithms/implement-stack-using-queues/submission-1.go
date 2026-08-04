type MyStack struct {
	popq  *queue
	pushq *queue
}

func Constructor() MyStack {
	return MyStack{
		newQueue(),
		newQueue(),
	}
}

func (this *MyStack) Push(x int) {
	fmt.Printf("PUSH %d | BEFORE: pushq: %v, popq: %v\n", x, this.pushq, this.popq)
	this.pushq.push(x)
	fmt.Printf("PUSH | AFTER: pushq: %v, popq: %v\n", this.pushq, this.popq)

}

func (this *MyStack) Pop() int {
	fmt.Printf("POP | BEFORE: pushq: %v, popq: %v\n", this.pushq, this.popq)

	for this.pushq.size() > 1 {
		headElem := this.pushq.pop()
		this.popq.push(headElem)
	}

	res := this.pushq.pop()
	this.pushq, this.popq = this.popq, this.pushq

	fmt.Printf("POP | AFTER: pushq: %v, popq: %v\n", this.pushq, this.popq)

	return res
}

func (this *MyStack) Top() int {
	var headElem int
	
	for this.pushq.size() > 0 {
		headElem = this.pushq.pop()
		this.popq.push(headElem)
	}

	this.pushq, this.popq = this.popq, this.pushq

	return headElem
}

func (this *MyStack) Empty() bool {
	return this.pushq.size() == 0
}

type queue struct {
	arr  []int
	head int
}

func newQueue() *queue {
	return &queue{
		arr: make([]int, 0),
		head: 0}
}

func (q *queue) push(x int) {
	q.arr = append(q.arr, x)
}

func (q *queue) pop() int {
	val := q.arr[q.head]
	q.head++
	return val
}

func (q *queue) peek() int {
	return q.arr[q.head]
}

func (q *queue) size() int {
	return len(q.arr) - q.head
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param2 := obj.Pop();
 * param3 := obj.Top();
 * param4 := obj.Empty();
 */

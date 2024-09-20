class NodeClass {
    value: number;
    next: NodeClass | null;

    constructor(value: number) {
        this.value = value;
        this.next = null;
    }
}

class StackClass{
    private top: NodeClass | null;
    private bottom: NodeClass | null;
    private length: number;

    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    empty = () => this.length === 0;

    peek(): number | null {
        if (this.empty()) {
            return null;
        }

        this.top = this.top as NodeClass;
        return this.top.value;
    }

    push = (value: number) => {
        const newNode = new NodeClass(value);
        if (this.empty()) {
            this.top = newNode;
            this.bottom = newNode;
        } else {
            const holdingPointer = this.top as NodeClass;
            this.top = newNode;
            this.top.next = holdingPointer;
        }
        this.length++;

        return this;
    }

    pop = () => {
        if (this.empty()) {
            return null;
        }

        const holdingPointer = this.top as NodeClass;

        if (this.length === 1) {
            this.top = null;
            this.bottom = null;
        } else {
            this.top = this.top as NodeClass;
            this.top = this.top.next;

        }
        this.length--;

        return holdingPointer;
    }
}

class MyQueue<T> {
    length: number;

    // Stacks
    stack1: StackClass | null;
    stack2: StackClass | null;

    constructor() {
        this.stack1 = new StackClass();
        this.stack2 = null;
        this.length = 0;
    }

    push(x: number): void {
        this.stack1 = this.stack1 as StackClass;
        this.stack1.push(x);
        this.length++;
    }

    pop(): number | null {
        if(!this.stack1){
            return null;
        }

        this.stack1 = this.stack1 as StackClass;
        this.stack2 = new StackClass();

        while (!this.stack1.empty()) {
            const tempNode = this.stack1.pop() as NodeClass;
            this.stack2.push(tempNode.value);
        }
        this.stack1 = null;

        let popedNode: NodeClass | null = null;
        if (!this.stack2.empty()) {
            popedNode = this.stack2.pop() as NodeClass;
        }

        // Transfer the nodes back from stack2 to stack1
        this.stack1 = null;
        this.stack1 = new StackClass();

        while (!this.stack2.empty()) {
            const tempNode = this.stack2.pop() as NodeClass;
            this.stack1.push(tempNode.value);
        }
        this.stack2 = null;
        this.length--;

        if (popedNode) {
            return popedNode.value;
        } else {
            return null;
        }
    }

    peek(): number | null {
        if(!this.stack1){
            return null;
        }

        this.stack2 = new StackClass();
        while(!this.stack1.empty()){
            const tempNode = this.stack1.pop() as NodeClass;
            this.stack2.push(tempNode.value);
        }
        this.stack1 = null;

        const valuePeeked = this.stack2.peek();

        // Stack back the stack2 values to stack1
        this.stack1 = new StackClass();
        while(!this.stack2.empty()){
            const tempNode = this.stack2.pop() as NodeClass;
            this.stack1.push(tempNode.value);
        }
        this.stack2 = null;

        return valuePeeked;
    }

    empty(): boolean {
        return this.length === 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

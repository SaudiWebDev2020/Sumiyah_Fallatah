//Min Heap - insert
//Create a MinHeap class that stores data in a nearly complete tree. The MinHeap should use an array to store values with index 0 kept empty (it will make the math easier) and the smallest value will be stored in index 1, effectively the root of the tree.

//Each child value must be larger or equal to its parent, and the parent index will be half of its own index.

//let parentIndex = Math.floor(currentIndex / 2);
//Each value can have up to two children, and they can be found at the 2*i and 2*i + 1 indexes.

//let childIndex1 = 2*currentIndex;
//let childIndex2 = 2*currentIndex + 1;
//Write an insert method.

class MinHeap {
    constructor() {
        this.heap = [null];
    }

    insert(value) {
        let currentIndex = this.heap.length;
        this.heap.push(value);

        let i = Math.floor(currentIndex / 2);
        while (i > 0) {
            console.log(i);
            if (this.heap[i] > this.heap[currentIndex]) {
                [this.heap[i], this.heap[currentIndex]] = [this.heap[currentIndex], this.heap[i]];
                currentIndex = this.heap.indexOf(this.heap[i]);
            }
            i = Math.floor(i / 2);
        }
    }

    print(value) {
        console.log(this.heap);
    }
}
//When we insert a value it should start out by pushing it to the end of the array, then rearranging the array as is needed.

const heap1 = new MinHeap();
heap1.insert(3);
heap1.insert(4);
heap1.insert(2);
heap1.insert(6);
heap1.insert(1);
heap1.insert(0);
heap1.print();
 // the heap should look like [null, 3]
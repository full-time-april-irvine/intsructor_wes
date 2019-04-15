class Node {
  constructor(value) {
    this.val = value;
    this.next = null;
  }
}

class SList {
  constructor() {
    this.head = null;
  }

  addFront() {

  }

  removeFront() {
    var oldHead = this.head;
    this.head = oldHead.next;
    return this;
  }
}

var n = new Node('A');

var list = new SList();
list.addFront("A")
list.removeFront()


var num = 10;
num = num + 1;
// console.log(n);

// console.log(someList.head.next.next.value);
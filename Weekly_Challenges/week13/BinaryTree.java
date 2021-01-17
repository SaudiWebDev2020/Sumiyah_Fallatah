public class BinaryTree {
   public BTNode root;
   public BinaryTree() {
      this.root = null;
   }
   public void add(int value) {
      BTNode newNode = new BTNode(value);
      if (root == null) {
         root = newNode;
      } 
      else {
         BTNode runner = root;
         while(runner.left != null && runner.right != null) {
            if (value >= runner.value) {
               runner = runner.right;
            } else {
               runner = runner.left;
            }
         }
         if (value >= runner.value) {
            runner.right = newNode;
         } else {
            runner.left = newNode;
         }
      }
   }

   public void print(BTNode runner) {
      if (runner != null) {
         print(runner.left);
         System.out.print(runner.value + " ");
         print(runner.right);
      }
   }

   public void print() {
      print(root);
   }
}

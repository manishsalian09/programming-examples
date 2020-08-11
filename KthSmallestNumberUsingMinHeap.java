import java.util.Scanner;

public class KthSmallestNumberUsingMinHeap {

	public static void main(String args[]) {
		int arr[] = {7, 10, 3, 1, 6, 33, 100, 50};

		Scanner scanner = new Scanner(System.in);
		int k = scanner.nextInt();

		if (k > arr.length || k <= 0) return;

		int element = -1;
		for (int i = 0; i < k; i++) {
			int n = arr.length - i;
			buildMinHeap(arr, n);
			element = remove(arr, n);
		}

		System.out.println(element);

	}

	private static void buildMinHeap(int arr[], int n) {
                int index = (n / 2) - 1;
                
		for (int i = index; i >= 0; i--) {
                        minHeapify(arr, i, n);
                }
        }


        private static int findLeftChild(int currentIndex) {
                return (2 * currentIndex) + 1;
        }

        private static int findRightChild(int currentIndex) {
                return (2 * currentIndex) + 2;
        }

        private static int findParent(int currentIndex) {
                return (currentIndex - 1) / 2;
        }

	private static void minHeapify(int arr[], int currentIndex, int n) {

                int smallest = currentIndex;
                int left = findLeftChild(currentIndex);
                int right = findRightChild(currentIndex);
                if (left < n && arr[smallest] > arr[left]) {
                        smallest = left;
                }

                if (right < n && arr[smallest] > arr[right]) {
                        smallest = right;
                }

                if (smallest != currentIndex) {
                        swap(arr, smallest, currentIndex);
                        minHeapify(arr, smallest, n);
                }
        }

	private static void swap(int arr[], int i, int j) {
		int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
        }

	private static int remove(int arr[], int n) {
		int element = arr[0];
		arr[0] = arr[n - 1];
		return element;
	}

}

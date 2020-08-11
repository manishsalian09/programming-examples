import java.util.Arrays;
import java.util.stream.Collectors;

// Original Array
//			    6
//
//		2			17
//
//	1		3	9		10


// Min Heap
//			   1
//
//		2			9
//	6		3	17		10
//
//
// Max Heap
//			  17
//		6			10
//	2		3	9		1
// 			

class BinaryHeap {


	public static void main(String args[]) {
		int arr[] = {6, 2, 17, 1, 3, 9, 10};
		System.out.println("Original = " + Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
		buildMinHeap(arr, arr.length);
		System.out.println("Min Heap = " + Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
		buildMaxHeap(arr, arr.length);
		System.out.println("Max Heap = " + Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
	}

	private static void buildMinHeap(int arr[], int n) {

		int index = (n / 2) - 1;
		for (int i = index; i >= 0; i--) {
			minHeapify(arr, i, n);
		}
	
	}

	private static void buildMaxHeap(int arr[], int n) {

		int index = (n / 2) - 1;
		for (int i = index; i >= 0; i--) {
			maxHeapify(arr, i, n);
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
	private static void maxHeapify(int arr[], int currentIndex, int n) {

		int largest = currentIndex;
		int left = findLeftChild(currentIndex);
		int right = findRightChild(currentIndex);
		if (left < n && arr[largest] < arr[left]) {
			largest = left;
		}

		if (right < n && arr[largest] < arr[right]) {
			largest = right;
		}

		if (largest != currentIndex) {
			swap(arr, largest, currentIndex);
			maxHeapify(arr, largest, n);
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

import java.util.Arrays;
import java.util.stream.Collectors;

//			    6
//
//		2			17
//
//	1		3	9		10


class BinaryHeap {

	static int arr[] = {6, 2, 17, 1, 3, 9, 10};

	public static void main(String args[]) {
		System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
		buildHeap();
		System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
	}

	private static void buildHeap() {

		int index = (arr.length / 2) - 1;
		for (int i = index; i >= 0; i--) {
			heapify(index);
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

	private static void heapify(int currentIndex) {

		int smallest = currentIndex;
		int left = findLeftChild(currentIndex);
		int right = findRightChild(currentIndex);
		System.out.println(smallest + " " + left + " " + right);
		if (left < arr.length && arr[smallest] > arr[left]) {
			smallest = left;
		}

		if (right < arr.length && arr[smallest] > arr[right]) {
			smallest = right;
		}

		if (smallest != currentIndex) {
			swap(smallest, currentIndex);
			System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
			heapify(smallest);
		}
	}

	private static void swap(int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
}

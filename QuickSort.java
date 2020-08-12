import java.util.Arrays;
import java.util.stream.Collectors;
// 4, 2, 99, 50, 77, 1, 3, 8, 100, 23
// 1, 2, 3, 4, 8, 23, 50, 77, 99, 100
//
// pivot 77  8 2 23 50 4 1 3 77 100 99
// pivot 50  3 2 23 8 4 1 50 77 100 99
// pivot 23  23 2 3 8 4 1
//

public class QuickSort {

	public static void main(String args[]) {
		int arr[] = {4, 2, 99, 50, 100, 1, 3, 8, 77, 23};
		quickSort(arr, 0, arr.length-1);
		System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));	
	}

	private static int findPivot(int arr[], int low, int high) {
		int mid = (low + high) / 2;

		if (arr[low] < arr[mid] && arr[mid] < arr[high]) {
			return mid;
		} else if (arr[mid] < arr[low] && arr[low] < arr[high]) {
			return low;
		} else if (arr[mid] < arr[high] && arr[high] < arr[low]) {
			return high;
		}
		return mid;
	}

	public static void quickSort(int arr[], int low, int high) {
		if (low < high) {

			int pivot = findPivot(arr, low, high);
			swap(arr, low, pivot);

			int i = low + 1 , j = high;
			while (i < j) {
				if (arr[i] < arr[low]) i++;
				if (arr[j] > arr[low]) j--;
			}

			if (i >= j) {
				swap(arr, i, low);

			} else {
				swap(arr, i, j);
			}
			System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));	
			quickSort(arr, low, pivot - 1);
			quickSort(arr, pivot + 1, high);

		}
	
	}

	public static void swap(int arr[], int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
}

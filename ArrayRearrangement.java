import java.util.Arrays;
import java.util.stream.Collectors;

//  given array rearrange it in 
//  smallest, largest, 2nd smallest, 2nd largest, 3rd smallest, 3rd largest,...
//
// input  6, 3, 2, 88, 90, 66, 89, 23, 1 
// output 1, 90, 2, 89, 3, 88, 6, 66, 23


public class ArrayRearrangement {
	public static void main(String args[]) {
		int arr[] = {6, 3, 2, 88, 90, 66, 89, 23, 1, 13};
		System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
                rearrange(arr);
		System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
	}

	private static void rearrange(int arr[]) {
                sort(arr, 0, arr.length - 1);
		int temp[] = new int[arr.length];
		
		int i = 0;
		while (i < arr.length / 2) {
			temp[2 * i] = arr[i];
			temp[2 * i + 1] = arr[arr.length - i - 1];
			i++;
		}

		if (arr.length % 2 != 0) temp[2 * i] = arr[i];

		for (int j = 0; j < arr.length; j++)
			arr[j] = temp[j];
	}

	private static void sort(int arr[], int left, int right) {
		if (left > right) return;
		int pivot = partition(arr, left, right);
		sort(arr, left, pivot - 1);
		sort(arr, pivot + 1, right);
	}

	private static int partition(int arr[], int left, int right) {
		int pivotIndex = findMedian(arr, left, right);
		swap(arr, left, pivotIndex);
		int pivot = arr[left];

		int start = left + 1, end = right;
		while (start <= end) {
			while (start <= end && arr[start] < pivot) start++;
			while (start <= end && arr[end] > pivot) end--;

			if (start <= end) {
				swap(arr, start, end);
				start++; end--;
			}
		}
		swap(arr, left, end);
		return end;
	}

	private static int findMedian(int arr[], int left, int right) {
		int mid = (left + right) / 2;
		if (arr[mid] < arr[left] && arr[mid] < arr[right]) {
			return mid;
		} else if (arr[left] < arr[mid] && arr[mid] < arr[right]) {
			return left;
		} else if (arr[right] < arr[mid] && arr[mid] < arr[left]) {
			return right;
		} else {
			return mid;
		}
	}

	private static void swap(int arr[], int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
}

import java.util.Arrays;
import java.util.stream.Collectors;

// 4, 2, 99, 50, 77, 1, 3, 8, 100, 23, 23
// 1, 2, 3, 4, 8, 23, 23, 50, 77, 99, 100

public class QuickSort {

	public static void main(String args[]) {
		int arr[] = {4, 2, 99, 50, 100, 1, 3, 8, 77, 23, 23};
		System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));	
		quickSort(arr, 0, arr.length-1);
		System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));	
	}

	public static void quickSort(int arr[], int left, int right) {
		if (left > right) return;
		int pivotIndex = partition(arr, left, right);
		quickSort(arr, left, pivotIndex - 1);
		quickSort(arr, pivotIndex + 1, right);
	
	}

	public static int partition(int arr[], int left, int right) {
                int median = findMedian(arr, left, right);
                swap(arr, left, right); // swap pivot to starting index of the array
                int pivot = arr[left];

		int start = left + 1, end = right;
		while (start <= end) {
			while (start <= end && arr[start] < pivot) 
				start++;
			while (start <= end && arr[end] > pivot) 
				end--;

			if (start <= end) {
				swap(arr, start, end);
				start++; end--;
			}
		}
			
		swap(arr, left, end); // swap pivot to its final sorted position in the un-sorted array
		return end;
	}

        public static int findMedian(int arr[], int left, int right) {
                int mid = (left + right) / 2;
                if (arr[mid] < arr[left] && arr[mid] < arr[right]) {
                        return mid;
                }
                else if (arr[left] < arr[mid] && arr[mid] < arr[right]) {
                        return left;
                }
                else if (arr[right] < arr[mid] && arr[mid] < arr[left]) {
                        return right;
                }
                else {
                        return mid;
                }
        }

	public static void swap(int arr[], int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
}

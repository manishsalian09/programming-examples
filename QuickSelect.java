import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.Scanner;

public class QuickSelect {

	public static void main(String args[]) {
		int arr[] = {4, 2, 99, 50, 100, 1, 3, 8, 77, 23, 23};
		System.out.println(Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
		Scanner scanner = new Scanner(System.in);
		int k = scanner.nextInt();
		if (k > 0 && k <= arr.length)
			System.out.println(quickSelect(arr, 0, arr.length - 1, k - 1));
	}

	public static int quickSelect(int arr[], int left, int right, int k) {
		if (left > right) return -1;

		if (left == right) return arr[left];

		int pivotIndex = partition(arr, left, right);
		if (k == pivotIndex) {
			return arr[k];
		} else if (k < pivotIndex) {
			return quickSelect(arr, left, pivotIndex - 1, k);
		} else {
			return quickSelect(arr, pivotIndex + 1, right, k);
		}
	}

        public static int partition(int arr[], int left, int right) {
		int median = findMedian(arr, left, right);
		swap(arr, left, right);
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

                swap(arr, left, end);
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

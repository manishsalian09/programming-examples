import java.util.Arrays;
import java.util.stream.Collectors;

public class MergedSortedArrayMedian {

	public static void main(String args[]) {
		int arr1[] = {1 ,2, 4, 5, 6};
		int arr2[] = {3 ,8, 10, 15, 16, 30};
		int arr[] = new int[arr1.length + arr2.length];
	
		int i = 0;
		int j = 0;
		int k = 0;

		// Compare and merge two sorted array.
		while (i < arr1.length && j < arr2.length) {
			if (arr1[i] == arr2[j]) {
				arr[k] = arr1[i];
				i++; j++; k++;
				continue;
			}
		       	if (arr1[i] < arr2[j]) {
				arr[k] = arr1[i];
				i++;
			} else {
				arr[k] = arr2[j];
				j++;
			}
			k++;
		}

		// Start appending pending elements from both the array.
		while (i < arr1.length) {
			arr[k] = arr1[i];
			i++;k++;
		}
		while (j < arr2.length) {
			arr[k] = arr2[j];
			j++;k++;
		}

		int median = arr[arr.length / 2];
		System.out.println("Mergerd Array = " + Arrays.stream(arr).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
		System.out.println("Median = " + median);
	}
}

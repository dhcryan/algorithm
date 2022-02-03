import java.io.IOException;
//https://todaycode.tistory.com/52
public class Test {
    public static void main(String[] args) throws IOException {
        int arr[] = { 4, 1, 5, 7, 3, 2, 6, 8, 10, 9 };
        quicksort(arr);
        for (int a : arr) {
            System.out.print(a);
        }

    }

    public static void quicksort(int[] arr) {
        quicksort(arr, 0, arr.length - 1);

    }

    public static void quicksort(int[] arr, int left, int right) {
        if (left >= right)
            return;
        int mid = partition(arr, left, right);
        quicksort(arr, left, mid - 1);
        quicksort(arr, mid, right);
    }

    public static int partition(int[] arr, int left, int right) {
        int pivot = arr[(left + right) / 2];
        while (left <= right) {
            while (arr[left] < pivot)
                left++;
            while (arr[right] > pivot)
                right--;
            if (left <= right) {
                swap(arr, left, right);
                left++;
                right--;
            }
        }
        return left;
    }

    public static void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
}

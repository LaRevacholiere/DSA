public class quickSort {
    static int partition(int[] arr, int start, int end) {
        int m = medianOfThree(arr, start, end);
        int pivot = arr[m];
        swap(arr, m, end);
        int i = start, j = start;
        while (j < end) {
            if (arr[j] < pivot) {
                swap(arr, i, j);
                i++;
            }
            j++;
        }
        swap(arr, i, end);
        return i;
    }

    static void quickSort(int[] arr, int start, int end) {
        if (start < end) {
            int pi = partition(arr, start, end);
            quickSort(arr, start, pi - 1);
            quickSort(arr, pi + 1, end);
        }
    }

    static int medianOfThree(int[] arr, int start, int end) {
        int mid = start+(end-start)/2;
        if ((arr[start] < arr[mid] && arr[mid] < arr[end]) || (arr[end] < arr[mid] && arr[mid] < arr[start]))
            return mid;
        else if ((arr[mid] < arr[start] && arr[start] < arr[end]) || (arr[end] < arr[start] && arr[start] < arr[mid]))
            return start;
        else
            return end;
    }

    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void printArray(int[] arr, int size) {
        for (int i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {11, 11, 12, 16, 5, 5, 4, 1, 2, 0, 99, 56, 75, 23, 16, 17, 18};

        quickSort(arr, 0, arr.length - 1);
        System.out.println("Sorted array: ");
        printArray(arr, arr.length);
    }
}

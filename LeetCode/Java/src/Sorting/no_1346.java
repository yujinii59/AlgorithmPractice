package Sorting;

import java.util.Arrays;

/*1346. Check If N and Its Double Exist*/
public class no_1346 {

    private static int[] insertNumToArr(int[] arr, int num, int start, int end) {
        for (int i = end; i >= start+1; i--) {
            arr[i] = arr[i-1];
        }
        arr[start] = num;
        return arr;
    }

    //binary sort
    public static int[] binarySort(int[] sortedArr, int cnt, int num, int left, int right) {
        if (right == left){
            if (sortedArr[left] >= num) {
                sortedArr = insertNumToArr(sortedArr, num, right, cnt);
            }
            else{
                sortedArr = insertNumToArr(sortedArr, num, left+1, cnt);
            }
        }
        else {
            int mid = (left+right)/2;
            if (sortedArr[mid] < num) {
                sortedArr = binarySort(sortedArr, cnt, num, mid+1, right);
            }
            else if (sortedArr[mid] > num) {
                sortedArr = binarySort(sortedArr, cnt, num, left, mid);
            }
            else {
                sortedArr = insertNumToArr(sortedArr, num, mid, cnt);
            }
        }

        return sortedArr;
    }

    public static int[] sortFunc(int[] arr) {
        int cnt = 0;
        int[] sortedArr = new int[arr.length];
        for (int num:arr) {
            sortedArr[cnt] = 1000;
            System.out.println(Arrays.toString(binarySort(sortedArr, cnt, num, 0, cnt)));
            cnt++;
        }
        return sortedArr;
    }

    public static boolean binartSearch(int[] arr, int num, int left, int right, int idx) {
        if (left > right || left == arr.length) {
            return false;
        } else if (left == right) {
            if (arr[left] == num && left != idx) {
                return true;
            }else {
                return false;
            }
        } else {
            int mid = (left+right)/2;
            if (arr[mid] < num) {
                return binartSearch(arr, num, mid+1, right, idx);
            } else if (arr[mid] > num) {
                return binartSearch(arr, num, left, mid, idx);
            } else {
                if (mid == idx) {
                    boolean left_rst = binartSearch(arr, num, left, mid, idx);
                    boolean right_rst = binartSearch(arr, num, mid + 1, right, idx);
                    if (left_rst || right_rst) {
                        return true;
                    } else {
                        return false;
                    }
                }
                return true;
            }
        }
    }

    public static boolean checkIfExist(int[] arr){
//        int[] sortedArr = sortFunc(arr);
        Arrays.sort(arr);
        int[] sortedArr = arr;
        int length = arr.length;
        for (int i = 0; i < length-1; i++) {
            int num = sortedArr[i];
            if (binartSearch(sortedArr, num*2, 0, length, i)) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        System.out.println(checkIfExist(new int[] {-2,0,10,-19,4,6,-8}));
    }

}

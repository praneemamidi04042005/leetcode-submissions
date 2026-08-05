class Solution {

 static void mergeSort(int[] nums, int left, int right) {
        if (left >= right) return;
        int mid = left + (right - left) / 2;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }
static void merge(int[] nums, int left, int mid, int right) {
        int[] b = new int[right - left + 1];
        int i = left;
        int j = mid + 1;
        int k = 0;
        while (i <= mid && j <= right) {
            if (nums[j] < nums[i]) {
                b[k++] = nums[j++];
            } else {
                b[k++] = nums[i++];
            }
        }
        while (i <= mid) {
           b[k++] = nums[i++];
        }

        while (j <= right) {
            b[k++] = nums[j++];
        }

        for (int p =0; p <b.length; p++) {
            nums[left+p] = b[p];
        }
    }
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }
    }
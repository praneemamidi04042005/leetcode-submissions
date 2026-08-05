class Solution {
    public List<Integer> spiralOrder(int[][] a) {
        int n=a.length;
        int m=a[0].length;
        int top=0,bottom=n-1,left=0,right=m-1;
        List<Integer> l=new ArrayList<>();
		while(top<=bottom&&left<=right){
		    for(int i=left;i<=right;i++){
		        l.add(a[top][i]);
		    }
		    top++;
		    for(int i=top;i<=bottom;i++){
                l.add(a[i][right]);
		    }
		    right--;
		    if(top<=bottom){for(int i=right;i>=left;i--){
		      l.add(a[bottom][i]);
		    }
		    bottom--;}
		    if(left<=right){for(int i=bottom;i>=top;i--){
		       l.add(a[i][left]);
		    }
		    left++;}
		}
        return l;
    }
}
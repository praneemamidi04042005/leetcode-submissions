class Solution {
    public int largestAltitude(int[] gain) {
        ArrayList<Integer> l=new ArrayList<>();
        l.add(0);
        int s=0;
        for(int i:gain){s+=i;l.add(s);}return Collections.max(l);
    }
}
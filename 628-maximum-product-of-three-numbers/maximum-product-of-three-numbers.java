class Solution {
    public int maximumProduct(int[] nums) {
        ArrayList<Integer> l=new ArrayList<>();
        for(int i:nums){
            l.add(i);
        }
        Collections.sort(l);
        return Math.max(l.get(0)*l.get(1)*l.get(2),Math.max(l.get(l.size()-1)*l.get(l.size()-2)*l.get(l.size()-3),l.get(l.size()-1)*l.get(0)*l.get(1)));
    }
}
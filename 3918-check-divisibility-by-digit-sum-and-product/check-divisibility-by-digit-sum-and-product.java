class Solution {
    public boolean checkDivisibility(int n) {
        int sum=0,prod=1;
        int m=n,t=n;
        while(n>0){
            sum+=n%10;
            n/=10;
        }
        while(m>0){
            prod*=m%10;
            m/=10;
        }
        return t%(prod+sum)==0;
    }
}
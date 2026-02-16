// Last updated: 2/15/2026, 8:54:10 PM
class Solution {
    public boolean squareIsWhite(String coordinates) {
        char letter = coordinates.charAt(0);
        int num = Integer.parseInt(coordinates.substring(1,2)); 
        if((letter=='a'||letter=='c'||letter=='e'||letter=='g')&&num%2==1){
            return false;
        }
        else if((letter=='b'||letter=='d'||letter=='f'||letter=='h')&&num%2==0){
            return false;
        }
        return true;
    }
}
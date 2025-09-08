// Last updated: 9/8/2025, 4:38:41 PM
class Solution {
    public int romanToInt(String s) {
        int total = 0;
        String roman = s+"0";
        int i = 0;
        while (roman.charAt(i) != '0'){
            switch(roman.charAt(i)){
                case 'I':
                    if (roman.charAt(i+1) == 'V'){
                        total += 4;
                        i++;
                    } 
                    else if (roman.charAt(i+1) == 'X'){
                        total += 9;
                        i++;
                    }
                    else{
                        total+=1;
                    }
                break;
                case 'V':
                    total+=5;
                break;
                case 'X':
                    if (roman.charAt(i+1) == 'L'){
                        total += 40;
                        i++;
                    } 
                    else if (roman.charAt(i+1) == 'C'){
                        total += 90;
                        i++;
                    } 
                    else{

                        total+=10;
                    }
                break;
                case 'L':
                    total += 50;
                break;
                case 'C':
                    if (roman.charAt(i+1) == 'D'){
                        total += 400;
                        i++;
                    } 
                    else if (roman.charAt(i+1) == 'M'){
                        total += 900;
                        i++;
                    } 
                    else{

                        total+=100;
                    }
                break;
                case 'D':
                    total += 500;
                break;
                case 'M':
                    total += 1000;
                break;

                case '0':
                break;
            } 
        i++;
        }
    return total;
    }
}
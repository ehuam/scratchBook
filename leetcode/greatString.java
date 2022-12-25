import java.util.Stack;
import java.lang.StringBuilder;
import java.util.Iterator;

public class greatString {

	public String makeGood(String s) {

		String[] sarr = s.split("");
		Stack<String> passes = new Stack<String>();
		StringBuilder temp = new StringBuilder();

		for (String letter : sarr){
			if( !passes.empty() ){
				String prev = passes.peek();
				if ( letter.toUpperCase().equals(prev) ||
				 prev.toUpperCase().equals(letter)){
					if(!letter.equals(prev))	
					passes.pop();
				}
				passes.push(letter);
			}
			else{
				passes.push(letter);
			}
		}
		for(String letter: passes){
			temp.append(letter);
		}

		return temp.toString();
	}

    public String makeGoodRecr(String s){
	StringBuilder t = new StringBuilder();
	String prev = "";

	StringBuilder result = makeGoodRecr(s, t, prev);
	
	return result.toString();
    }

   public StringBuilder makeGoodRecr(String s, StringBuilder t, String p){

       if(s == null) {return t;}
	    else{
		String curr = s.substring(0,1);
		String nextPass = s.substring(1);
		String prev = curr;
		if(curr.toUpperCase().equals(prev) ||
		   prev.toUpperCase().eqauls(letter)){
		    
		    makeRecrv(nextPass, t, prev); 
		}
		else{
		    t.append(curr);
		    makeGoodRecr(nextPass, t, prev);
		}

	    }
    }
    

	public static void main(String args[]) {
		String s = "kkdsFuqUfSDKK";
		greatString result = new greatString();
		String answer = result.makeGood(s);
		System.out.println(answer);
	}
}

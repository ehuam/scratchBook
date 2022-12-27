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
			if( letter.equals(prev)  ){ passes.push(letter);}
			else if ( letter.equalsIgnoreCase(prev) ){ passes.pop();}
			else{ passes.push(letter); }
		    }
		    else{ passes.push(letter);}
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

   public StringBuilder makeGoodRecr(String s, StringBuilder t, String prev){

       
       if( s.equals("") ) {return t;}

       String curr = s.substring(0,1);
       String nextPass = s.substring(1);
       
       if( s.length() ==1 ) {
	   t.append(curr);
	   makeGoodRecr(nextPass, t, curr);
       }
       else if(curr.equals(prev)){
	   t.append(curr);
	   makeGoodRecr(nextPass,t, curr);
       }
       else if(curr.equalsIgnoreCase(prev)){
	   int end = t.length()-1;
	   t.deleteCharAt(end);
	   makeGoodRecr(nextPass, t, curr); 
       }
       else{
	   t.append(curr);
	   makeGoodRecr(nextPass, t, curr);
       }
       return t;

    }
    

	public static void main(String args[]) {
		String s = "kkdsFuqUfSDKK";
		greatString result = new greatString();
		String answer = result.makeGood(s);
		String recr_answer = result.makeGoodRecr(s);
		System.out.println("The answer itr = " + answer);
		/*
		  Recursive is broke;
		System.out.println("The answer recr = " + recr_answer);
		*/
	}
}

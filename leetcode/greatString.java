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
				else if ( letter.equalsIgnoreCase(prev) ){ passes.pop();	}
			 else{ passes.push(letter); }
		}
		for(String letter: passes){
			temp.append(letter);
		}

		return temp.toString();
	}

	public static void main(String args[]) {
		String s = "kkdsFuqUfSDKK";
		greatString result = new greatString();
		String answer = result.makeGood(s);
		System.out.println(answer);
	}
}

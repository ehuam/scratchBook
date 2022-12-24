import java.util.Stack;
import java.lang.StringBuilder;

class 1544-great_string{
    
    public String makeGood(String s){
	String[] sarr = s.split("");
	Stack<String> passes = new Stack<String>();
	StringBuilder temp = new StringBuilder();

	int i = 0;
	for(String letter: sarr){
	    while(i + 1 < sarr.length){
		String curr = sarr[i];
		String after = sarr[i+1];

		if(curr.equalsIgnoreCase(after)){
		    if(curr.toUpperCase().equals(after)
		       || after.toUpperCase().equals(curr) ){
			Stringbuilder c= new StringBuilder();
			for(int j = 0; j < i; j++){
			    c.append(sarr[j]);
			}
			for(int j = i+1; j < sarr.length ; j++){
			    c.append(sarr[j]);
			}
			temp = c;
			String current = temp.toString();
			passes.push(current);
			sarr = current.split("");
			i = 0;
			continue;
		}
	    }
		i++;
	}
	    System.out.println(passes);
    }
}
}


public static void main(String args[]){
	String s = "abBAcC";
	String answer = makeGood(s);

	System.out.println(answer);
}

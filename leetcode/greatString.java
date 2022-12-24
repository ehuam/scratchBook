import java.util.Stack;
import java.lang.StringBuilder;
import java.util.Iterator;

public class greatString{
    
    public String makeGood(String s){

	
	String[] sarr = s.split("");
	Stack<String> passes = new Stack<String>();
	StringBuilder temp = new StringBuilder();

	int i = 0;
	for(String letter: sarr){
	    while(i + 1 < sarr.length){

		//debugger
		//System.out.println("i = " + i);
		//
		
		String curr = sarr[i];
		String after = sarr[i+1];

		if(curr.equalsIgnoreCase(after)){
		    if(curr.toUpperCase().equals(after)
		       || after.toUpperCase().equals(curr) ){
			StringBuilder c= new StringBuilder();
			for(int j = 0; j < i; j++){
			    c.append(sarr[j]);
			}
			
			//debugger
			System.out.print("C =: " + c);
			//
			
			for(int j = i+2; j < sarr.length ; j++){
			    c.append(sarr[j]);
			}
			//debugger
			System.out.print("C = : " + c + "\n");
			
			temp = c;
			String current = temp.toString();
			passes.push(current);
			sarr = current.split("");
			i = 0;

			//debugger
			System.out.println("Temp is: " + temp);
			//
			continue;
		}
	    }
		i++;
		System.out.println("Stack has : " + passes.toString());
	    }
	}
	    // Debugger
	    /* 
	    System.out.println("outside of while: i = " + i);
	    	for(String x: sarr){
		    System.out.println("sarr.length = " +  sarr.length);
		    System.out.print("sarr=: ");
		    System.out.print(s);
		    System.out.println();
		}

	    System.out.println("arr[i] = " + sarr[i]);
	    */

	System.out.println("s.length = " + s.length());
	// debugger
	System.out.println("s = " + s);
	//

	if(!passes.empty()){
	    return s;
	}
	return passes.pop();
    }

    public static void main(String args[]){
	String s = "kkdsFuqUfSDKK";
	greatString result = new greatString();
	String answer = result.makeGood(s);
	System.out.println(answer);
	}
}

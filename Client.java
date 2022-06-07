//Client.java
import java.util.*;
import java.net.*;
import java.io.*;
class Client {
    public static void main(String a[]){      
        String mssg;        
        Scanner sc = new Scanner(System.in);
        try{
            while(true){
                Socket s = new Socket("localhost",5000);
                BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
                mssg = br.readLine();
                System.out.println("\nMssg:  "+mssg);                
                if(mssg.equals("quit")){
                    s.close();
                    break;
                }
                System.out.println("\nEnter message: ");
                mssg = sc.nextLine();
                PrintStream ps = new PrintStream(s.getOutputStream());
                ps.println(mssg);
            }
        }
        catch(Exception e){
            System.out.println(e);
        }
        
        
    }
}
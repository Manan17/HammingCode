//Server.java
import java.util.*;
import java.net.*;
import java.io.*;
class Server {
    public static void main(String a[]){
        try{
            
            ServerSocket s = new ServerSocket(5000);
            Scanner sc = new Scanner(System.in);
            String mssg;
            while(true){
                Socket ss = s.accept();
                System.out.println("\nEnter message: ");
                mssg = sc.nextLine();
                PrintStream ps = new PrintStream(ss.getOutputStream());
                ps.println(mssg);
                if(mssg.equals("quit")){
                    break;
                }
                BufferedReader br = new BufferedReader(new InputStreamReader(ss.getInputStream()));
                mssg = br.readLine();
                System.out.println("\nMssg:  "+mssg);
            }
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}

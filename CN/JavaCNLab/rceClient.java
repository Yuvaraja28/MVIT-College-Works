import java.io.*;
import java.net.*;
import java.lang.*;

public class rceClient
{
    public static void main(String a[]) throws UnknownHostException, IOException
    {
        Socket c = new Socket("26.158.245.166", 8000);
        System.out.println("Enter cmd:");
        DataInputStream dis = new DataInputStream(System.in);
        String s = dis.readLine();
        OutputStream os = c.getOutputStream();
        DataOutputStream dos = new DataOutputStream(os);
        dos.write(s.getBytes());
        dos.close();
        dis.close();
        c.close();
    }
}

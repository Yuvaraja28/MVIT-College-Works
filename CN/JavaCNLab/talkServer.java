import java.io.*;
import java.net.*;

public class talkServer
{
    public static void main(String[] args)
    {
        try
        {
            ServerSocket server = new ServerSocket(8000);
            Socket client = server.accept();
            System.out.println("Connection established..");
            DataInputStream dis = new DataInputStream(client.getInputStream());
            PrintStream ps = new PrintStream(client.getOutputStream());
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String s = "";
            int i = 0;
            while (i < 10)
            {
                System.out.println("From client: " + dis.readLine());
                System.out.println("To client:");
                s = br.readLine();
                ps.println(s);
                if (s.equals("end"))
                {
                    break;
                }
                i++;
            }
            ps.close();
            dis.close();
            br.close();
            client.close();
            server.close();
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}

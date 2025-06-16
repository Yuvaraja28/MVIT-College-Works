import java.io.*;
import java.net.*;
class echoServer
{
    public static void main(String args[])
    {
        try (ServerSocket ss = new ServerSocket(8000))
        {
            System.out.println("Server is listening on port 8000");
            try (Socket s = ss.accept())
            {
                System.out.println("Client connected: " + s);
                try (BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
                     PrintWriter print = new PrintWriter(s.getOutputStream(), true))
                {
                    String str;
                    while ((str = br.readLine()) != null)
                    {
                        if (str.equals(".")) break;
                        System.out.println("Message received by client:\n" + str);
                        print.println(str);
                    }
                }
            }
        }
        catch (IOException e)
        {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

import java.io.*;
import java.net.*;
public class ftpServer
{
    public static void main(String args[]) throws IOException
    {
        ServerSocket s1 = null;
        try
        {
            s1 = new ServerSocket(8000);
        }
        catch (IOException u1)
        {
            System.out.println("Could not find port 8000");
            System.exit(1);
        }
        Socket c = null;
        try
        {
            c = s1.accept();
            System.out.println("Connection frame: " + c);
        }
        catch (IOException e)
        {
            System.out.println("Accept failed");
            System.exit(1);
        }
        PrintWriter out = new PrintWriter(c.getOutputStream(), true);
        BufferedReader sin = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the text file name: ");
        String s = sin.readLine();
        File f = new File(s);
        if (f.exists())
        {
            BufferedReader in = new BufferedReader(new FileReader(s));
            String v;
            while ((v = in.readLine()) != null)
            {
                out.write(v);
                out.flush();
            }
            System.out.println("The file was sent successfully");
            in.close();
            c.close();
            s1.close();
        }
    }
}

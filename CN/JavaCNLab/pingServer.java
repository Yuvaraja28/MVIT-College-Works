import java.io.*;
import java.net.*;
public class pingServer
{
    public static void main(String a[])
    {
        String line1, line2;
        int i;
        ServerSocket es;
        DataInputStream di;
        PrintStream ps;
        Socket csoc;
        es = null;
        csoc = null;
        try
        {
            es = new ServerSocket(8000);
        }
        catch (Exception e)
        {
            System.out.println(e);
        }
        System.out.println("Ping Server");
        try
        {
            csoc = es.accept();
            di = new DataInputStream(csoc.getInputStream());
            ps = new PrintStream(csoc.getOutputStream());
            for (i = 0; i < 4; i++)
            {
                line1 = di.readLine();
                System.out.println("Pinged by client");
                ps.println(line1 + " reply from host: bytes=3 < time < 1ms TT<=128");
            }
            di.close();
            ps.close();
        }
        catch (Exception e)
        {
            System.out.println(e);
        }
    }
}

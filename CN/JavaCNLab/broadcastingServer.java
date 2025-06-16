import java.net.*;
import java.io.*;

class broadcastingServer 
{
    public static void main(String args[]) throws Exception 
    {
        DatagramSocket socket = new DatagramSocket();
        DataInputStream in = new DataInputStream(System.in);
        String msg;
        byte[] buf;

        while (true) 
        {
            System.out.println("Server:");
            msg = in.readLine();
            buf = msg.getBytes();

            try 
            {
                InetAddress clientAddr = InetAddress.getByName("RAGUL"); 
                DatagramPacket packet = new DatagramPacket(buf, buf.length, clientAddr, 8000); 
                socket.send(packet);
                System.out.println("Message successfully sent to client:" + clientAddr);
            } 
            catch (Exception e) 
            {
                System.out.println("Unable to connect to client: " + e);
            }
            if (msg.equalsIgnoreCase("Bye")) 
            {
                System.out.println("Server quits");
                socket.close();
                break;
            }
        }
    }
}

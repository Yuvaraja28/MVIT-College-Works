import java.io.*; 
import java.net.*;
class ftpUdpServer
{
    public static void main(String args[]) throws Exception
    {
        try
        {
            DatagramSocket dsoc = new DatagramSocket(8000); 
            byte[] receiveData = new byte[1024];
            System.out.println("Server is up and waiting for data...");
            FileOutputStream fos = new FileOutputStream("received_file.txt");
            while (true)
            {
                DatagramPacket dp = new DatagramPacket(receiveData, receiveData.length);
                dsoc.receive(dp);
                fos.write(dp.getData(), 0, dp.getLength());
                System.out.println("Received data and saved to file.");
                break; 
            }
            fos.close();
        }
        catch (Exception e)
        {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

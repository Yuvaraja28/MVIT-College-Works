import java.io.*;
import java.net.*;
class udpServer {
  DatagramSocket ds;
  DatagramPacket dp;
  byte buff[]=new byte[1024];
  String str,str1;
  boolean i=true;
  public void send() throws IOException {
    while(i) {
      ds=new DatagramSocket();
      DataInputStream in=new DataInputStream(System.in);
      System.out.println("Enter the msg:");
      str=in.readLine();
      buff=str.getBytes();
      dp = new DatagramPacket(buff,buff.length,InetAddress.getByName("RAGUL"), 8000);
      ds.send(dp);
      System.out.println("do u want to continue:yes or no");
      str1=in.readLine();
      if(str1.equals("yes")) {
        i=true;
      } else {
        i=false;
      }
    }
  }
  public static void main(String args[])throws IOException {
    udpServer se=new udpServer();
    se.send();
  }
}

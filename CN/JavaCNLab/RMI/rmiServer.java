import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;
import java.net.*;
import RMI.rmiImplement;
public class rmiServer {
  public static void main(String args[]) throws RemoteException {
    try {
      rmiImplement i=new rmiImplement();
      Naming.rebind("server",i);
      System.out.println("server reasdy");
    } catch(Exception e) {
      System.out.println("exception:"+e);
    }
  }
}

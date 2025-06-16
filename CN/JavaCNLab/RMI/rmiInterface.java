import java.rmi.*;
import java.rmi.server.*;
public interface rmiInterface extends Remote {
  public void fact(int n) throws RemoteException;
}
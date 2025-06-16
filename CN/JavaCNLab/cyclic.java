import java.io.*;

class cyclic
{
    public static void main(String args[]) throws IOException 
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the frame:");
        String data = in.readLine();
        int flen = data.length();
        int[] f = new int[flen + 10]; 
        int[] gen = new int[10];
        int[] rem = new int[10];
        
        for (int i = 0; i < flen; i++) 
        {
            f[i] = data.charAt(i) - '0';
        }
        
        System.out.println("Enter the generator:");
        String generator = in.readLine();
        int glen = generator.length();
        
        for (int i = flen; i < flen + glen - 1; i++) 
        {
            f[i] = 0;
        }
        
        for (int i = 0; i < glen; i++) 
        {
            gen[i] = generator.charAt(i) - '0';
        }
        
        int[] dataBits = new int[flen + glen - 1];
        System.arraycopy(f, 0, dataBits, 0, flen + glen - 1);
        
        for (int i = 0; i < flen; i++) 
        {
            if (dataBits[i] == 1) 
            {
                for (int j = 0; j < glen; j++) 
                {
                    dataBits[i + j] ^= gen[j];
                }
            }
        }
        
        System.out.print("Transmitted string: ");
        for (int i = 0; i < flen; i++) 
        {
            System.out.print(f[i]);
        }
        
        for (int i = flen; i < flen + glen - 1; i++) 
        {
            System.out.print(dataBits[i]);
        }
        
        System.out.println();
        System.out.println("Enter the received string:");
        String receivedData = in.readLine();
        int[] receivedBits = new int[flen + glen - 1];
        
        for (int i = 0; i < receivedData.length(); i++) 
        {
            receivedBits[i] = receivedData.charAt(i) - '0';
        }
        
        for (int i = 0; i < flen; i++) 
        {
            if (receivedBits[i] == 1) 
            {
                for (int j = 0; j < glen; j++) 
                {
                    receivedBits[i + j] ^= gen[j];
                }
            }
        }
        
        boolean error = false;
        for (int i = flen; i < flen + glen - 1; i++) 
        {
            if (receivedBits[i] == 1) 
            {
                error = true;
                break;
            }
        }
        
        if (error) 
        {
            System.out.println("Message received with error");
        } 
        else 
        {
            System.out.println("Message received with no error");
        }
    }
}

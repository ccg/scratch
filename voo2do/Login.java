import java.io.*;
import java.net.*;
import org.w3c.dom.*;
//import org.apache.xerces.dom.*;
//import org.apache.xerces.parsers.*;
//import javax.xml.parsers.*;
//import org.xml.sax.SAXException;

// FILL IN THE PASSWORD BEFORE RUNNING!

public class Login {
    public static void main(String[] args) throws IOException {
        try {
            URL url = new URL("http://voo2do.com/api/getLoginHash?email=ccg_spam@yahoo.com&password=PASSWORD");

            BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
            String str;
            StringBuilder sb = new StringBuilder();

            while ((str = in.readLine()) != null) {
                System.out.println(str);
                sb.append(str);
            }

            in.close();
        }
        catch (MalformedURLException e) { e.printStackTrace(); }
        catch (IOException e) { e.printStackTrace(); }
    }
}

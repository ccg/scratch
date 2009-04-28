import java.io.*;
import org.w3c.dom.*;
import javax.xml.parsers.*;
import org.xml.sax.SAXException;

// FILL IN THE PASSWORD BEFORE RUNNING!

public class Login2 {
    public static void main(String[] args) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder parser = factory.newDocumentBuilder();
            //URL url = new URL("http://voo2do.com/api/getLoginHash?email=ccg_spam@yahoo.com&password=PASSWORD");
            Document dom = parser.parse("http://voo2do.com/api/getLoginHash?email=ccg_spam@yahoo.com&password=PASSWORD");
            NodeList nodeList = dom.getElementsByTagName("login");
            Node node = nodeList.item(0);
            //System.out.println("Found node with name " + node.getNodeName());
            try {
                NamedNodeMap nodeMap = node.getAttributes();

                Node loginHashNode = nodeMap.getNamedItem("loginHash");
                String loginHash = loginHashNode.getNodeValue();
                System.out.println("loginHash: " + loginHash);

                Node userIdNode = nodeMap.getNamedItem("userId");
                String userId = userIdNode.getNodeValue();
                System.out.println("userId: " + userId);
            } catch (NullPointerException e) {
                System.err.println("Login XML missing expected attributes.");
                e.printStackTrace();
            }
        }
        catch (SAXException e) {
            System.err.println("XML response not well-formed.");
        }
        catch (IOException e) { e.printStackTrace(); }
        catch (FactoryConfigurationError e) {
            System.err.println("Could not locate a factory class.");
        }
        catch (ParserConfigurationException e) {
            System.err.println("Could not locate a JAXP parser.");
        }
    }
}

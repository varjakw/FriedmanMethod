import javax.swing.*;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

public class Vigenere {

    static final int MINIMUM_KEY_LENGTH = 1;
    static final int MAXIMUM_KEY_LENGTH = 5;
    //Estimating key lengths

    public static void main(String[] args) {

        int selection;
        Object[] options = { "Encrypt a Message", "Decrypt a Message" , "Friedman's Method", "Quit" };
        JPanel panel = new JPanel();
        panel.add(new JLabel("Vigenére Cipher & Friedman's Method"));

        selection = JOptionPane.showOptionDialog(null, "Main Menu", "Vigenére Cipher & Friedman's Method",

                JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE,

                null, options, options[0]);

        System.out.println(selection);

        switch (selection) {
            case 0: //encrypt a message
                String plaintextInput = JOptionPane.showInputDialog ("Please enter your plaintext");
                String keyword = JOptionPane.showInputDialog ("Please enter your keyword");

                String ciphertextAndKey = encrypt(plaintextInput, keyword);

                JTextArea ta1 = new JTextArea(10, 10);
                ta1.setText(ciphertextAndKey);
                ta1.setWrapStyleWord(true);
                ta1.setLineWrap(true);
                ta1.setCaretPosition(0);
                ta1.setEditable(false);
                JOptionPane.showMessageDialog(null, new JScrollPane(ta1), "Encrypted Text", JOptionPane.INFORMATION_MESSAGE);
                main(args);
                break;
            case 1: //decrypt message
                String ciphertextInput = JOptionPane.showInputDialog ("Please enter the ciphertext");
                String keyInput = JOptionPane.showInputDialog ("Please enter the key");

                String plaintext = decrypt(ciphertextInput, keyInput);
                System.out.println();

                JTextArea ta2 = new JTextArea(10, 10);
                ta2.setText(plaintext);
                ta2.setWrapStyleWord(true);
                ta2.setLineWrap(true);
                ta2.setCaretPosition(0);
                ta2.setEditable(false);
                JOptionPane.showMessageDialog(null, new JScrollPane(ta2), "Decrypted Text", JOptionPane.INFORMATION_MESSAGE);
                main(args);
                break;
            case 2: //Friedman's Method
                String ciphertextFriedman = JOptionPane.showInputDialog ("What is the ciphertext?");

                System.out.println();

                JTextArea ta3 = new JTextArea(10, 10);
                ta3.setText("hi");
                ta3.setWrapStyleWord(true);
                ta3.setLineWrap(true);
                ta3.setCaretPosition(0);
                ta3.setEditable(false);
                JOptionPane.showMessageDialog(null, new JScrollPane(ta3), "Decrypted Text", JOptionPane.INFORMATION_MESSAGE);
                main(args);
                break;
        }
    }

    public static String encrypt(String plaintext, String keyword){
        //generate key; repeating possible
        String key = generateKey(plaintext, keyword);
        char ciphertext[] = new char[plaintext.length()];

        //convert plaintext to array of chars
        char[] ch = new char[plaintext.length()];
        for (int i = 0; i < plaintext.length(); i++) {
            ch[i] = plaintext.charAt(i);
        }

        //convert key to array of chars
        char[] chkey = new char[key.length()];
        for (int i = 0; i < key.length(); i++) {
            ch[i] = key.charAt(i);
        }

        for (int i  = 0; i < plaintext.length(); i++){
            ciphertext[i] = (char) (((ch[i] + chkey[i]) % 26) + 'A');
        }
        return "Ciphertext: " + String.valueOf(ciphertext) + "\nKey: " + key;
    }

    public static String generateKey(String plaintext, String keyword){
        int x = plaintext.length();

        for (int i = 0; ; i++)
        {
            if (x == i)
                i = 0;
            if (keyword.length() == plaintext.length())
                break;
            keyword+=(keyword.charAt(i));
        }
        return keyword;
    }

    public static String decrypt(String ciphertext, String key){
        char plaintext[] = new char[ciphertext.length()];

        //convert ciphertext to array of chars
        char[] ch = new char[ciphertext.length()];
        for (int i = 0; i < ciphertext.length(); i++) {
            ch[i] = ciphertext.charAt(i);
        }

        //convert key to array of chars
        char[] chkey = new char[key.length()];
        for (int i = 0; i < key.length(); i++) {
            ch[i] = key.charAt(i);
        }

        for (int i  = 0; i < ciphertext.length(); i++){
            plaintext[i] = (char) (((ch[i] + chkey[i]) % 26) + 'A');
        }
        return String.valueOf(plaintext);
    }
}

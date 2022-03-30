package Cryptography.Module;

import org.junit.jupiter.api.Test;

import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

class EncryptingTest {

    @Test
    void encryptingTest() {
        try {
            Encrypting encrypting = new Encrypting("RSA", 2048);
            System.out.println(new String(encrypting.encryptData("JE-Chen", "RSA/ECB/PKCS1Padding"), StandardCharsets.UTF_8));
        } catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException | IllegalBlockSizeException | BadPaddingException e) {
            e.printStackTrace();
        }
    }

}
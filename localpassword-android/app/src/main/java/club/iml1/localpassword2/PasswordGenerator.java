package club.iml1.localpassword2;

import java.math.BigInteger;
import java.security.MessageDigest;

public class PasswordGenerator {
    public static String shuffle(String str1, String str2) {
        StringBuilder shuffled = new StringBuilder();
        int minLength = Math.min(str1.length(), str2.length());
        for (int i = 0; i < minLength; i++) {
            shuffled.append(str1.charAt(i));
            shuffled.append(str2.charAt(i));
        }
        if (str1.length() > str2.length()) {
            shuffled.append(str1.substring(minLength));
        } else {
            shuffled.append(str2.substring(minLength));
        }
        return shuffled.toString();
    }


    public static String generate(int length, String name, String password, String birthdate, String website) {
        try {
            // Secret one
            String combined = length + name + birthdate + website + length;
            String secretOne = hash(combined, MessageDigest.getInstance("SHA256"));
            // Secret two
            combined = length + website + password + birthdate + length;
            String secretTwo = hash(combined, MessageDigest.getInstance("SHA256")).substring(0, 32);

            System.out.println(secretOne);
            System.out.println(secretTwo);

            return shuffle(secretOne, secretTwo + secretTwo).substring(0, length);
        } catch (Throwable e) {
            e.printStackTrace();
        }
        return null;
    }

    private static String hash(String message, MessageDigest algorithm) {
        algorithm.reset();
        algorithm.update(message.getBytes());
        byte[] digest = algorithm.digest();
        return String.format("%0" + (digest.length << 1) + "x", new BigInteger(1, digest));
    }
}
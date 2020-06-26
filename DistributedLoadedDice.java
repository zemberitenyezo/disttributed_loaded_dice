import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

class DistributedLoadedDice {

    private static String suggestion = "";

    static String distributedLoadedDice(Integer participants, List<String> names, List<Integer> chances, Integer joker) //throws IOException
    {
        MessageDigest hash = null;
        try {
            hash = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        assert hash != null;

        BigInteger previousHash = BigInteger.ZERO;
        for (int candidateIndex = 0; candidateIndex < participants; candidateIndex++) {
            for (Integer candidateChance = 0; candidateChance < chances.get(candidateIndex); candidateChance++) {
                String text = names.get(candidateIndex) + candidateChance.toString() + joker.toString();
                byte[] bytes = hash.digest(text.getBytes(StandardCharsets.UTF_8));
                BigInteger nextHash = new BigInteger(1, bytes);
                if (previousHash.compareTo(nextHash) < 0) {
                    suggestion = names.get(candidateIndex);
                    previousHash = nextHash;
                }
            }
        }
        return suggestion;
    }
}
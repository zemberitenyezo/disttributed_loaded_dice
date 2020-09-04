import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        List<String> nevek = new ArrayList<String>();
        List<Integer> eselyek = new ArrayList<Integer>();
        Integer joker;
        System.out.println("Hany nem listas ellenzeki indul a korzeteben?");
        String indulokSzamaStr = System.console().readLine();
        Integer indulokSzama = Integer.parseInt(indulokSzamaStr);
        Float eselye;
        for (Integer index = 0; index < indulokSzama; index++) {
            System.out.println(index+1 + ". indulo neve?");
            nevek.add(System.console().readLine());
            System.out.println(index+1 + ". indulo nepszerusege (%)?");
            eselye = Float.parseFloat(System.console().readLine())*100;
            eselyek.add(eselye.intValue());
        }
        System.out.println("Kerem adja meg a legfrissebb Joker sorsolason kihuzott 6 jegyu szelveny szamot!");
        joker = Integer.parseInt(System.console().readLine());
        System.out.println("Kerem szavazzon " +
                DistributedLoadedDice.distributedLoadedDice(indulokSzama, nevek, eselyek, joker) +
                " nevu jeloltre!");
    }
}

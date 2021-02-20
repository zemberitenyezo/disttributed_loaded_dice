(Scroll down for English...)

# Decentralizált cinkelt kocka algoritmus

Ahogy a "kocogtatok" szó is erősen szöveg környezet érzékeny - "én" vagy "ti" - úgy a "visszacsatolás párti", is csak egyes embereknek juttatja a trianoni békeszerződést eszébe. Mások, főleg műszakiak, tudják, hogy a "jó tett helyébe jót várj" mondás igazságára utal ez a sajnálatosan inkább műszó kategóriába eső kifejezés, aminek a hétköznapi elterjedtsége nagyon hiányzik a magyar nyelvből: talán még a demokráciához és a kapitalizmushoz való viszonyunkat is aláássa, hogy nem gondolkodunk nyelvi szinten abban, az emberre a cselekedeteinek vissza kell hatnia. A modern társadalmak mind erre épülnek, ettől fejlődtek fel. Ahol a visszacsatolás sérül, ott csak a neveltetésen, elveken, eszméken, vagy épp hiten múlik, ki hogyan cselekszik, de az pár évszadnyi középkoron át nem vitt sehova.

Ma Magyarországon ez a visszacsatolás sérül a politikában az új, 2010 utáni választási rendszer és az ellenzéki pártok számosságának nem is olyan szövevényes együttállása miatt: a relatív többség alapú, egy fordulós választásban az ellenzék rendre alul marad a körzetekben, lásd 2018-ban, ahol "országosan" (határon túli szavazatokkal együtt) 49,5%-nyi szavazó voksolt a kormányra listán. Éppcsak az ellenzék 50,5%-nyi szavazója szanaszét szavazott a versengő ellenzéki pártokra, így az országos többség végül a körzetek miatt is a jelenlegi kormányé lett. Erre a jelenségre több megoldás is elképzelhető, például összefogás előválasztás alapján a relevánsabb körzetekben. De mi lesz azon területeken, ahol nincs meg az emberi és-vagy anyagi erőforrás az ellenzék egységesítésére, és a verseny miatt továbbra is eloszlanának az ellenzéki szavazatok?

Legkézenfekvőbb, ha a szavazók maguk egyeznek meg, kire szavazzanak. De hogyan lehet azt megszervezni egy előválasztás nélkül?

Ha a szavazók minden körzetben a valóban ellenzéki pártok jelöltjei közül szimplán a névsorban legelsőt választanák, akkor országos szinten a nevek véletlenszerűsége miatt kb. azonos számú körzeti képviselő juthatna be az országgyűlésbe az egyes ellenzéki pártokból. Későbbiekben ez a módszer egy offline is működőképes számítógépes programmal vagy okostelefon applikációval tovább finomítható úgy, hogy az egyes körzetekben a szoftver által tett véletlenszerű javaslatok országos szintű végeredménye közelítse a pártok valódi országos támogatottságát.

Ez műszakilag megoldható... Valahogy így:

Induljunk ki abból, hogy a pártvezetők kidobhatnák egy sima dobókockával, melyik körzetben melyikük jelöltje induljon. Ennek a decentralizált megfelelője, ha ABC sorrendben, praktikusan az első - releváns - ellenzéki jelöltre szavaz mindenki a saját helyi listájáról. Ez azonban még nem tükrözi a pártok országos népszerűségét. Ahhoz egy cinkelt kockán keresztül vezethetne az út, amit a pártvezetők a pártjaik népszerűsége szerint súlyozhatnának. Ez azonban nem decentralizált, vagyis nem hajtható végre állampolgárként, egyemberként.

A "decentralizált cinkelt kocka" technikai megoldása jobban hasonlítható egy olyan kártya játékhoz ahol a legerősebb kártya birtokosa nyer, és a pártjaik országos népszerűségével arányos számú lapot kapnak az egyes körzetek helyi jelöltjei párt hovatartozásaik alapján. A leosztáshoz egy ún. ál-véletlen generátorra van szükség, ami egy olyan matematikai számítás amely azonos bemenetre mindig ugyanazzal, a bemeneti adat függvényében egyébként rendkívül megjósolhatatlanul változó eredménnyel reagál. Ez ott jön be a képbe, hogy nem a pártok vezetői vagy jelöltjei játsszák le a  képzeletbeli kártya játékot, hanem minden szavazónak egyenként, passziánsz jelleggel a saját szoftvere számolja ki, hogy kire érdemes szavaznia egymástól függetlenül, offline, központi koordinációtól mentesen. Ahhoz azonban, hogy körzetenként minden szavazó mégis ugyanazt a tanácsot kapja, a kiindulási lapjaiknak egyezniük kell! Eközben ahhoz, hogy orszagos szinten körzetről körzetre valtozó legyen a végeredmény, így tükrözve az országos népszerűségi szinteket, az egyes körzetekben azonos, de az eltérő körzetekben már más és más leosztásra van szükség az egyes "passziánszozó" applikációkban. Ezt a két feltételt egyszerre teljesíti, ha a lapjárást a körzetenként változó, de egy adott körzetben azonos névlistakat bemenetként használó ál-véletlen generátor segítségével osztjuk ki. Mintegy a körzeti név listákat használva egységes igazodási pontként.

A lapjárást még célszerű a választás előtti, utolsó előtti - kb. 1 hetes - Joker sorsolás eredményétől is függővé tenni, több okból is:
1) szinte az utolsó napig nem derül ki, kiket fog javasolni a szoftver, így lejáratni, politikailag támadni sem tudni, melyik körzetben kiket kell pontosan
2) a pártok körzetenkénti reprezentációja, bár közelíteni fogja azok korábban mért országos népszerűségét, de a statisztikai folyamat szórása és a körzetek véges száma miatt ez matematikailag nem lehet tökéletes, lesz amelyik párt a pontos népszerűségéhez képest kicsit felül reprezentáltabb lesz, lesz amelyik alul, és a Joker sorsoláson múlik gyakorlatilag, hogy ez végül az adott választáson éppen pontosan hogyan alakul
3) a 2) pont szerinti eltérések véletlenszerűen alakulnak választásról választásra, amíg a választáshoz ezt az algoritmust használjuk és a mostani törvény hatályos
4) a különböző későbbi választásokon akkor is más és más eredmény születik majd, ha történetesen egy-két helyen ugyanazok a nevek indulnának

Az algoritmus működéséhez kritikus, hogy
 - mindenki precízen és pontosan ugyanazt az algoritmust használja
 - az egy körzetben szavazók ugynazokat a neveket adják meg (ékezet, kis és nagy betű, de még a szóközök száma (1) is befolyásol)
 - országosan pedig azonos esélyeket adjanak meg az egyes pártok helyi indulóinak (utóbbihoz per pillanat jó kiindulási alap lehet az önkormányzati választás, máskor a legutolsó hasonlóan hiteles országos népszerűségi felmérés)
 - a Joker szám ismert legyen mindenki számára (ezért érdemes az egy héttel korábbit használni, ha a sorsolás "véletlenül" elmaradna, akkor "ééééhhnn" formátumban a választás napja adandó meg)

Ha a kormányt leváltani akaró szavazó polgárok mind, önként ezen eljárás szerint választanak, akkor gyakorlatilag csak az egyszerű, abszolút többségükön múlik egy-egy körzet megnyerése, még akkor is, ha több, egymás közt nem koordináló ellenzéki párt száll versenybe!

A vázolt eljárás offline, önállóan számolja ki a javasolt jelölteket, használata semmilyen központi adatgyűjtést nem igényel, és központosított koordinációt is csak annyiban tesz szükségessé, hogy ha a lakosság több különféle alkalmazást használna, vagy több különféle véletlen szám forrást adna meg (egy hetes Joker helyett), azzal újfent megosztaná saját magát a helyi ellenzéki jelöltek között, és valószínűleg elveszítené az helyi választási körzeteket.

Arra az esetre ha több applikáció létrehozása miatt komprimittálódna a szavazatok egységesítése, és nem sikkerülne időben megszervezni, hogy melyiket használjuk egységesen, marad a _vészforgatókönyv: az ABC sorrendben 1. (első) releváns ellenzéki körzeti jelölt választása!_

# Distributed loaded dice algorithm

Voting systems are most of the cases never ideal - that's proven by maths - and times may come when a particular voting system gets abused by some rouge politicians or parties. In such times people can optimize their voting power to deviate from rather randomly scattered voting to pre-election based and with various goals. Most of the time however that rouge government will try to hinder this process so it might not seem a bad idea to do it privately safely just by being able to run an offline application on a mobile phone which helps the masses organise themselves according to some rule of thumb rather than just failing to change the system! Let's see a proof of concept for an app to help unite voters in a single round voting system with a fragmented opposition by an offline computable pseudo-random function.

In a single round voting system, where the strongest party's candidate wins irrespective of whether s/he has >50% majority, a fragmented opposition automatically yields that votes cast on them get more or less statistically distributed among the oppositions' candidates, thus enabling a party with relative majority retain its power even if its popularity is <50% among the voters' entire population.

One way of tackling this problem is if the opposition holds pre-elections to agree upon a single candidate for each district, so that people's votes can't scatter. A simpler and faster one is throwing a dice to select a candidate in districts without sufficient funds to hold pre-elections for. A more fair one is doing one big public poll - like an EU referendum - to see the public support for each oppositional party and throwing with an adequatly loaded dice to choose the single oppositional candidates for each and every voting district.

However this would need politicians who know how to gamble, and that has already been proven not to be the best idea. So we people of any Democratic Republic of a Single Rounded Voting System with Fragmented Opposition, need to take the situation in our hands, and do it personally... ;)

How can a decentralizied pseudo random algorithm help with that?

First lets stay with the non-loaded, regular dice concept. If all voters would vote for the oppositional candidate in every district with a name first in alphabetical order among all candidate names, that would be a deterministic yet equally random selection among the competing parties. However it would make up a funny parliament if most representatives' names would start with 'A' or 'B' rarely 'C' sometimes 'D' etc.. So it is better to compute a pseudo random function, a so called hash of the candidates' names with a smart phone app offline, and then let the largest hash be selected from that list. This has further benefits too, because it opens the door to the distributed version of the loaded dice concept, that is capable of representing the diverse parties actual public support! All that the application needs to do is simply ask for the weight of the load, i.e. how much chance one oppositional party's candidate needs to have based on the previously polled nation wide popularity, and then create proportionally many hashes for each candidate of the respective parties in every voting district by adding a counter value to the names. Meaning for example if a party won 4 seats in the EU parliament, that party's candidates should be assigned 4x as many hashes as candidates of a party with 1 EU seat. This is easy to accomplish, just a chance counter needs to be added to the hash input, that runs from 1...4 in case of the candidates of the stronger party in this example.

In other words the applications compute the results of card games where the strongest card wins. The cards' setup is as follows: each local candidate of a particular party gets proportionally many cards as their respective party's nation wide popularity, but the cards themselves are generated by calculations involving the names list of the particular voting district as changing random input. This results in the same suggestion in any given district, but changes from district to district - because of the semi-random nature of the applied hash function - so that each party's candidates have chances relating to the number of how many cards they have. Thus the final setup of the parliament is better going to represent each party according to their popularity because of probability.

The joker number, named after one of the Hungarian lottery games, is a real life random number, generated publicly not so much before election day, any lottery number does the trick. It is needed for several reasons:
1) by not being able to forecast the people finally suggested by the algorithm, the governments don't have enough time to provoke or politically attack them dedicatedly
2) due to statistical dispersion and the finite number of districts, some parties are going to be slightly over represented, others under compared to their measured popularity, and how this eventually turns out depends mostly on the lottery number entered
3) the distortion based fluctuations from 2) are going to be different at every election, as long as the current law is in power, and this algorithm is being applied by voters
4) if the same software is used for several elections throughout years, but at some small districts the names list wouldn't change, still everyone will always have a new a chance to win

Of course the entire offline distributed process is very sensitive to
 - application of the exact same algorithm by every voter
 - people entering proper data into their phones: locally candidate names, nationwide the same popularity results
 - selecting the common random number source that can't be silenced, censored at the very last moment yet is still widely accessable
 
As stated the process works offline, doesn't require any collection of voters' data and doesn't require more centralized coordination than named in the last list.

A _fallback plan_ in case of the existence of multiple diversly working applications, that would split voters' influence by not knowing which app to use, a fallback plan can be to vote still to the _first_ relevant oppositional candidate in the voting district in _alphabetical order_...

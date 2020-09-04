using System;
using System.Collections.Generic;
using System.Numerics;
using System.Security.Cryptography;
using System.Text;

namespace Zemberitenyezo
{
    class DistributedLoadedDice
    {
        private static string suggested = "";
        public static string algorithm(int length, List<string> names, List<int> chances, int joker)
        {
            BigInteger previousHash = BigInteger.Zero;
            for (int i = 0; i < length; i++)
                for (int j = 0; j < chances[i]; j++)
                {
                    byte[] bytes = Encoding.UTF8.GetBytes(names[i] + Convert.ToString(j) + Convert.ToString(joker));
                    SHA256Managed hashstring = new SHA256Managed();
                    byte[] hash = hashstring.ComputeHash(bytes);
                    BigInteger hashInt = new BigInteger(hash, true, true);
                    if (hashInt > previousHash)
                    {
                        suggested = names[i];
                        previousHash = hashInt;
                    }
                }
            return suggested;
        }
    }

    class BuktApp
    {
        static void Main(string[] args)
        {
            List<string> nevek = new List<string>();
            List<int> eselyek = new List<int>();
            int joker;
            Console.WriteLine("Hány nem listás ellenzéki jelölt indul a körzetében?");
            int indulokSzama = int.Parse(Console.ReadLine());
            float eselye;
            for (int index = 0; index < indulokSzama; index++)
            {
                Console.WriteLine(index + 1 + ". induló neve?");
                nevek.Add(Console.ReadLine());
                Console.WriteLine(index + 1 + ". induló népszerűsége (%)?");
                eselye = float.Parse(Console.ReadLine()) * 100;
                eselyek.Add((int) eselye);
            }
            Console.WriteLine("Kérem adja meg a legfrissebb Joker sorsoláson kihúzott 6 jegyű szelvény számot!");
            joker = int.Parse(Console.ReadLine());
            Console.WriteLine("Kérem szavazzon " +
                    DistributedLoadedDice.algorithm(indulokSzama, nevek, eselyek, joker) +
                    " nevű jelöltre!");
            Console.ReadLine();
        }
    }
}

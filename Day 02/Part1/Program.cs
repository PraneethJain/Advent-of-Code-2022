using System;
using System.IO;
using System.Collections.Generic;

namespace Part1
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, int> mapping = new Dictionary<string, int>() { { "A", 1 }, { "B", 2 }, { "C", 3 }, { "X", 4 }, { "Y", 5 }, { "Z", 6 } };
            string[] lines = File.ReadAllLines("input.txt");
            string[] plays;
            int result = 0, p1, p2;

            foreach (string line in lines)
            {
                plays = line.Split(' ');
                p1 = mapping[plays[0]];
                p2 = mapping[plays[1]];
                result += p2 - 3;
                if (p2 - p1 == 3)
                    result += 3;
                else if ((p1 == 1 && p2 == 5) || (p1 == 2 && p2 == 6) || (p1 == 3 && p2 == 4))
                    result += 6;
            }

            Console.WriteLine(result);
        }
    }
}
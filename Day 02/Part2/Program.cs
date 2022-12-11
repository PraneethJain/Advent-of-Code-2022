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

                if (p2 == 6)
                {
                    result += 6;
                    if (p1 == 1)
                        result += 2;
                    else if (p1 == 2)
                        result += 3;
                    else if (p1 == 3)
                        result += 1;
                }
                else if (p2 == 5)
                {
                    result += 3;
                    result += p1;
                }
                else
                {
                    if (p1 == 1)
                        result += 3;
                    else if (p1 == 2)
                        result += 1;
                    else
                        result += 2;
                }
            }

            Console.WriteLine(result);
        }
    }
}
using System;

namespace Parrot
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello.");
            Console.WriteLine("I am a parrot.");
            Console.WriteLine("What do you want me to say?");
            string UserWord;
            UserWord = Console.ReadLine();
            Console.WriteLine(UserWord + "!");
        }
    }
}
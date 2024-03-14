class Program
{
    static void Main(string[] args)
    {
        int upperLimit = 100;
        // List<int> primeNumbersList = Enumerable.Range(2, upperLimit).ToList();
        // foreach (var i in primeNumbersList)
        // {
        //     Console.WriteLine(i);    
        // }

        bool[] primeNumbers = new Boolean[upperLimit];

        int smallest = 2;
        while (smallest < upperLimit)
        {
            Console.WriteLine(smallest);
            
            for (int i = smallest * 2 - 1; i < upperLimit; i += smallest)
            {
                primeNumbers[i] = true;
            }

            for (int i = smallest + 1 - 1; i <= upperLimit; i++)
            {
                if (i == upperLimit)
                {
                    smallest = upperLimit + 1;
                    break;
                }
                if (primeNumbers[i] == false)
                {
                    smallest = i + 1;
                    break;
                }
            }
        }

        // for (int i = 1; i < upperLimit; i++)
        // {
        //     if (primeNumbers[i] == false)
        //     {
        //         Console.WriteLine(i + 1);
        //     }
        // }
        
    }
    
}

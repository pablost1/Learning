using System;
using System.Collections.Generic;
using System.Text;

namespace Dio
{
    class Xenlongao
    {
        static void Main(string[] args)
        {
            int N = Convert.ToInt32(Console.ReadLine());

            while(N-- > 0)
            {
                int resposta = 0;
                int val = Convert.ToInt32(Console.ReadLine());
                for(int i = 1; i <= val; i++){
                    int doev = 0 ; // doev == divisors of each value
                    for(int divisor = 1; divisor <= i; divisor++)
                    {
                        if((i%divisor)==0)
                        {
                            doev++;
                        }
                    }
                    if((doev%2)==0)
                    {
                        resposta++;
                    }
                }
                
                Console.WriteLine(resposta);
            }
        }
    }
}
using System; 

class DIO {

    static void Main(string[] args) { 

       for(int i = 1; i <= 9; i+=2)
            {
                for(int j = 7; j >= 5; j--)    //escreva seu código nos espaços em branco
                {
                  string output = string.Format("I={0} J={1}", i, j);
                  Console.WriteLine(output);
                }
            }
    }

}
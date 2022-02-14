using System;

class Program {
  
  static void Main(string[] args) {
    // Utilize Console.ReadLine para leitura do input de cada linha
    // Utilize Console.WriteLine para fazer o output de cada linha
    List<string> tesouro = new List<string>();

    while(true)
    {
      string joia = Console.ReadLine();
      if(!string.IsNullOrWhiteSpace(joia))
      {
        tesouro.Add(joia);
      }
      else
      {
        break;
      }
    }
    Console.WriteLine(tesouro.Distinct().Count());
  }
}
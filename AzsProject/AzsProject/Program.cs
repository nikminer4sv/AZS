using System;
using System.Text.Json;
using System.IO;
using System.Threading.Tasks;

namespace AzsProject {
    
    class Azs {
        public string Name { get; set; }
        public string Adress { get; set; }
        public string[] Coords { get; set; }
    }

    class Program {

        public const string _DATAFILE_PATH = "../../../JSONData.json";
        
        static async Task Main(string[] args) {

            string JSONFileData;
            
            using (FileStream FStream = File.OpenRead(_DATAFILE_PATH)) {

                byte[] Array = new byte[FStream.Length];
                await FStream.ReadAsync(Array, 0, Array.Length);
                JSONFileData = System.Text.Encoding.Default.GetString(Array);

            }
            
            Azs[] AzsArray = JsonSerializer.Deserialize<Azs[]>(JSONFileData);

            PrintArray(AzsArray);

        }
        
        public static void PrintArray(Azs[] AzsArray) {
            
            int Counter = 0;
            
            for (int i = 0; i < AzsArray.Length; i++) {
                
                Counter++;

                if (AzsArray[i].Coords[0] != "Error") {
                    Console.WriteLine("{0}. [{1}] [{2}, {3}] [{4}]",
                        Counter, AzsArray[i].Name, AzsArray[i].Coords[0],
                        AzsArray[i].Coords[1], AzsArray[i].Adress);
                } else {
                    Console.WriteLine("{0}. [{1}] [Error] [{2}]", 
                        Counter, AzsArray[i].Name,
                        AzsArray[i].Adress);
                }
                
            }
            
        }
        
    }
    
}

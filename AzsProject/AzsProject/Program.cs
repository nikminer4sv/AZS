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
        
        static async Task Main(string[] args) {

            string json;
            
            using (FileStream fstream = File.OpenRead("/home/nikminer4sv/RiderProjects/AzsProject/AzsProject/file.json")) {

                byte[] array = new byte[fstream.Length];
                await fstream.ReadAsync(array, 0, array.Length);
                json = System.Text.Encoding.Default.GetString(array);

            }
            
            Azs[] azs = JsonSerializer.Deserialize<Azs[]>(json);

            PrintArray(azs);

        }
        
        public static void PrintArray(Azs[] azs) {
            
            int counter = 0;
            
            for (int i = 0; i < azs.Length; i++) {
                
                counter++;
                
                if (azs[i].Coords[0] != "Error")
                    Console.WriteLine("{0}. [{1}] [{2}, {3}] [{4}]", counter, azs[i].Name, azs[i].Coords[0], azs[i].Coords[1],
                        azs[i].Adress);
                else
                    Console.WriteLine("{0}. [{1}] [Error] [{2}]", counter, azs[i].Name,
                        azs[i].Adress);
            }
            
        }
        
    }
    
}

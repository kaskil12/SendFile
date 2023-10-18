using System;
using System.IO;
using System.Net;
using System.Net.Sockets;

class FileSender
{
    static void Main()
    {
        // Replace with the actual IP address and port you want to send the file to
        string ipAddress = "192.168.98.170";
        int port = 3000;

        // Replace with the file path you want to send
        string filePath = @"C:\Users\kaspe\OneDrive\Desktop\penisssssssss.fbx";

        SendFile(ipAddress, port, filePath);
    }

    static void SendFile(string ipAddress, int port, string filePath)
    {
        try
        {
            using (TcpClient client = new TcpClient(ipAddress, port))
            using (NetworkStream stream = client.GetStream())
            using (FileStream fileStream = File.OpenRead(filePath))
            {
                byte[] buffer = new byte[1024];
                int bytesRead;

                while ((bytesRead = fileStream.Read(buffer, 0, buffer.Length)) > 0)
                {
                    stream.Write(buffer, 0, bytesRead);
                }

                Console.WriteLine("File sent successfully.");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}

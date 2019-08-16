using System;
using UnityEngine;

public class logs
{

    /*local variables*/
    static logs manager = new logs();
    public int static_ad_count = 0;

    public static logs sharedInstance()
    {
        return manager;
    }

    public static void writeToFile(string data)
    {
        System.IO.File.AppendAllText("C://xampp//htdocs//desim//visualization//uvisual.txt", data);
    }

}

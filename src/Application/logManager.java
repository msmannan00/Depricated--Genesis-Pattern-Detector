package Application;

public class logManager
{
    public static void loge(String log)
    {
        fileManager.writeLogs("C:\\xampp\\htdocs\\desim\\Command\\cmd_backup.txt","Syslogs : "+log + "\n");
    }
}

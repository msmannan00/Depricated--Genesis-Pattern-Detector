package Application;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class helperMethod
{
    public static String extractClassName(String content)
    {
        Pattern r = Pattern.compile("class( )+[a-zA-Z0-9_]*([ \\n])*(extends|implements)?([ \\n])*[a-zA-Z0-9_]*([ \\n])*\\{");

        // Now create matcher object.
        Matcher m = r.matcher(content);

        String matchResult = "";
        while (m.find())
        {
            matchResult=m.group();
            break;
        }
        matchResult=matchResult.replaceAll("class","");
        matchResult = matchResult.split("\\{")[0].split("extends")[0].split("implements")[0];
        return matchResult;
    }

    public static String extractParemeters(String content)
    {
        Pattern r = Pattern.compile("(String|void) +[a-zA-Z0-9]*\\(([a-zA-Z0-9 ,]*)\\)");

        // Now create matcher object.
        Matcher m = r.matcher(content);

        String matchResult = "";
        int maxParam = 0;
        while (m.find())
        {
            matchResult=m.group();
            int count = matchResult.split(",").length;
            if(count>maxParam)
            {
                maxParam = count;
            }
        }
        if(maxParam>=constants.maxParamLen)
        {
            return " :: LongParamSmell";
        }
        else
        {
            return "";
        }
    }

    public static String findRegex(String regex,String str)
    {
        // String to be scanned to find the pattern.

        // Create a Pattern object

        Pattern r = Pattern.compile(regex);

        // Now create matcher object.
        Matcher m = r.matcher(str);
        System.out.println(regex + " - ------- \n\n\n\n");
        System.out.println(str);


        String matchResult = "";
        int counter=1;
        while (m.find())
        {
            matchResult=matchResult+"Instance#"+counter+" : "+m.group()+"_____";
            counter++;
        }

        return matchResult;
    }

    public static void openPythonProject() throws IOException, InterruptedException
    {
        File file = new File(("Classifier\\main.py"));

        List<String> list = new ArrayList<String>();
        list.add("python.exe");
        String absPath = file.getAbsolutePath();

        System.out.println("absPath>>"+absPath);

        list.add(absPath);
        ProcessBuilder pb = new ProcessBuilder(list);
        Process process = pb.start();

        InputStream inputStream = process.getInputStream();
        byte[] b = new byte[1024 * 1024];// {(byte) 1024};
        while (inputStream.read(b) > 0) {
            System.out.println("b.length>>"+new String(b));
        }

        process.waitFor();
        System.out.println("exitValue()>>"+process.exitValue());
    }

    public static boolean detectGodClassCodeSmell(String code)
    {
        boolean status = false;

        if(code.length()>6000 || (findRegex("(String|void) +[a-zA-Z0-9]*\\(([a-zA-Z0-9 ,]*)\\)",code).split("public").length + findRegex("(String|void) +[a-zA-Z0-9]*\\(([a-zA-Z0-9 ,]*)\\)",code).split("private").length)>15)
        {
            status = true;
        }

        return status;
    }


}

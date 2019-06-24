package Application;

import org.apache.commons.io.FilenameUtils;

import java.io.*;
import java.nio.file.Files;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class fileManager
{
    public static String readFromFile(String path)
    {
        File file = new File(path);
        Scanner sc = null;
        String command = "";
        try
        {
            sc = new Scanner(file);
            while (sc.hasNextLine())
            {
                command = command + sc.nextLine();
                break;
            }
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }

        return command;
    }

    public static String readCompleteFile(String path)
    {
        File file = new File(path);
        Scanner sc = null;
        String command = "";
        try
        {
            sc = new Scanner(file);
            while (sc.hasNextLine())
            {
                command = command + sc.nextLine();
            }
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }

        return command;
    }

    public static void removeFirstLine(String fileName) throws IOException {
        RandomAccessFile raf = new RandomAccessFile(fileName, "rw");
        //Initial write position
        long writePosition = raf.getFilePointer();
        raf.readLine();
        // Shift the next lines upwards.
        long readPosition = raf.getFilePointer();

        byte[] buff = new byte[1024];
        int n;
        while (-1 != (n = raf.read(buff)))
        {
            raf.seek(writePosition);
            raf.write(buff, 0, n);
            readPosition += n;
            writePosition += n;
            raf.seek(readPosition);
        }
        raf.setLength(writePosition);
    }

    static void  indexFiles(File[] arr,String name,int index,int level,String allowedTypes) throws IOException
    {
        if(level>dataset.getInstance().fmodel.maxDepth)
        {
            dataset.getInstance().fmodel.maxDepth = level;
        }
        // terminate condition
        if(index == arr.length)
        {
            return ;
        }

        if(arr[index].isFile() && status.global_file_support.contains(FilenameUtils.getExtension(arr[index].getName())))
        {
            System.out.println(arr[index].toPath());
            double lineCount = 0;
            try
            {
                lineCount = Files.lines(arr[index].toPath()).count();
            }
            catch (Exception ex)
            {
                //ex.printStackTrace();
                lineCount = 0;
            }
            if (allowedTypes.contains(FilenameUtils.getExtension(arr[index].getName())) || allowedTypes.equals("all"))
            {
                String content = "";
                String classf = "";
                String classp = "";

                if(FilenameUtils.getExtension(arr[index].getName()).equals("java"))
                {
                    content = readCompleteFile(arr[index].getAbsolutePath());
                    String className = helperMethod.extractClassName(content);
                    classf = "<br>" + className+".class";
                    classp = "" + helperMethod.extractParemeters(content);
                    dataset.getInstance().classes.add(className);
                    dataset.getInstance().classcode.add(content);
                }
                dataset.getInstance().file_list.add(arr[index].getPath());
                dataset.getInstance().fmodel.filteredFiles+=1;
                dataset.getInstance().fmodel.filteredLines += lineCount;
                dataset.getInstance().fmodel.filteredFilesSize += arr[index].length();
                dataset.getInstance().fmodel.filesList += "\n"+arr[index].getName()+classf+classp;
            }
            dataset.getInstance().fmodel.totalFiles+=1;
            dataset.getInstance().fmodel.totalLines += lineCount;
            dataset.getInstance().fmodel.totalFilesSize += arr[index].length();
            if(dataset.getInstance().fmodel.largestFile<arr[index].length())
            {
                dataset.getInstance().fmodel.largestFile = arr[index].length();
            }
            if(dataset.getInstance().fmodel.smallestFile>arr[index].length())
            {
                dataset.getInstance().fmodel.smallestFile = arr[index].length();
            }
        }
        // for sub-directories
        else if(arr[index].isDirectory())
        {
            indexFiles(arr[index].listFiles(),arr[index].getName(),0, level + 1,allowedTypes);
            dataset.getInstance().fmodel.totalDirectories+=1;
        }

        // recursion for main directory
        indexFiles(arr,"null",++index, level,allowedTypes);
    }

    public static String extractClassesComments()
    {
        ArrayList<String> fileslist = dataset.getInstance().file_list;
        String regexResult = "";
        int classes = 0;
        int comments = 0;
        for(int counter=0;counter<fileslist.size();counter++)
        {
            String readString = readCompleteFile(fileslist.get(counter));
            if(!readString.equals(constants.empty_string))
            {
                classes += ( readString.split("public class", -1).length );
                comments += readString.split("//").length;
            }
        }
        writeFileModel("C:\\xampp\\htdocs\\desim\\visualization\\pvisual.txt",regexResult);
        String val = "Total Classes <strong>|</strong> " + classes+"\n"
                   + "Total Comments <strong>|</strong> " + comments+"\n";

        return val;
    }

    public static String  associationMapper()
    {
        String association = "";
        for(int counterupper=0;counterupper<dataset.getInstance().classes.size();counterupper++)
        {
            boolean status = false;
            status = helperMethod.detectGodClassCodeSmell(dataset.getInstance().classcode.get(counterupper));
            for(int counterinner=counterupper;counterinner<dataset.getInstance().classes.size();counterinner++)
            {
                if(dataset.getInstance().classes.get(counterupper).contains("admanager"))
                {
                    System.out.println("");
                }
                if(counterupper==counterinner)
                {
                    continue;
                }

                int relation1 = 0;
                int relation2 = 0;
                if(dataset.getInstance().classcode.get(counterupper).replaceAll(" ","").contains(dataset.getInstance().classes.get(counterinner).replaceAll(" ","")))
                {
                    relation1 = 1;
                    if(dataset.getInstance().classcode.get(counterupper).replaceAll(" ","").contains("<"+dataset.getInstance().classes.get(counterinner).replaceAll(" ","")))
                    {
                        relation1 = 2;
                    }
                }
                if(dataset.getInstance().classcode.get(counterinner).replaceAll(" ","").contains(dataset.getInstance().classes.get(counterupper).replaceAll(" ","")))
                {
                    relation2 = 1;
                    if(dataset.getInstance().classcode.get(counterinner).replaceAll(" ","").contains("<"+dataset.getInstance().classes.get(counterupper).replaceAll(" ","")))
                    {
                        relation2 = 2;
                    }
                }

                if(relation1 == 2 || relation2 == 2)
                {
                    if(relation1>0 && relation2>0)
                    {
                        association += "N Relation | " + dataset.getInstance().classes.get(counterupper) + " :: " + dataset.getInstance().classes.get(counterinner) + "\n";
                        association += " | isGodClass " + status + " | ";
                    }
                    else
                    {
                        association += "N Uniary Relation | " + dataset.getInstance().classes.get(counterupper) + " :: " + dataset.getInstance().classes.get(counterinner) + "\n";
                        association += " | isGodClass " + status + " | ";
                    }
                }
                else if(relation1 >= 1 && relation2 >= 1)
                {
                    association += "Binary Relation | " + dataset.getInstance().classes.get(counterupper) + " :: " + dataset.getInstance().classes.get(counterinner) + "\n";
                    association += " | isGodClass " + status + " | ";
                }
                else if(relation1 == 1 || relation2 == 1)
                {
                    association += "Uniary Relation | " + dataset.getInstance().classes.get(counterupper) + " :: " + dataset.getInstance().classes.get(counterinner) + "\n";
                    association += " | isGodClass " + status + " | ";
                }
            }
        }

        dataset.getInstance().classes.clear();
        dataset.getInstance().classcode.clear();

        return association;
    }

    public static void writeFileModel(fileModel model)
    {
        try
        {
            String associaltions = associationMapper();

            DecimalFormat df = new DecimalFormat("#.00");
            String fileContent = "Total Files <strong>|</strong> " + df.format(model.totalFiles)+"\n"
            + "Total Filtered Files <strong>|</strong> " + df.format(model.filteredFiles)+"\n"
            + "Filtered Percentage <strong>|</strong> " + df.format(model.filteredPercentage) +"%\n"
            + "Total Lines <strong>|</strong> " + df.format(model.totalLines)+"\n"
            + "Total Filtered Lines <strong>|</strong> " + df.format(model.filteredLines)+"\n"
            + "Average Lines Per File <strong>|</strong> " + df.format(model.averageLinesPerfile)+"\n"
            + "Filtered File Size <strong>|</strong> " + df.format(model.filteredFilesSize / 1024)+" kb\n"
            + "Total File Size <strong>|</strong> " + df.format(model.totalFilesSize / 1024)+" kb\n"
            + "Largest File Size <strong>|</strong> " + df.format(model.largestFile / 1024)+" kb\n"
            + "Smallest File Size <strong>|</strong> " + df.format(model.smallestFile / 1024)+" kb\n"
            + "Total Directories <strong>|</strong> " + df.format(model.totalDirectories)+"\n"
            + "Max Depth <strong>|</strong> " + df.format(model.maxDepth)+"\n"
            + extractClassesComments()
            + "</div><h2>Files List</h2><div class=\"list-group\">"
            + model.filesList
            + "</div><h2>Association List</h2><div class=\"list-group\">"
            + associaltions;

            //<div class="list-group">

            FileWriter fileWriter = new FileWriter(constants.fVisualPath,true);
            fileWriter.write(fileContent);
            fileWriter.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    public static void writeLogs(String dest,String str)
    {
        try
        {
            FileWriter fileWriter = new FileWriter(dest,true);
            fileWriter.write(str);
            fileWriter.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    public static void writeFileModel(String dest,String str)
    {
        try
        {
            FileWriter fileWriter = new FileWriter(dest);
            fileWriter.write(str);
            fileWriter.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    public static void matchParserFromFiles(String pattern)
    {
        ArrayList<String> fileslist = dataset.getInstance().file_list;
        String regexResult = "";
        for(int counter=0;counter<fileslist.size();counter++)
        {
            String readString = readCompleteFile(fileslist.get(counter));
            readString = htmlParserHelper.parseHTML(pattern,readString);
            if(!readString.equals(constants.empty_string))
            {
                File path = new File(fileslist.get(counter));
                regexResult += path.getParent()+"\\"+path.getName() + " | " + readString + "-newstart-";
            }
        }
        writeFileModel("C:\\xampp\\htdocs\\desim\\visualization\\pvisual.txt",regexResult);
        System.out.println("SHIT : " + regexResult);
    }

    public static void matchRegexFromFiles(String regex)
    {


        ArrayList<String> fileslist = dataset.getInstance().file_list;
        String regexResult = "";
        for(int counter=0;counter<fileslist.size();counter++)
        {
            String readString = readCompleteFile(fileslist.get(counter));
            String data = helperMethod.findRegex(regex,readString);
            if(!data.equals(constants.empty_string))
            {
                File path = new File(fileslist.get(counter));
                regexResult += path.getParent()+"\\"+path.getName() + " | " + data + "-newstart-";
            }
        }
        writeFileModel("C:\\xampp\\htdocs\\desim\\visualization\\rvisual.txt",regexResult);
    }

}

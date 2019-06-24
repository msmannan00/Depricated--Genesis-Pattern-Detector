package Application;

import java.io.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
import org.apache.commons.io.FileUtils;

public class UnRar
{
    private static final int BUFFER_SIZE = 4096;

    public static void unzip(String zipFilePath, String destDr) throws IOException
    {
        File dirc = new File(zipFilePath);
        File[] listOfFiles = dirc.listFiles();
        if(listOfFiles.length<=0)
        {
            return;
        }
        FileUtils.cleanDirectory(new File("C:\\xampp\\htdocs\\desim\\Extracted_Source\\"));
        zipFilePath = listOfFiles[0].getAbsolutePath();


        File destDir = new File(destDr);
        if (!destDir.exists())
        {
            destDir.mkdir();
        }
        ZipInputStream zipIn = new ZipInputStream(new FileInputStream(zipFilePath));
        ZipEntry entry = zipIn.getNextEntry();
        // iterates over entries in the zip file
        while (entry != null)
        {
            String filePath = destDr + File.separator + entry.getName();
            if (!entry.isDirectory())
            {
                extractFile(zipIn, filePath);
            }
            else
            {
                File dir = new File(filePath);
                dir.mkdir();
            }
            zipIn.closeEntry();
            entry = zipIn.getNextEntry();
        }
        zipIn.close();

    }

    private static void extractFile(ZipInputStream zipIn, String filePath) throws IOException
    {
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(filePath));
        byte[] bytesIn = new byte[BUFFER_SIZE];
        int read = 0;
        while ((read = zipIn.read(bytesIn)) != -1) {
            bos.write(bytesIn, 0, read);
        }
        bos.close();
    }

}
package Application;

import java.util.ArrayList;

public class dataset {
    private static dataset ourInstance = new dataset();

    public static dataset getInstance() {
        return ourInstance;
    }
    public ArrayList<String> file_list = new ArrayList<String>();
    public ArrayList<String> classes = new ArrayList<String>();
    public ArrayList<String> classcode = new ArrayList<String>();
    public fileModel fmodel = new fileModel();

    private dataset()
    {
    }
}

package Application;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class htmlParserHelper
{
    public static String parseHTML(String pattern,String html)
    {

        try
        {
            Document doc = Jsoup.parse(html);
            String parsedData="";
            int counter = 0;

            if(pattern.contains("all_images"))
            {
                Elements img = doc.getElementsByTag("img");
                for (Element tag : img)
                {
                    parsedData+=tag.attr("src")+"_____";
                }
            }
            if(pattern.contains("all_urls"))
            {
                Elements src = doc.getElementsByTag("a[href]");
                for (Element tag : src)
                {
                    parsedData+=tag.attr("abs:src")+"_____";
                }
            }
            if(pattern.contains("metadata"))
            {
                Elements metaTags = doc.getElementsByTag("meta");

                for (Element metaTag : metaTags)
                {
                    parsedData+=metaTag.attr("content")+"_____";
                }
            }
            if(pattern.contains("par"))
            {
                Elements src = doc.getElementsByTag("p");
                for (Element tag : src)
                {
                    parsedData+=tag.text()+"_____";
                }
            }
            if(pattern.contains("title"))
            {
                parsedData = doc.title();
            }
            return parsedData;
        }
        catch (Exception ex)
        {
            ex.printStackTrace();
            return constants.empty_string;
        }
    }

}

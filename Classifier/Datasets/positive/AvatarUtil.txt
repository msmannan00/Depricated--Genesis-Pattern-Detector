package com.pwxcoo.github.utils;

import com.talanlabs.avatargenerator.Avatar;
import com.talanlabs.avatargenerator.GitHubAvatar;
import org.apache.commons.lang3.RandomStringUtils;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.io.File;
import java.util.Random;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.utils
 * @email pwxcoo@gmail.com
 * @time 2018/10/02 14:30
 * @description
 */
@Component
public class AvatarUtil {


    private static String avatarPath;

    @Value("${avatar.directory}")
    public void setAvatarPath(String dir) {
        avatarPath = dir;
    }

    public static String generateAvatar(Long code) {
        Avatar avatar = GitHubAvatar.newAvatarBuilder().size(256, 256).build();

        try {
            String f = RandomStringUtils.randomAlphanumeric(8) + ".png";
//            System.out.println((new File(f).getAbsolutePath()));
            avatar.createAsPngToFile(code, new File(avatarPath + f));
            return f;
        } catch (Exception e) {
            throw e;
        }

    }

    public static String generateAvatar() {
        Avatar avatar = GitHubAvatar.newAvatarBuilder().build();

        return generateAvatar(new Random().nextLong());
    }

    public static Boolean deleteAvatar(String f) {

        File file = new File(avatarPath + f);
        if (file.exists()) {
            file.delete();
            return true;
        }
        return false;

    }

    public static String getAvatarUrl(String f) {
        return "/static/avatar/" + f;
    }

}

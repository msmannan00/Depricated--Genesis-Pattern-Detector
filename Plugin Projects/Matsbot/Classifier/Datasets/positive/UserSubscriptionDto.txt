package com.pwxcoo.github.dto;

import lombok.Data;

import java.util.Date;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.dto
 * @email pwxcoo@gmail.com
 * @time 2018/10/05 12:01
 * @description
 */
@Data
public class UserSubscriptionDto {

    private Long userId;
    private String username;
    private String userAvatar;
    private String action;  // 'follow'
    private String actionObject;
    private String actionAvatar;
    private String actionBio;
    private Date time;

}

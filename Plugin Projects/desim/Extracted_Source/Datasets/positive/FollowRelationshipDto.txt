package com.pwxcoo.github.dto;

import lombok.Data;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.dto
 * @email pwxcoo@gmail.com
 * @time 2018/10/05 18:41
 * @description
 */
@Data
public class FollowRelationshipDto {

    private Long followerId;
    private String followerUsername;
    private String followerAvatar;
    private Long followingId;
    private String followingUsername;
    private String followingAvatar;
}

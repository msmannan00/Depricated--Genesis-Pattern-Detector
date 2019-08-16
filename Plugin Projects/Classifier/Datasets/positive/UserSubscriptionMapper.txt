package com.pwxcoo.github.mapper;

import com.pwxcoo.github.dto.UserSubscriptionDto;
import com.pwxcoo.github.model.type.Action;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.mapper
 * @email pwxcoo@gmail.com
 * @time 2018/10/05 11:53
 * @description
 */
@Mapper
@Repository
public interface UserSubscriptionMapper {


    @Select("SELECT \n" +
            "    *\n" +
            "FROM\n" +
            "    (\n" +
            "    SELECT \n" +
            "        t.user_id as user_id, t.action as action, t1.username as username, \n" +
            "        t1.avatar as user_avatar, t2.username as action_object, t2.avatar as action_avatar, \n" +
            "        t2.bio as action_bio, t.creation_time as time\n" +
            "    FROM \n" +
            "        user_subscription t\n" +
            "        JOIN user t1 ON t.user_id = t1.user_id\n" +
            "        JOIN user t2 ON t.action_id = t2.user_id\n" +
            "    ) f1\n" +
            "JOIN \n" +
            "    (\n" +
            "        SELECT \n" +
            "            following_id\n" +
            "        FROM\n" +
            "            follow_relationship\n" +
            "        WHERE\n" +
            "            follower_id = #{user_id}\n" +
            "    ) f2\n" +
            "ON\n" +
            "    f1.user_id = f2.following_id\n" +
            "ORDER BY\n" +
            "    time DESC;\n")
    List<UserSubscriptionDto> getSubscriptionByUserId(@Param("user_id") Long userId);

    @Insert("INSERT INTO user_subscription(user_id, action, action_id) VALUES(#{user_id}, #{action}, #{action_id})")
    int insertUserSubscription(@Param("user_id") Long userId, @Param("action") Action action, @Param("action_id") Long actionId);
}

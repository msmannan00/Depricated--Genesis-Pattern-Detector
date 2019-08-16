package com.pwxcoo.github.mapper;

import com.pwxcoo.github.dto.FollowRelationshipDto;
import com.pwxcoo.github.model.data.FollowRelationship;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.mapper
 * @email pwxcoo@gmail.com
 * @time 2018/10/05 18:40
 * @description
 */
@Mapper
@Repository
public interface FollowRelationshipMapper {

    @Select("SELECT * FROM follow_relationship WHERE follower_id = #{follower_id} AND following_id = #{following_id}")
    FollowRelationship getFollowRelationship(@Param("follower_id") Long followId, @Param("following_id") Long followingId);

    @Insert("INSERT INTO follow_relationship(follower_id, following_id) VALUES (#{follower_id}, #{following_id})")
    int addFollowRelationship(@Param("follower_id") Long followId, @Param("following_id") Long followingId);

    @Delete("DELETE FROM follow_relationship WHERE follower_id = #{follower_id} AND following_id = #{following_id}")
    int deleteFollowRelationship(@Param("follower_id") Long followId, @Param("following_id") Long followingId);

    @Select("SELECT\n" +
            "    *\n" +
            "FROM\n" +
            "(\n" +
            "SELECT \n" +
            "    t.follower_id, t.following_id, t1.username as follower_username, t2.username as following_username, t1.avatar as follower_avatar, t2.avatar as following_avatar\n" +
            "FROM\n" +
            "    follow_relationship t\n" +
            "    JOIN user t1 ON t1.user_id = t.follower_id\n" +
            "    JOIN user t2 ON t2.user_id = t.following_id\n" +
            ") AS tt\n" +
            "WHERE\n" +
            "    tt.follower_id = #{follower_id};\n")
    List<FollowRelationshipDto> getAllFollowingByFollowerId(@Param("follower_id") Long followerId);

    @Select("SELECT\n" +
            "    *\n" +
            "FROM\n" +
            "(\n" +
            "SELECT \n" +
            "    t.follower_id, t.following_id, t1.username as follower_username, t2.username as following_username, t1.avatar as follower_avatar, t2.avatar as following_avatar\n" +
            "FROM\n" +
            "    follow_relationship t\n" +
            "    JOIN user t1 ON t1.user_id = t.follower_id\n" +
            "    JOIN user t2 ON t2.user_id = t.following_id\n" +
            ") AS tt\n" +
            "WHERE\n" +
            "    tt.following_id = #{following_id};")
    List<FollowRelationshipDto> getAllFollowerByFollowingId(@Param("following_id") Long followingId);
}

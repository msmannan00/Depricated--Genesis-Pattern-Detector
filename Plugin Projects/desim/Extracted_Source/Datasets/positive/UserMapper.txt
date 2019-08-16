package com.pwxcoo.github.mapper;

import com.pwxcoo.github.model.data.User;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.mapper
 * @email pwxcoo@gmail.com
 * @time 2018/09/30 19:56
 * @description
 */
@Mapper
@Repository
public interface UserMapper {

    @Select("SELECT * FROM user WHERE user_id = #{user_id}")
    User findUserByUserId(@Param("user_id") Long userId);

    @Select("SELECT * FROM user WHERE email = #{email}")
    User findUserByEmail(@Param("email") String email);

    @Select("SELECT * FROM user WHERE username = #{username}")
    User findUserByUsername(@Param("username") String username);

    @Insert("INSERT INTO USER(username, avatar, email, password, salt) VALUES(#{username}, #{avatar}, #{email}, #{password}, #{salt})")
    int insertUser(@Param("username") String username, @Param("avatar") String avatar, @Param("email") String email, @Param("password") String password, @Param("salt") String salt);

    @Delete("DELETE FROM user WHERE email = #{email}")
    int deleteUserByEmail(@Param("email") String email);
}

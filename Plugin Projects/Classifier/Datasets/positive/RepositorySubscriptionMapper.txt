package com.pwxcoo.github.mapper;

import com.pwxcoo.github.dto.RepositorySubscriptionDto;
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
 * @time 2018/10/05 15:35
 * @description
 */
@Mapper
@Repository
public interface RepositorySubscriptionMapper {

    @Select("SELECT * FROM repository_subscription WHERE user_id = #{user_id}")
    List<RepositorySubscriptionDto> getRepositorySubscriptionByUserId(@Param("user_id") Long userId);

    @Insert("INSERT INTO repository_subscription(user_id, action, repository_id) VALUES(#{user_id}, #{action}, #{repository_id})")
    int insertRepositorySubscription(@Param("user_id") Long userId, @Param("action") Action action, @Param("repository_id") Long repositoryId);

}

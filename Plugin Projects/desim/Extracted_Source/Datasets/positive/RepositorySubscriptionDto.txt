package com.pwxcoo.github.dto;

import com.pwxcoo.github.model.type.Action;
import lombok.Data;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.dto
 * @email pwxcoo@gmail.com
 * @time 2018/10/05 15:42
 * @description
 */
@Data
public class RepositorySubscriptionDto {

    private Long repositorySubscriptionId;
    private Long userId;
    private Action action;     // 'star', 'create', 'fork'
    private Long repositoryId;
}

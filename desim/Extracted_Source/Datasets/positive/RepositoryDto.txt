package com.pwxcoo.github.dto;

import lombok.Data;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.dto
 * @email pwxcoo@gmail.com
 * @time 2018/10/05 10:59
 * @description
 */
@Data
public class RepositoryDto {

    private String description;
    private String repositoryName;
    private Integer repositoryStar;
    private Integer repositoryFork;
    private String username;
}

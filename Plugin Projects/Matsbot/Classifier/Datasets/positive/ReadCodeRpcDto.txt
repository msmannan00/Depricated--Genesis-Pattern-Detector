package com.pwxcoo.github.dto;

import lombok.Data;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.dto
 * @email pwxcoo@gmail.com
 * @time 2018/10/07 16:27
 * @description
 */
@Data
public class ReadCodeRpcDto {

    private String username;
    private String repositoryName;
    private String commitId;
    private String filename;
    private String fileContent;
}

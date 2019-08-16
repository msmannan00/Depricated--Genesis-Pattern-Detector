package com.pwxcoo.github.controller;

import com.pwxcoo.github.dto.RepositoryDto;
import com.pwxcoo.github.service.repository.RepositoryService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.controller
 * @email pwxcoo@gmail.com
 * @time 2018/10/04 12:04
 * @description
 */
@Controller
@Slf4j
public class RepositoryController {

    @Autowired
    RepositoryService repositoryService;

    @RequestMapping(value = "/{username}/{repositoryName}", method = RequestMethod.GET)
    public String getRepository(ModelMap modelMap, @PathVariable("username") String username, @PathVariable("repositoryName") String repositoryName) {

        RepositoryDto repositoryDto = repositoryService.getRepositoryByRepositoryNameAndUsername(username, repositoryName);
//        System.out.println(repositoryDto.toString());


        modelMap.addAttribute("repository", repositoryDto);
        return "code";
    }
}

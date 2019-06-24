package com.pwxcoo.github.controller;

import com.pwxcoo.github.model.data.User;
import com.pwxcoo.github.service.user.UserService;
import com.pwxcoo.github.utils.SessionUtil;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.Optional;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.controller
 * @email pwxcoo@gmail.com
 * @time 2018/10/01 13:40
 * @description Home Module & Sign In Module
 */
@Controller
@Slf4j
public class HomeController {

    @Autowired
    UserService userService;

    @RequestMapping(value = "/", method = RequestMethod.GET)
    public String index(ModelMap modelMap) {
        Optional<HttpSession> session = SessionUtil.session();
        if (session.isPresent()) {
            User currentUser = userService.getUserByUsername(session.get().getAttribute("username").toString());

            return "home";
        } else {
            return "index";
        }
    }


    @RequestMapping(value = "/", method = RequestMethod.POST)
    public String login(ModelMap modelMap, @Param("email") String email, @Param("password") String password,
                        @Param("rememberMe") String rememberMe, HttpServletRequest request) {
        log.info("Remember Me: " + rememberMe);
        if (userService.validateUser(email, password) == false) {
            modelMap.addAttribute("error", true);
            return "index";
        } else {
            SessionUtil.storeSession(request, userService.getUserByEmail(email));

            if (rememberMe != null) {
                SessionUtil.session().get().setMaxInactiveInterval(3600 * 24 * 7);
            }

            return "redirect:/";
        }
    }
}

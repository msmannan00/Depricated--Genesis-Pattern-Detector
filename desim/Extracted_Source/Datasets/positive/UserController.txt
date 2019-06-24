package com.pwxcoo.github.controller;

import com.pwxcoo.github.model.data.User;
import com.pwxcoo.github.model.exception.NotFoundPageExcetpion;
import com.pwxcoo.github.service.user.UserService;
import com.pwxcoo.github.utils.SessionUtil;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.Optional;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.controller
 * @email pwxcoo@gmail.com
 * @time 2018/10/01 15:08
 * @description
 */
@Controller
@Slf4j
public class UserController {

    @Autowired
    UserService userService;

    @RequestMapping(value = "/signup", method = RequestMethod.GET)
    public String signUpPage(ModelMap modelMap) {
        Optional<HttpSession> session = SessionUtil.session();
        if (session.isPresent()) {
            return "redirect:/";
        } else {
            return "signup";
        }
    }


    @RequestMapping(value = "/signup", method = RequestMethod.POST)
    public String signUp(ModelMap modelMap, @Param("email") String email, @Param("username") String username,
                          @Param("password") String password, @Param("confirmPassword") String confirmPassword, HttpServletRequest request) {
        modelMap.addAttribute("error", true);
        if (password.equals(confirmPassword) == false) {
            modelMap.addAttribute("errorInfo", "The two password is inconsistent");
            return "signup";
        } else if (userService.getUserByEmail(email) != null) {
            modelMap.addAttribute("errorInfo", "The email had been registered");
            return "signup";
        } else if (userService.getUserByUsername(username) != null) {
            modelMap.addAttribute("errorInfo", "The username had been registered");
            return "signup";
        } else {
            User newUser = new User();
            newUser.setEmail(email);
            newUser.setUsername(username);
            newUser.setPassword(password);
            if (userService.createUser(newUser)) {
                SessionUtil.storeSession(request, userService.getUserByEmail(email));

                return "redirect:/";
            } else {
                modelMap.addAttribute("errorInfo", "Unknown Error, Please Contact: pwxcoo@gmail");
                return "signup";
            }
        }
    }

    @RequestMapping(value = "/{username}", method = RequestMethod.GET)
    public String profilePage(ModelMap modelMap, @PathVariable String username) throws NotFoundPageExcetpion {
        User user =  userService.getUserByUsername(username);
        if (user == null) throw new NotFoundPageExcetpion("没有这个用户");

        modelMap.addAttribute("user", user);
        log.info(userService.getUserByUsername(username).toString());
        return "user";
    }
}

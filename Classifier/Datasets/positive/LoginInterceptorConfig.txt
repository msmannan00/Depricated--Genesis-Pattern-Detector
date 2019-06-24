package com.pwxcoo.github.config;

import com.pwxcoo.github.interceptor.LoginInterceptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.config
 * @email pwxcoo@gmail.com
 * @time 2018/10/01 18:46
 * @description
 */
//@Component
public class LoginInterceptorConfig implements WebMvcConfigurer {

    @Autowired
    LoginInterceptor loginInterceptor;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(loginInterceptor);
    }
}

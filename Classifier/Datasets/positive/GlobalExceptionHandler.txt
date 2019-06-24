package com.pwxcoo.github.exception;

import com.pwxcoo.github.model.exception.NotFoundPageExcetpion;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.exception
 * @email pwxcoo@gmail.com
 * @time 2018/10/04 16:08
 * @description
 */
@ControllerAdvice
@Slf4j
public class GlobalExceptionHandler {

    public static final String DEFAULT_ERROR_VIEW = "default_error";
    public static final String NOT_FOUND_ERROR_VIEW = "not_found_error";

    @ExceptionHandler(value = Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ModelAndView defaultErrorHandler(HttpServletRequest httpServletRequest, Exception e) throws Exception {
        log.error(e.getMessage());

        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("exception", e);
        modelAndView.addObject("url", httpServletRequest.getRequestURL());
        modelAndView.setViewName(DEFAULT_ERROR_VIEW);

        return modelAndView;
    }

    @ExceptionHandler(value = NotFoundPageExcetpion.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ModelAndView  NotFoundPageErrorHandler(HttpServletRequest httpServletRequest, NotFoundPageExcetpion e) throws Exception {
        log.error(e.getMessage());

        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("username", httpServletRequest.getRequestURI().substring(1));
        modelAndView.addObject("exception", e);
        modelAndView.setViewName(NOT_FOUND_ERROR_VIEW);

        return modelAndView;
    }

}

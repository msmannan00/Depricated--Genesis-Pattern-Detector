package com.pwxcoo.github.exception;

import com.pwxcoo.github.model.exception.NotFoundException;
import com.pwxcoo.github.model.exception.ServerException;
import com.pwxcoo.github.model.exception.UnauthorizedException;
import com.pwxcoo.github.model.response.RestfulExceptionInfo;
import lombok.extern.slf4j.Slf4j;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

import javax.servlet.http.HttpServletRequest;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github.exception
 * @email pwxcoo@gmail.com
 * @time 2018/10/04 23:12
 * @description
 */
@ControllerAdvice
@Slf4j
@Order(Ordered.HIGHEST_PRECEDENCE)
public class RestfulExceptionHandler {

    @ExceptionHandler(value = ServerException.class)
    @ResponseBody
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public RestfulExceptionInfo ServerErrorHandler(HttpServletRequest httpServletRequest, ServerException e) throws ServerException {
        log.error(e.getMessage());
        return new RestfulExceptionInfo(org.apache.http.HttpStatus.SC_INTERNAL_SERVER_ERROR,
                e.getMessage(),
                httpServletRequest.getRequestURL().toString());
    }

    @ExceptionHandler(value = NotFoundException.class)
    @ResponseBody
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public RestfulExceptionInfo NotFoundErrorHandler(HttpServletRequest httpServletRequest, NotFoundException e) {
        log.error(e.getMessage());
        return new RestfulExceptionInfo(org.apache.http.HttpStatus.SC_NOT_FOUND,
                e.getMessage(),
                httpServletRequest.getRequestURL().toString());
    }


    @ExceptionHandler(value = UnauthorizedException.class)
    @ResponseBody
    @ResponseStatus(HttpStatus.UNAUTHORIZED)
    public RestfulExceptionInfo UnauthorizedErrorHandler(HttpServletRequest httpServletRequest, UnauthorizedException e) {
        log.error(e.getMessage());
        return new RestfulExceptionInfo(org.apache.http.HttpStatus.SC_UNAUTHORIZED,
                e.getMessage(),
                httpServletRequest.getRequestURL().toString());
    }
}

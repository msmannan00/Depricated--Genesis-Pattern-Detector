package com.pwxcoo.github.config;

import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurationSupport;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

/**
 * @author pwxcoo
 * @package com.pwxcoo.github
 * @email pwxcoo@gmail.com
 * @time 2018/10/01 12:01
 * @description
 */
//@Configuration
//@EnableSwagger2
public class Swagger2Config extends WebMvcConfigurationSupport {

    @Bean
    public Docket createRestApi() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.pwxcoo.github.api.restful"))
                .paths(PathSelectors.any())
                .build();
    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("Github - pwxcoo API Docs")
                .description("API docs built with Swagger2")
                .termsOfServiceUrl("https://blog.pwxcoo.com/")
                .contact("pwxcoo@gmail.com")
                .version("1.0")
                .build();
    }

//    @Override
//    public void addViewControllers(ViewControllerRegistry registry) {
//        registry.addRedirectViewController("/documentation/v2/api-docs", "/v2/api-docs");
//        registry.addRedirectViewController("/documentation/configuration/ui", "/configuration/ui");
//        registry.addRedirectViewController("/documentation/configuration/security", "/configuration/security");
//        registry.addRedirectViewController("/documentation/swagger-resources", "/swagger-resources");
//        registry.addRedirectViewController("/documentation", "/documentation/swagger-ui.html");
//        registry.addRedirectViewController("/documentation/", "/documentation/swagger-ui.html");
//    }
//
//    @Override
//    public void addResourceHandlers(ResourceHandlerRegistry registry) {
//        registry
//                .addResourceHandler("/documentation/**").addResourceLocations("classpath:/META-INF/resources/");
//    }

}

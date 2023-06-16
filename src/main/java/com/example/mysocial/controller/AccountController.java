package com.example.social.loginaction.controller;


import com.example.social.loginaction.model.Account;
import com.example.social.loginaction.service.AccountService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.server.reactive.HttpHandler;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.net.http.HttpHeaders;

@Controller
@RequestMapping("/")
public class AccountController {
    @GetMapping
    public String home(
            HttpSession session
    ){
        if(session != null && session.getAttribute("login") != null){
            boolean login = (boolean) session.getAttribute("login");
            if(login){
                return "redirect:/main";
            }
        }
        return "index";
    }

    @GetMapping("/join")
    public String joinpage(Model model){
        model.addAttribute("account", new Account());
        return "join";
    }
    @Autowired
    private AccountService accountService;

    @PostMapping("/join")
    public String join(Model model,
                       @ModelAttribute("account") Account account,
                       RedirectAttributes redirectAttributes){
        accountService.join(account);
        redirectAttributes.addFlashAttribute("msg", "정상가입완료");
        return "redirect:/";
    }
    @PostMapping("/login")
    public String login(HttpSession session,
                        HttpServletResponse response,
                        RedirectAttributes redirectAttributes,
                        @RequestParam("loginID") String loginID,
                        @RequestParam("password") String password
    ){
        Account account = (Account) accountService.login(loginID, password);

        if(account == null){
            redirectAttributes.addFlashAttribute("msg", "존재하지 않는 회원");
            return "redirect:/";
        }
        session.setAttribute("login", true);
        response.addCookie(new Cookie(
                "name", account.getName()
        ));
        return "redirect:/";
    }
    @GetMapping("/main")
    public String main(
            HttpSession session,
            @CookieValue("name") String name,
            Model model
    ){
        if(session != null && session.getAttribute("login") != null){
            boolean login = (boolean) session.getAttribute("login");
            if(login){
                model.addAttribute("msg", name + "님이 로그인");
                return "main";
            }
        }
        return "redirect:/";
    }
    @GetMapping("/logout")
    public String logout(
            HttpSession session,
            RedirectAttributes redirectAttributes
    ){
        if(session != null){
            session.invalidate();//세션 만료
            redirectAttributes.addFlashAttribute("msg", "로그아웃");
        }
        return "redirect:/";
    }
//    @GetMapping("/oauth/callback/kakao")
//    public String kakaoCallback(String code){
//        return "일단 성공 했고 code값:"+code;
//    }

}

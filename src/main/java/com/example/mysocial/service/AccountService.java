package com.example.social.loginaction.service;



import com.example.social.loginaction.model.Account;
import com.example.social.loginaction.repository.AccountRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AccountService {
    @Autowired
    private AccountRepository accountRepository;

    //join
    public void join(Account account){
        accountRepository.save(account);
    }

    //login
    public Account login(String loginID, String password){
        return (Account) accountRepository.findByLoginIDAndPassword(loginID, password);
    }

}

package com.example.mysocial.mylogin.repository;




import com.example.mysocial.mylogin.model.Account;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AccountRepository extends JpaRepository<Account, Long> {
    public Account findByLoginIDAndPassword(String loginID, String password);

}

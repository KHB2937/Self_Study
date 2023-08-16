package com.example.mysocial.OAuthlogin.repository;

import com.example.mysocial.OAuthlogin.model.Users;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<Users, Long> {
    Optional<Users> findByEmail(String email);
    Users findByEmailAndPassword(String email, String password);

    boolean existsUsersByEmail(String email);
}

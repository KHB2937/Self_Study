package com.example.mysocial.mylogin.model;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;


@Entity
@Data
public class Account {
    @Id
    @GeneratedValue
    Long id;
    String loginID;
    String password;
    String name;
    String email;

}
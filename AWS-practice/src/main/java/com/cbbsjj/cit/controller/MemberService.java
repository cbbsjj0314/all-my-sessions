package com.cbbsjj.cit.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MemberService {
    @GetMapping("/members")
    @ApiOperation("회원 조회")
    public void get() {

    }

    @PostMapping("/members")
    @ApiOperation("회원 등록")
    public void register() {

    }

    @DeleteMapping("/members")
    @ApiOperation("회원 삭제")
    public void delete() {

    }
}

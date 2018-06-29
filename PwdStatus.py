#!/usr/bin/env pytho      # -*- coding: utf-8 -*-

import math

class PwdStatus():

    class PwdStatusNode():

        def __init__(self, pwdStatus, action_step_num = 0, pre_pwdStatus=''):
            self.pwdStatus = pwdStatus
            self.action_step_num = action_step_num
            self.pre_pwdStatus = pre_pwdStatus

        def __eq__(self, other):
            return self.pwdStatus.__eq__(other.pwdStatus)

        def __hash__(self):
            return self.pwdStatus.__hash__()

    def __init__(self, pwd, cursor_position):
        self.pwd = pwd
        self.cursor_position = cursor_position

    #一次操作后的密码的状态
    def get_pwdStatus_after_action(self, action):
        new_pwd = self.pwd[:]
        new_cursor_position = self.cursor_position
        if action == 'SWAP1':
            #交换元素位置
            new_pwd[0] = new_pwd[0]^new_pwd[self.cursor_position]
            new_pwd[self.cursor_position] = new_pwd[0]^new_pwd[self.cursor_position]
            new_pwd[0] = new_pwd[0]^new_pwd[self.cursor_position]
        elif action == 'SWAP6':
            new_pwd[5] = new_pwd[5]^new_pwd[self.cursor_position]
            new_pwd[self.cursor_position] = new_pwd[5]^new_pwd[self.cursor_position]
            new_pwd[5] = new_pwd[5]^new_pwd[self.cursor_position]
        elif action == 'UP':
            new_pwd[self.cursor_position] = new_pwd[self.cursor_position] + 1 if new_pwd[self.cursor_position] + 1 < 10 else new_pwd[self.cursor_position]
        elif action == 'DOWN':
            new_pwd[self.cursor_position] = new_pwd[self.cursor_position] - 1 if new_pwd[self.cursor_position] - 1 >= 0 else new_pwd[self.cursor_position]
        elif action == 'LEFT':
            new_cursor_position = new_cursor_position - 1 if new_cursor_position - 1 >= 0 else new_cursor_position
        elif action == 'RIGHT':
            new_cursor_position = new_cursor_position + 1 if new_cursor_position + 1 < 6 else new_cursor_position

        return PwdStatus(new_pwd, new_cursor_position)

    def __eq__(self, other):
        if self.pwd == other.pwd and self.cursor_position == other.cursor_position:
            return True
        else:
            return False

    def __hash__(self):
        hash_num = 0
        for i in range(len(self.pwd)):
            hash_num += self.pwd * math.pow(10, i)
        hash_num += self.cursor_position * math.pow(10, len(self.pwd))
        return hash_num

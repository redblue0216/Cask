# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个cask配置分发包类，主要功能提供任意工程的打包、部署和版本管理。
"""
模块介绍
-------

这是一个cask配置分发包类，主要功能提供任意工程的打包、部署和版本管理。

设计模式：

    （1）  无 

关键点：    

    （1）tar压缩包管理

主要功能：            

    （1）提供任意工程的打包、部署和版本管理                               

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import os
import shutil
import sys



####### cask配置分发包类 ####################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）tar压缩包管理                                                    ###
### 主要功能：                                                           ###
### （1）提供任意工程的打包、部署和版本管理                                 ###
############################################################################


####### cask配置分发包类 ################################################################################
########################################################################################################



class Caskpkg(object):
    '''
    类介绍：

        这是一个cask配置分发包类，主要功能提供任意工程的打包、部署和版本管理。
    '''


    def __init__(self,objects,scripts,configs):
        '''
        属性功能：

            定义一个初始化属性的初始化方法

        参数：
            objects (str): 这是一个需要存储的工程对象文件
            scripts (str): 这是一个配置环境和安装对应包的脚本
            config (dict): 这是一个配置参数字典，主要包括name,version,casktype,remark,operator
        '''

        self.objects = objects
        self.scripts = scripts
        self.configs = configs


    def add_object(self,object_file,mode='copy_and_pack'):
        '''
        方法功能：

            定义一个添加对象的方法

        参数：
            object_file (str): 对象文件
            mode (str): 包括两种模式，move_and_pack打包并删除原有文件，copy_and_pack打包并保留原有文件

        返回：
            result (str): 运行结果信息
        '''

        ### 设置destination为当前程序目录下的.cask
        destination = '.cask/objects'
        if mode == 'copy_and_pack':
            ### 将文件复制到当前程序目录下的.cask隐藏文件夹下
            if os.path.isfile(object_file):
                shutil.copy(object_file,destination)
        elif mode == 'move_and_pack':
            ### 将文件移动到当前程序目录下的.cask隐藏文件夹下
            if os.path.isfile(object_file):
                shutil.copy(object_file,destination)
        else:
            print('Caskpkg add object error about mode!')


    def add_script(self,script_file,mode='copy_and_pack'):
        '''
        方法功能：

            定义一个添加脚本的方法

        参数：
            script_file (str): 脚本文件
            mode (str): 包括两种模式，move_and_pack打包并删除原有文件，copy_and_pack打包并保留原有文件

        返回：
            result (str): 运行结果信息
        '''

        ### 设置destination为当前程序目录下的.cask
        destination = '.cask/scripts'
        if mode == 'copy_and_pack':
            ### 将文件复制到当前程序目录下的.cask隐藏文件夹下
            if os.path.isfile(script_file):
                shutil.copy(script_file,destination)
        elif mode == 'move_and_pack':
            ### 将文件移动到当前程序目录下的.cask隐藏文件夹下
            if os.path.isfile(script_file):
                shutil.copy(script_file,destination)
        else:
            print('Caskpkg add script error about mode!')


    def add_config(self,config_file,mode='copy_and_pack'):
        '''
        方法功能：

            定义一个添加配置的方法

        参数：
            config_file (str): 配置文件
            mode (str): 包括两种模式，move_and_pack打包并删除原有文件，copy_and_pack打包并保留原有文件

        返回：
            result (str): 运行结果信息
        '''

        ### 设置destination为当前程序目录下的.cask
        destination = '.cask/configs'
        if mode == 'copy_and_pack':
            ### 将文件复制到当前程序目录下的.cask隐藏文件夹下
            if os.path.isfile(config_file):
                shutil.copy(config_file,destination)
        elif mode == 'move_and_pack':
            ### 将文件移动到当前程序目录下的.cask隐藏文件夹下
            if os.path.isfile(config_file):
                shutil.copy(config_file,destination)
        else:
            print('Caskpkg add config error about mode!')


    def commit(self):
        '''
        方法功能：

            定义一个提交实例中所有加载的对象文件、脚本文件和配置文件

        参数：
            无
        
        返回：
            result (str): 运行结果信息
        '''
        
        ### 判断系统平台类型，用于后续如果出现平台依赖问题，进行条件判断
        system_platform = sys.platform
        ### 遍历添加对象
        for tmp_object in self.objects:
            if os.path.isfile(tmp_object):
                self.add_object(object_file=tmp_object)
            else:
                tmp_file_list = os.listdir(tmp_object)
                for tmp_file in tmp_file_list:
                    ### 根据系统平台类型，进行条件判断
                    if system_platform == 'linux':
                        tmp_file = '{}/{}'.format(tmp_object,tmp_file)
                    elif system_platform == 'win32':
                        tmp_file = '{}\{}'.format(tmp_object,tmp_file)
                    self.add_object(tmp_file)
        ### 遍历添加脚本
        for tmp_script in self.scripts:
            if os.path.isfile(tmp_script):
                self.add_script(script_file=tmp_script)
            else:
                tmp_file_list = os.listdir(tmp_script)
                for tmp_file in tmp_file_list:
                    ### 根据系统平台类型，进行条件判断
                    if system_platform == 'linux':
                        tmp_file = '{}/{}'.format(tmp_script,tmp_file)
                    elif system_platform == 'win32':
                        tmp_file = '{}\{}'.format(tmp_script,tmp_file)
                    self.add_script(tmp_file)
        ### 遍历添加配置
        for tmp_config in self.configs:
            if os.path.isfile(tmp_config):
                self.add_config(config_file=tmp_config)
            else:
                tmp_file_list = os.listdir(tmp_config)
                for tmp_file in tmp_file_list:
                    ### 根据系统平台类型，进行条件判断
                    if system_platform == 'linux':
                        tmp_file = '{}/{}'.format(tmp_config,tmp_file)
                    elif system_platform == 'win32':
                        tmp_file = '{}\{}'.format(tmp_config,tmp_file)
                    self.add_config(tmp_file)
        result = 'Caskpkg commit well done!'
        print(result)
        
        

####################################################################################################################################
####################################################################################################################################



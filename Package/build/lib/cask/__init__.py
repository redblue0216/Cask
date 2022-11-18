# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个python包初始进入工作栈，主要功能提供基础操作函数，主要技术__all__
"""
模块介绍
-------

这是一个python包初始进入工作栈，主要功能提供基础操作函数，主要技术__all__

设计模式：

    （1）  无 

关键点：    

    （1）__all__

主要功能：            

    （1）基础操作函数集合                               

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import os
import sys
import tarfile
import yaml
import cask as ck
import dill
import io



####### 基础工具集合类 ######################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）__all__                                                        ###
### 主要功能：                                                           ###
### （1）基础操作函数集合                                                 ###
############################################################################


####### 基础操作函数集合 ####################################################################################
###########################################################################################################



### 暴露指定的公开接口
__all__ = ['create_cask_worksapce','generate_cask_package','install_caskpkg','seriallize','deseriallize']


### 创建cask工作空间
def create_cask_workspace():
    '''
    函数功能：

        定义一个创建cask工作空间的函数

    参数：
        无

    返回：
        result (str): 运行结果信息
    '''

    ### 判断系统平台类型，用于后续如果出现平台依赖问题，进行条件判断
    system_platform = sys.platform
    ### 配置基础路径
    if system_platform == 'linux':
        objects_path = './.cask/objects'
        scripts_path = './.cask/scripts'   
        configs_path = './.cask/configs'   
        logs_path = './.cask/logs'      
    elif system_platform == 'win32':
        objects_path = '.\.cask\objects'
        scripts_path = '.\.cask\scripts'   
        configs_path = '.\.cask\configs'   
        logs_path = '.\.cask\logs' 
    ### 开始创建对象、脚本、配置和日志文件夹
    if not os.path.exists(objects_path ):
        os.makedirs(objects_path )
    if not os.path.exists(scripts_path):
        os.makedirs(scripts_path)    
    if not os.path.exists(configs_path):
        os.makedirs(configs_path)  
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
    result = 'Cask create workspace well done!'
    print(result)


### 生成cask压缩包
def generate_cask_package(caskpkg_name):
    '''
    函数功能：

        定义一个生成cask压缩包的函数

    参数：
        caskpkg_name (str): cask压缩包名称

    返回：
        result (str): 运行结果信息
    '''

    ### 配置压缩包生成路径
    caskpkg_pack_path = '{}.caskpkg'.format(caskpkg_name)
    ### 将相关文件使用Tar打包
    tar = tarfile.open(name = caskpkg_pack_path,mode = 'w:gz') ### 此处的使用gzip压缩格式，在打包后的tar.gz中会嵌套存在一个tar包，此处由于改变了文件后缀，会显示同名文件嵌套
    tar.add(name='.cask',arcname='.cask')
    tar.close()
    ### 打包结束输出运行结果信息
    result = 'Cask generate cask package well done!'
    print(result)


### 安装cask包
def install_caskpkg(caskpkg_file):
    '''
    函数功能：

        定义一个安装cask压缩包的函数

    参数：
        caskpkg_file (str): cask压缩包文件

    返回：
        result (str): 运行结果信息
    '''

    ### 解压一个caskpkg压缩包
    tar = tarfile.open(name = caskpkg_file,mode = 'r:gz') ### 只是在当前路径下解压caskpkg
    tar.extractall()
    tar.close()
    ### 解压结束输出运行结果信息
    result = 'Cask install caskpkg well done!'
    print(result)


### 展示cask包配置
# def show_caskpkg_config():
#     pass


### 设置cask包配置
# def set_caskpkg_config():
#     pass


### 设置cask存储配置
# def set_caskstore_config():
#     pass


### 序列化
def seriallize(target_object,filepath = None):
    '''
    函数功能：

        定义一个序列化对象的函数

    参数：
        target_object (object): 具体python对象
        filepath (str): 序列化文件路径

    返回：
        dill_object (object): 序列化后对象
    '''

    if filepath == None:
        dill_object = dill.dumps(target_object)
        return dill_object
    else:
        file = open(filepath,"wb")
        dill.dump(target_object,file)
        file.close()
        return 'Seriallize well done!'


### 反序列化
def deseriallize(target_object = None,filepath = None):
    '''
    函数功能：

        定义一个反序列化对象的函数

    参数：
        target_object (object): 具体python对象
        filepath (str): 反序列化文件路径

    返回：
        normal_object (object): 反序列化后对象
    '''
    
    if filepath == None:            
        normal_object = dill.loads(target_object)
        return normal_object
    else:
        file = open(filepath,"rb")
        normal_object = dill.load(file)
        file.close()
        return normal_object


#############################################################################################################################################################
#############################################################################################################################################################



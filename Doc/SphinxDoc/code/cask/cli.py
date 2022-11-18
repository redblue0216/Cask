# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个cask常用命令行接口类
"""
模块介绍
-------

这是一个cask常用命令行接口类

设计模式：

    无

关键点：    

    （1）click 

主要功能：            

    （1）cask程序管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ###########################################################################################
#############################################################################################################



import click
from rich.console import Console
from cask import create_cask_workspace,generate_cask_package,install_caskpkg,seriallize,deseriallize
from cask.package import Caskpkg
from cask.store import CaskStore



####### CLI命令行接口 #######################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）click                                                           ###
### 主要功能：                                                            ###
### （1）cask程序管理                                                     ###
############################################################################



###### CLI命令行接口 #####################################################################
#########################################################################################


### cask命令组
@click.group()
@click.help_option('-H','--help')
@click.version_option('-V','--version')
def cask():
    console = Console()
    console.print("\n\
                   =========================================================================== \n\
                   =======                                                             ======= \n\
                   =======                    Hello! Welcome to Cask                   ======= \n\
                   =======                                                             ======= \n\
                   ===========================================================================",style="red")


### 创建cask工作空间
@click.command(help='cask create workspace')
def create_workspace():
    '''
    函数功能：

        定义一个创建工作空间的函数

    参数：
        无

    返回：
        无
    '''

    console = Console()
    console.print('====================================================>>>>>> cask create workspace well done!',style="red")
    ### 创建cask工作空间，生成.cask隐藏文件夹
    create_cask_workspace()


### 生成cask包
@click.command(help='cask generate package')
@click.option("--caskpkg_name",help="cask package name")
def generate_package(caskpkg_name):
    '''
    函数功能：

        定义一个生成cask包的函数

    参数：
        caskpkg_name (str): 包名称

    返回：
        无
    '''    

    console = Console()
    ### 生成cask包
    generate_cask_package(caskpkg_name=caskpkg_name)
    console.print('====================================================>>>>>> cask generate package well done!',style="red")


### 安装cask包，生成.cask隐藏文件夹
@click.command(help='cask install package')
@click.option("--caskpkg_file",help="cask package file")
def install_package(caskpkg_file):
    '''
    函数功能：

        定义一个安装cask包的函数

    参数：
        cacaskpkg_file (str): 包文件路径

    返回：
        无
    ''' 

    console = Console()
    ### 安装cask包，生成.cask隐藏文件夹
    install_caskpkg(caskpkg_file=caskpkg_file)
    console.print('====================================================>>>>>> cask install package well done!',style="red")


### 上传文件
@click.command(help='cask upload file')
@click.option("--endpoint",help="endpoint string")
@click.option("--bucket_name",help="bucket name")
@click.option("--object_name",help="object name")
@click.option("--file_path",help="file path")
def upload_file(endpoint,bucket_name,object_name,file_path):
    '''
    函数功能：

        定义一个上传文件的函数

    参数：
        endpoint (str): 存储连接信息
        bucket_name (str): 对象存储中桶的名称
        object_name (str): 二进制数据对象名称
        file_path (str): 文件名称

    返回：
        无
    ''' 

    console = Console()
    ### 初始化cask存储对象               
    caskstore = CaskStore(endpoint=endpoint)
    ### 上传文件
    result = caskstore.push_file(bucket_name=bucket_name,object_name=object_name,file_path=file_path)
    console.print('====================================================>>>>>> cask upload file well done!',style="red")    


### 下载文件
@click.command(help='cask upload file')
@click.option("--endpoint",help="endpoint string")
@click.option("--bucket_name",help="bucket name")
@click.option("--object_name",help="object name")
@click.option("--file_path",help="file path")
def download_file(endpoint,bucket_name,object_name,file_path):
    '''
    函数功能：

        定义一个下载文件的函数

    参数：
        endpoint (str): 存储连接信息
        bucket_name (str): 对象存储中桶的名称
        object_name (str): 二进制数据对象名称
        file_path (str): 文件名称

    返回：
        无
    ''' 

    console = Console()
    ### 初始化cask存储对象               
    caskstore = CaskStore(endpoint=endpoint)
    ### 下载文件
    result = caskstore.pull_file(bucket_name=bucket_name,object_name=object_name,file_path=file_path)
    console.print('====================================================>>>>>> cask download file well done!',style="red")



### 向cask命令组添加命令
cask.add_command(create_workspace)
cask.add_command(generate_package)
cask.add_command(install_package)
cask.add_command(upload_file)
cask.add_command(download_file)



### python脚本主程化
if __name__ == '__main__':
    console = Console()
    console.print("\n\
                =========================================================================== \n\
                =======                                                             ======= \n\
                =======                    Hello! Welcome to Cask                   ======= \n\
                =======                                                             ======= \n\
                ===========================================================================",style="red")
    cask()



#######################################################################################################################################################
#######################################################################################################################################################



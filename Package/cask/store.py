# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个cask存储管理类，主要功能管理cask远端存储，主要技术property动态属性和MinIO
"""
模块介绍
-------

这是一个cask存储管理类，主要功能管理cask远端存储，主要技术property动态属性和MinIO

设计模式：

    （1）  无 

关键点：    

    （1）MinIO

主要功能：            

    （1）远端存储管理                              

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import yaml
from minio import Minio
from minio.error import S3Error
import dill 
import io
import cask as ck




####### cask存储管理类 ######################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）MinIO                                                           ###
### 主要功能：                                                           ###
### （1）远端存储管理                                                     ###
############################################################################


####### cask存储管理类 #####################################################################################
###########################################################################################################



class CaskStore(object):
    '''
    类介绍：

        这是一个cask存储管理类，主要功能管理cask远端存储，主要技术property动态属性和MinIO
    '''


    def __init__(self,
                 endpoint,
                 access_key = 'minioadmin',
                 secret_key = 'minioadmin',
                 secure = False):
        '''
        属性功能：

            定义一个初始化属性的初始化方法

        参数：
            store_instance (object): 这是一个存储对象实例，此处为minio客户端
            store_parameter (dict): 这是一个存储参数字典，此处主要包括datatype和dataobj
        '''

        ### minio客户端连接
        minio_client = Minio(endpoint = endpoint,
                        access_key = access_key,
                        secret_key = secret_key,
                        secure= secure)
        ### 加载进类存储属性
        self.store_instance = minio_client


    def make_bucket(self,bucket_name):
        '''
        方法功能：

            定义一个创建桶名称的方法

        参数：
            bucket_name (str): 桶名称

        返回：
            result (str): 运行结果信息
        '''

        ### 开始创建桶空间操作
        found = self.store_instance.bucket_exists(bucket_name)
        if not found:
            self.store_instance.make_bucket(bucket_name)
            result = 'Bucket create well done!'
        else:
            result = 'Bucket already exists'
        print(result)
            
        return result 


    def push_file(self,bucket_name,object_name,file_path):
        '''
        方法功能：

            定义一个上传文件的方法

        参数：
            bucket_name (str): 对象存储中桶的名称
            object_name (str): 二进制数据对象名称
            file_path (str): 文件名称

        返回：
            result (str): 运行结果信息
        '''

        ### 开始推送文件
        self.store_instance.fput_object(bucket_name=bucket_name,object_name=object_name,file_path=file_path)
        result = '{} push well done!'.format(file_path)

        return result


    def push_object(self,bucket_name,object_name,bytes_obj):
        '''
        方法功能：

            定义一个向远端推送对象的方法

        参数：
            bucket_name (str): 对象存储中桶的名称
            object_name (str): 二进制数据对象名称
            bytes_obj (object): 二进制对象

        返回：
            result (str): 运行结果信息
        '''

        ### 检验minio的bucket是否存在，不存在则自动创建
        tmp_result = self.make_bucket(bucket_name = bucket_name)
        ### 开始推送对象
        self.store_instance.put_object(bucket_name=bucket_name,
                                       object_name=object_name,
                                       data=io.BytesIO(bytes_obj),
                                       length=-1,
                                       part_size=10 * 1024 * 1024)
        result = '{} put well done!'.format(object_name)
        print(result)
        return result


    def push(self):
        '''
        方法功能：

            定义一个向远端推送的方法

        参数：
            无

        返回：
            无
        '''

        pass


    def pull_file(self,bucket_name,object_name,file_path):
        '''
        方法功能：

            定义一个从远端拉文件的方法

        参数：
            bucket_name (str): 对象存储中桶的名称
            object_name (str): 二进制数据对象名称
            file_path (str): 文件名称

        返回：
            bytes_obj (object): 二进制对象
        '''

        ### 开始拉取文件操作
        self.store_instance.fget_object(bucket_name=bucket_name,object_name=object_name,file_path=file_path)
        result = '{} pull well done!'.format(file_path)

        return result


    def pull_object(self,bucket_name,object_name):
        '''
        方法功能：

            定义一个从远端拉对象的方法

        参数：
            bucket_name (str): 对象存储中桶的名称
            object_name (str): 二进制数据对象名称

        返回：
            bytes_obj (object): 二进制数据对象
        '''

        ### 开始下载对象
        response = self.store_instance.get_object(bucket_name=bucket_name,
                                        object_name=object_name)
        bytes_obj = response.read()
        print('{} get well done!'.format(object_name))

        return bytes_obj


    def list_objects(self):
        '''
        方法功能：

            定义一个列举出远端存储的对象的方法

        参数：
            无

        返回：
            无
        '''

        pass



######################################################################################################################################
######################################################################################################################################



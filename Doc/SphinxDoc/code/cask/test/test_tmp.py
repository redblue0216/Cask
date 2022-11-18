from cask import seriallize,deseriallize
from cask.store import CaskStore
import cask
### 判断系统平台类型，用于后续如果出现平台依赖问题，进行条件判断
# system_platform = sys.platform
# ### 开始创建对象、脚本、配置和日志文件夹
# objects_path = './.cask/objects'
# if not os.path.exists(objects_path ):
#     os.makedirs(objects_path )
# scripts_path = './.cask/scripts'
# if not os.path.exists(scripts_path):
#     os.makedirs(scripts_path)    
# configs_path = './.cask/configs'
# if not os.path.exists(configs_path):
#     os.makedirs(configs_path)  
# logs_path = './.cask/logs'
# if not os.path.exists(logs_path):
#     os.makedirs(logs_path)

def testfunc(a):
    return a + 1

# tmp_dill_object = seriallize(testfunc)
# de_tmp_dill_object = deseriallize(tmp_dill_object)
# seriallize(target_object=testfunc,filepath='testfunc.dill')
# de_tmp_dill_object = deseriallize(filepath='testfunc.dill')
# b = de_tmp_dill_object(1)
# print(b)


### 初始化cask存储对象               
caskstore = CaskStore(endpoint='192.168.1.82:9000')
### 序列化对象
testfunc_bytes_obj = cask.seriallize(target_object=testfunc)
### 上传二进制对象
result = caskstore.push_object(bucket_name='cask',object_name='testfunc',bytes_obj=testfunc_bytes_obj)
print(result)
### 获取二进制对象
tmp_bytes_obj = caskstore.pull_object(bucket_name='cask',object_name='testfunc')
### 反序列化对象
testfunc_bytes_obj_a = cask.deseriallize(target_object=tmp_bytes_obj)
print(testfunc_bytes_obj_a(1))
### 上传文件
result = caskstore.push_file(bucket_name='cask',object_name='testfunc.dill',file_path='testfunc.dill')
print(result)
### 获取文件
caskstore.pull_file(bucket_name='cask',object_name='testfunc.dill',file_path='testaaa.dill')
### 反序列化对象
testfunc_bytes_obj_aaa = cask.deseriallize(filepath='testaaa.dill')
print(testfunc_bytes_obj_aaa(2))

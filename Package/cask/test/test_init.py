from cask import create_cask_workspace,generate_cask_package,install_caskpkg,seriallize,deseriallize
from cask.package import Caskpkg


### 创建cask工作空间，生成.cask隐藏文件夹
# create_cask_workspace()


### 生成cask包
# generate_cask_package(caskpkg_name='testcask')


### 安装cask包，生成.cask隐藏文件夹
# install_caskpkg(caskpkg_file='testcask.caskpkg')


### 添加object_file到.cask下
# tmp_caskpkg = Caskpkg(objects=['logtest'],scripts=['logtest'],configs=['logtest'])
# tmp_caskpkg.commit()


### 序列化，反序列化测试
def testfunc(a):
    return a + 1
# tmp_dill_object = seriallize(testfunc)
# de_tmp_dill_object = deseriallize(tmp_dill_object)
# seriallize(target_object=testfunc,filepath='testfunc.dill')
de_tmp_dill_object = deseriallize(filepath='testfunc.dill')
b = de_tmp_dill_object(1)
print(b)


### 
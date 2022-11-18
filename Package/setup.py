from setuptools import setup,find_packages

setup(
        ### 包与作者信息
        name = 'cask',
        version = '0.1',
        author = 'shihua',
        author_email = "hua.shi@meritech-data.com",
        python_requires = ">=3.9.12",
        license = "MIT",

        ### 源码与依赖
        packages = find_packages(),
        include_package_data = True,
        description = 'Cash is a storage management tool, including project packaging and remote storage.',
        # install_requires = ['minio','yaml','click','console'],

        ### 包接入点，命令行索引
        entry_points = {
            'console_scripts': [
                'caskctl = cask.cli:cask'
            ]
        }      
)
# nsxapitest
This is for demo nsx api. Code by python

该脚本仅供 CT NSX API 测试使用！


执行环境准备如下：
1. 准备好待测对象：vShpere5.5 + NSX6.3 测试环境
2. 创建用于NSX API测试的用户，先在webClient->Administration->Users中创建用户，然后去webClient->NSXManager->Manage->Users处添加, 角色选Enterprise Administrator。


测试终端准备如下：
1. 测试终端可以是PC机也可以是VM，操作系统为Linux，建议选择带GUI的ubuntu15.10或者centos7，并且能够访问互联网络。
2. 确认Linux上已经安装好了python2.7.x，查看命令为： python -V
3. 确认pip已经安装，查看命令为： pip，如未安装则进行安装（sudo apt-get install python-pip）
4. 安装python包lxml，安装命令为： sudo pip install lxml，或 sudo apt-get install python-lxml，详情见 https://pypi.python.org/pypi/lxml/3.8.0
5. 安装python包pycurl，安装命令为： sudo apt-get install libcurl4-openssl-dev 或 sudo yum install libcurl-devel，详情见 https://pypi.python.org/pypi/pycurl 
6. 安装python包pyvmomi，安装命令为： sudo pip install pyvmomi，详情见 https://pypi.python.org/pypi/pyvmomi
7. 如果测试终端不能访问互联网络，请在以上网址先下载好安装包文件（tar.gz文件），然后传到该测试机进行安装，先执行解压命令（tar -zxvf xxxx.tar.gz），然后执行安装命令： sudo python setup.py install
8. 下载该测试脚本到测试终端，在nsx_basic_input.py中配置vCenter的用户名和密码(administrator@vsphere.local)和NSX API的用户名和密码(用第2步创建的，禁止使用admin)


测试步骤如下：
1. 编辑input文件进行参数配置，以netowrk/case04_nsx_network_get为例，先编辑case04_nsx_network_get_input.py，也有某些测试项不需要参数配置，则该测试项无对应的input.py文件
2. 执行script文件，以netowrk/case04_nsx_network_get为例，执行命令为： python ca04_nsx_network_get_script.py，观察测试是否顺利完成
3. 去log目录查看output文件，以netowrk/case04_nsx_network_get为例，输出文件名为：ca04_nsx_network_get_output_yyyymmddhhmmss.log

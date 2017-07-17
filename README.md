# nsxapitest
This is for demo nsx api. Code by python

该脚本仅供测试使用，执行环境准备如下：
1. 准备好待测对象：vShpere5.5 + NSX6.3 测试环境
2. 准备好用于测试的VM，要求如下：
	 1> linux环境，已安装 python2.7.*
	 2> 安装python包：lxml, pycurl, pyvmomi，如何安装请参考
	    https://pypi.python.org/pypi/lxml/3.8.0
		  https://pypi.python.org/pypi/pycurl 
		  https://pypi.python.org/pypi/pyvmomi
3. 下载该测试脚本到测试VM，在nsx_basic_input.py中配置vCenter和NSX的用户名和密码


测试步骤如下：
1. 编辑input文件进行参数配置，以netowrk/case04_nsx_network_get为例，先编辑case04_nsx_network_get_input.py，也有某些测试项不需要参数配置，则该测试项无对应的input.py文件
2. 执行script文件，以netowrk/case04_nsx_network_get为例，执行命令为： python ca04_nsx_network_get_script.py，观察测试是否顺利完成
3. 去log目录查看output文件，以netowrk/case04_nsx_network_get为例，输出文件名为：ca04_nsx_network_get_output_yyyymmddhhmmss.log

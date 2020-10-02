创建一个项目
==========
> gradle init --type scala-library

修改build.gradle，注意版本问题！

启动spark
=========
要进入到spark 2.4.7安装包目录下

第一种方式（仅本机）：
------------------
> ./sbin/start-master.sh -h localhost

> ./sbin/start-slave.sh spark://localhost:7077

第二种方式（多台电脑）：
--------------------
> ./sbin/start-master.sh -h localhost

> ./sbin/start-slave.sh spark://ip地址:7077

若要停止
-------
> ./sbin/stop-slave.sh

> ./sbin/stop-master.sh
*顺序不可反*

构建打包
=======
gradle build
gradle shadowJar

提交计算
=======
> spark-submit --master spark://localhost:7077 --class hello_01.SparkPi ./build/libs/hello_01-all.jar
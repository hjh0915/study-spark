cassandra转spark计算
===================
1、多项目构建
-----------
> gradle init --type scala-library
去除src目录，自建子目录，把src目录结构拷贝到子目录中
settings.gradle 增加子项目名称
> gradle :projects

修改build.gradle文件

2、构建打包
----------
> gradle build
> gradle shadowJar

子项目打包
> gradle :brchrpt:build
> gradle :brchrpt:shadowjar

3、启动spark
-----------
> ./sbin/start-master.sh -h localhost

> ./sbin/start-slave.sh spark://localhost:7077

4、提交计算
----------
> spark-submit --master spark://localhost:7077 --class brchqry.BrchQry ./brchqry/build/libs/brchqry-all.jar

> spark-submit --master spark://localhost:7077 --deploy-mode client --total-executor-cores 2 --executor-memory 512M --class hello_01.SparkPi ./build/libs/hello_01-all.jar
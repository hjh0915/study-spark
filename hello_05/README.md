更新sudo源
=========
> sudo apt-get update
若sudo安装没办法下载成功，需要更新sudo源

修改hostname
============
> sudo nano /etc/hostname
> sudo nano /etc/hosts
重启
> sudo reboot

时间同步
=======
参考资料: https://vitux.com/how-to-install-ntp-server-and-client-on-ubuntu/  
局域网内部集群服务器的时间同步
> sudo apt-get install ntp ntpdate

需要两台电脑
----------
两个ip地址
一个作为client
一个作为server
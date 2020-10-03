运行cassandra
============
> cassandra -f

访问cql
=======
> pyenv activate gopy3
> cqlsh -u cassandra -p cassandra localhost

修改cassandra配置
================
配置文件 conf/cassandra.yaml

```yaml
authenticator: PasswordAuthenticator
```

默认的用户/口令 cassandra/cassandra

```sql
alter user cassandra with password '1234';
create user test with password '1234;
```

```cql
list users;
login test '1234'
```

python读取cass
=============
先在python3中安装：
pip install cassandra-driver
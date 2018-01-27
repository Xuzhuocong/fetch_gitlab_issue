# fetch_gitlab_issue
由于GitLab没有导出issue的功能，因此写个小工具用于拉取GitLab中的issue列表。
当前脚本基于Gitlab v3版本的api，把issue列表导出到json文件中，而json文件可以很方便的转换成其他的文件格式，如xml、csv、excel等等。

## 环境
当前脚本需要运行在**Python3**环境下

## 使用
使用该脚本后，issue会输出到脚本所在目录下的叫做`issues.json`的文件中。
使用格式：
```shell
./fetchGitlabIssue.py http://host_to_gitlab "private token"
或
python3 ./fetchGitlabIssue.py http://host_to_gitlab "private token"
```

例如，我的gitlab是部署在192.168.8.1这台机器上，平时我通过`http://192.168.8.1`访问我gitlab，通过`http://192.168.8.1/profile/personal_access_tokens`配置assess token。那我用的时候，就这么用：
```shell
./fetchGitlabIssue.py http://192.168.8.1 "我的token"
```

## TODO
当前脚本比较简陋，只能称作可以使用而已，后续有机会（？）会做出改进。

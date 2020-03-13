# fix_confict_SecurityEnvSDK_SGMain
解决SecurityEnvSDK与SGMain的冲突问题



## 原理

将下面这两个文件中 `OTHER_LDFLAGS` 所在行的内容里，把 `-framework "SecurityEnvSDK"` 置为空字符串。

```shell
Pods/Target Support Files/Pods-项目名/Pods-项目名.debug.xcconfig
Pods/Target Support Files/Pods-项目名/Pods-项目名.release.xcconfig
```



## 使用

1. 将 `fix.py` 放到与`Pods`平级目录中

```shell
.
├── ...
├── Podfile
├── Podfile.lock
├── Pods
│   ├── ...
│   └── ...
└── fix.py
```

 

2. 打开 `Podfile`，在内容最后添加如下内容

```ruby
post_install do |installer|
  # 解决SecurityEnvSDK与SGMain的冲突问题
  command = "python fix.py -p 项目名称"
  system(command)
end
```



3. 执行`pod install`
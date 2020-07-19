[Jupyter Project Documentation](https://jupyter.readthedocs.io/en/latest/)
# 在线尝试[Jupyter](https://try.jupyter.org)
![Dashboard](https://jupyter.readthedocs.io/en/latest/_images/tryjupyter_file.png)
# 运行Notebook

## 基本步骤

1. 从命令行启动Notbook服务```jupyter notebook```
2. 看到在浏览器中的Notebook

## 启动Notebook服务
通过在命令行中运行```jupyter notebook```启动notebook服务，这将在终端中打印一些关于服务的信息，包括web应用的URL（by default, http://localhost:8888）

URL随后会在默认的浏览器中打开。会看到一个显示了notebooks，文件，以及启动Notebook服务时所在目录的子目录的Notebook Dashboard。大部分时候我们都希望在包含notebook的最高层目录中启动服务。

## Notebook服务的命令行选项介绍

### 如何打开一个指定的Notebook?
```
Jupyter notebook notebook.ipynb
```

### 如何在启动Notebook时使用定制端口？
默认情况：服务启动在端口8888，如果端口不可用，服务将搜索下一个可用端口，也可以手工指定一个端口：
```
jupyter notebook --port 9999
```

### 如何在启动Notebook服务时不打开浏览器？
```
Jupyter notebook --no-browser
```

### 如何获得关于Notebook服务选项的帮助？
```
Jupyer notebook --help
```
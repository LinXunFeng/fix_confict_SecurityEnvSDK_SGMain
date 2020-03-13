# -*- coding: UTF-8 -*-
import sys, os, getopt, codecs

def get_current_file_name():
    """获取当前文件名称"""
    return os.path.split(__file__)[-1]

def replace_all_str(file_path, for_str, to_str):
    """
    全文搜索替换或单行替换
    :param file_path: 文件路径
    :param for_str: 要被替换的内容
    :param to_str: 替换之后的内容
    """
    if not os.path.exists(file_path):
        # 文件不存在
        print('文件不存在')
        return
    bak_file_path = file_path+".bak"
    with codecs.open(file_path, 'r', encoding='utf-8') as f, codecs.open(bak_file_path, 'w', encoding='utf-8') as f_w:
        lines = f.readlines()
        for line in lines:
            if "OTHER_LDFLAGS" in line and for_str in line:
                line = line.replace(for_str, to_str)
            f_w.write(line)

    os.remove(file_path)
    os.rename(bak_file_path, file_path)

def throwParamError():
    print("请正确输入命令： %s -p 项目名称" % get_current_file_name())
    sys.exit(0)

def main(argv):
    project_name = ""
    try:
        opts, args = getopt.getopt(argv, "p:", ["project="])
    except getopt.GetoptError:
        throwParamError()
    for opt, arg in opts:
        # print("opt -- ", opt)
        # print("arg -- ", arg)
        if opt in ('-p', '--project'):
            project_name = arg

    if not len(project_name):
        throwParamError()
    
    path_str = "Pods/Target Support Files/Pods-%s/Pods-%s.%s.xcconfig"
    xcconfig_debug_path = path_str % (project_name, project_name, "debug")
    xcconfig_release_path = path_str % (project_name, project_name, "release")
    # print(xcconfig_debug_path)
    # print(xcconfig_release_path)
    be_fixed_str = '-framework "SecurityEnvSDK"'
    replace_all_str(xcconfig_debug_path,  be_fixed_str, '')
    replace_all_str(xcconfig_release_path,  be_fixed_str, '')
    print("%s is fixed successfully" %project_name)

if __name__ == "__main__":
    main(sys.argv[1:])

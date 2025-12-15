#!/usr/bin/env python3
"""
将 very_small 目录下每个子目录中的 GLB 文件转换为 USDA 格式
"""
import bpy
import os
import sys
from pathlib import Path

try:
    from pxr import Usd
except ImportError:
    print("错误: 缺少必要的USD库。请安装pxr USD库。")
    sys.exit(1)

def convert_glb_to_usd(input_glb, output_usd): # 清空现有场景（如果有的话） 
    bpy.ops.object.select_all(action='SELECT') 
    bpy.ops.object.delete() # 导入 GLB 文件 
    bpy.ops.import_scene.gltf(filepath=input_glb) # 导出为 USD 文件 
    bpy.ops.wm.usd_export(filepath=output_usd)
def convert_glb_to_usda(input_dir):
    """
    遍历 input_dir 下的所有子目录，将其中的 3d-asset.glb 转换为 3d-asset.usda
    
    Args:
        input_dir (str): 输入目录路径
    """
    # 检查输入目录是否存在
    if not os.path.exists(input_dir):
        print(f"错误: 目录 '{input_dir}' 不存在")
        return
    
    # 获取所有子目录
    subdirs = [d for d in os.listdir(input_dir) 
               if os.path.isdir(os.path.join(input_dir, d))]
    
    print(f"找到 {len(subdirs)} 个子目录")
    
    # 按名称排序
    subdirs.sort()
    
    success_count = 0
    failed_count = 0
    
    # 遍历每个子目录
    for i, subdir in enumerate(subdirs):
        subdir_path = os.path.join(input_dir, subdir)
        glb_path = os.path.join(subdir_path, "3d-asset.glb")
        usda_path = os.path.join(subdir_path, "3d-asset.usda")
        
        # 检查GLB文件是否存在
        if not os.path.exists(glb_path):
            print(f"警告: {subdir} 中未找到 3d-asset.glb")
            failed_count += 1
            continue
        
        # 检查USDA文件是否已存在
        if os.path.exists(usda_path):
            print(f"跳过: {subdir} 的 USDA 文件已存在")
            success_count += 1
            continue
        
        try:
            # 使用USD库加载GLB文件并保存为USDA格式\
            convert_glb_to_usd(glb_path, usda_path)
            success_count += 1
        except Exception as e:
            print(f"转换出错: {subdir} - {str(e)}")
            failed_count += 1
        # 显示进度
        if (i + 1) % 10 == 0:
            print(f"进度: 已处理 {i + 1}/{len(subdirs)} 个目录")
    
    print(f"\n转换完成!")
    print(f"成功: {success_count}")
    print(f"失败: {failed_count}")


def main():
    input_dir = "very_small"
    convert_glb_to_usda(input_dir)


if __name__ == "__main__":
    main()
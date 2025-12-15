import bpy
import os
import shutil

# 获取当前工作目录
base_dir = os.getcwd()

# 定义目标转换的路径
converted_dir = os.path.join(base_dir, 'converted')

# 如果 converted 文件夹不存在，则创建它
if not os.path.exists(converted_dir):
    os.makedirs(converted_dir)

def convert_glb_to_usd(input_glb, output_usd): # 清空现有场景（如果有的话） 
    bpy.ops.object.select_all(action='SELECT') 
    bpy.ops.object.delete() # 导入 GLB 文件 
    bpy.ops.import_scene.gltf(filepath=input_glb) # 导出为 USD 文件 
    bpy.ops.wm.usd_export(filepath=output_usd)
def process_directory(directory):
    # 遍历目录下的所有文件和子目录
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name == "collision" or dir_name == "visual":
                # 处理collision和visual文件夹
                folder_path = os.path.join(root, dir_name)
                
                # 创建 converted 目录下的对应目录
                relative_path = os.path.relpath(folder_path, base_dir)
                new_folder_path = os.path.join(converted_dir, relative_path)
                
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)

                # 获取所有 .glb 文件
                glb_files = [f for f in os.listdir(folder_path) if f.endswith(".glb")]

                # 如果该文件夹有多个 GLB 文件，合并为一个 USD 文件
                for glb_file in glb_files:
                    input_glb=os.path.join(folder_path, glb_file)
                    output_usd=os.path.join(new_folder_path, glb_file.replace(".glb", ".usd"))
                    print(f"正在合并: {input_glb} 到 {output_usd}")
                    convert_glb_to_usd(input_glb,output_usd)


# 执行转换
process_directory(base_dir)

print("所有文件转换完成。")

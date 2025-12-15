# converting glb file to usd or usda

主要基于bpy库进行实现。bpy是blender的python api。核心代码系：

```python
def convert_glb_to_usd(input_glb, output_usd): # 清空现有场景（如果有的话） 
    bpy.ops.object.select_all(action='SELECT') 
    bpy.ops.object.delete() # 导入 GLB 文件 
    bpy.ops.import_scene.gltf(filepath=input_glb) # 导出为 USD 文件 
    bpy.ops.wm.usd_export(filepath=output_usd)
```

包含两个文件：

convert_to_usda.py和convert_to_usd.py

使用正常时候的截图应为：
<img width="1098" height="417" alt="image" src="https://github.com/user-attachments/assets/b02d99ea-93dd-4f8f-be3a-74cdf2a6bc15" />

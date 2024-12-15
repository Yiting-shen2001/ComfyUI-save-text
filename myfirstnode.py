import shutil
import os
import re

class MyNode:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),				
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Strinng",)

    FUNCTION = "test"

    CATEGORY = "image/mynode2"

    def test(self, text):
        try:
            # 假設 text 是原文件的完整路徑
            source_path = text
            target_folder = "/path/to/destination/folder"  # 修改為目標文件夾
            
            # 確保目標文件夾存在
            os.makedirs(target_folder, exist_ok=True)
            
            # 獲取原文件名和擴展名
            file_name, file_ext = os.path.splitext(os.path.basename(source_path))
            
            # 查找目標資料夾內所有與該文件名相關的文件
            existing_files = [f for f in os.listdir(target_folder) 
                              if f.startswith(file_name) and f.endswith(file_ext)]
            
            # 分析現有文件的數字後綴
            max_index = 0
            for f in existing_files:
                match = re.match(rf"{re.escape(file_name)}_(\d+){re.escape(file_ext)}", f)
                if match:
                    max_index = max(max_index, int(match.group(1)))
            
            # 決定新文件名
            if max_index == 0 and f"{file_name}{file_ext}" not in existing_files:
                target_path = os.path.join(target_folder, f"{file_name}{file_ext}")
            else:
                target_path = os.path.join(target_folder, f"{file_name}_{max_index + 1}{file_ext}")
            
            # 複製文件到目標文件夾
            shutil.copy(source_path, target_path)
            
            # 清空原文件內容
            with open(source_path, "w") as file:
                file.write("")
            
            return (f"File copied to: {target_path}",)
        
        except Exception as e:
            return (f"An error occurred: {str(e)}",)




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "My First Node": MyNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FirstNode": "My First Node"
}

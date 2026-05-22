cd backend

# 创建虚拟环境（可选但推荐）
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 启动服务
python main.py

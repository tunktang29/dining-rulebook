import sys
import os

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.agent import build_agent

def main():
    """简单的测试运行"""
    print("正在加载餐饮红宝书 Agent...")
    
    try:
        # 构建 Agent
        agent = build_agent()
        print("✅ Agent 加载成功！")
        print("可以通过 API 接口访问 Agent")
        
    except Exception as e:
        print(f"❌ Agent 加载失败: {e}")
        print("请检查配置文件和依赖是否正确安装")

if __name__ == "__main__":
    main()
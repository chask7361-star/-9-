"""
智谱 AI 评价后端代理服务
使用前需要先安装依赖: pip install flask flask-cors requests
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)
CORS(app)  # 允许跨域

# ============ 配置区域 ============
# 请设置环境变量 ZHIPU_API_KEY，或在下方填入你的 API Key
# 注意：不要把包含真实 API Key 的文件提交到 Git！
ZHIPU_API_KEY = os.environ.get('ZHIPU_API_KEY', '')

# 如果没有设置环境变量，可以临时在这里填写（仅本地测试用）
# ZHIPU_API_KEY = 'your-api-key-here'
ZHIPU_API_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'

# 如果上面直接写了 API Key，把这行注释掉
# ZHIPU_API_KEY = 'your-api-key-here'
# ==================================


@app.route('/api/review', methods=['POST'])
def review_anime_taste():
    """
    接收用户的9部动画，返回 AI 评价
    请求格式: {"animes": [{"title": "火影忍者", "year": "2002"}, ...]}
    """
    try:
        data = request.get_json()
        animes = data.get('animes', [])
        
        if not animes or len(animes) == 0:
            return jsonify({'error': '请至少选择一部动画'}), 400
        
        # 构建动画列表文本
        anime_list_text = '\n'.join([
            f"{i+1}. {anime.get('title', '未知')} ({anime.get('year', '未知年份')})"
            for i, anime in enumerate(animes)
        ])
        
        # 构建 Prompt
        prompt = f"""你是一位资深的动漫评论家，对动画有深入的研究和独特的见解。

请根据用户选择的以下{len(animes)}部动画，分析用户的动画品味，并给出有趣、专业且略带幽默的评价：

用户选择的动画：
{anime_list_text}

请从以下几个维度进行分析（总字数控制在300-500字）：

1. **整体品味画像**：用户偏爱什么类型的动画？是热血少年、治愈日常、还是文艺深沉？

2. **时代偏好分析**：从选择的动画年代分布，推测用户的入坑时期和怀旧程度

3. **毒舌点评**：用幽默的方式指出用户选择中的"问题"（比如是不是太宅了、太热血中二了、或者过于文艺装逼等）

4. **推荐补番**：基于已有选择，推荐2-3部用户可能喜欢但没看过的动画，并简要说明理由

请用中文回答，语气要轻松有趣，不要太严肃。可以适当使用emoji增加趣味性。
"""

        # 调用智谱 API
        headers = {
            'Authorization': f'Bearer {ZHIPU_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': 'glm-4-flash',  # 使用免费/低成本的 flash 模型，如需更好效果可改为 'glm-4'
            'messages': [
                {'role': 'system', 'content': '你是动漫领域专家，善于分析用户的动画品味并给出有趣的专业评价。'},
                {'role': 'user', 'content': prompt}
            ],
            'temperature': 0.8,
            'max_tokens': 800
        }
        
        response = requests.post(
            ZHIPU_API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code != 200:
            print(f'智谱API错误: {response.status_code} - {response.text}')
            return jsonify({'error': 'AI 服务暂时不可用，请稍后重试'}), 500
        
        result = response.json()
        review_text = result['choices'][0]['message']['content']
        
        return jsonify({
            'success': True,
            'review': review_text,
            'model': result.get('model', 'unknown')
        })
        
    except Exception as e:
        print(f'服务器错误: {str(e)}')
        return jsonify({'error': f'服务器错误: {str(e)}'}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({'status': 'ok', 'message': 'AI 评价服务运行中'})


if __name__ == '__main__':
    print("=" * 50)
    print("智谱 AI 评价服务启动中...")
    print(f"API Key: {'已配置' if ZHIPU_API_KEY and ZHIPU_API_KEY != 'your-api-key-here' else '未配置！请在代码中设置或设置环境变量 ZHIPU_API_KEY'}")
    print("服务地址: http://127.0.0.1:5000")
    print("测试地址: http://127.0.0.1:5000/api/health")
    print("=" * 50)
    
    # debug=True 方便调试，生产环境建议关闭
    app.run(host='0.0.0.0', port=5000, debug=True)

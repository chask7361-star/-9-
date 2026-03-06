# 9部动画 + AI 品味分析

## 功能介绍

在原有的 "构成我的9部动画" 基础上，新增了 **AI 动漫品味分析** 功能：

- ✅ **右侧侧边栏** 显示 AI 评价
- 🤖 **智谱 GLM-4** 大模型分析用户动画品味
- 📊 **多维度分析**：整体品味画像、时代偏好、毒舌点评、推荐补番
- 🌐 **国内可直接访问**，无需梯子

## 效果预览

```
+--------------------------------+------------------+
|   构成我的9部动画              |  AI 动漫品味分析师  |
|   [1] [2] [3]                  |  ----------------  |
|   [4] [5] [6]                  |  📖 整体品味画像   |
|   [7] [8] [9]                  |  📈 时代偏好分析   |
|                                |  💬 毒舌点评      |
|   分享文案...                  |  ✨ 推荐补番       |
|                                |                    |
|   [复制分享文案] [全部重置]    |  [获取 AI 评价]    |
+--------------------------------+------------------+
```

## 快速开始

### 1. 获取智谱 API Key

1. 访问 [智谱 AI 开放平台](https://open.bigmodel.cn/)
2. 注册/登录账号
3. 在「API Keys」页面创建新的 API Key
4. 复制 API Key（格式类似：`xxx.yyyyy`）

> 💰 智谱 GLM-4-Flash 模型目前是**免费的**，有额度限制但个人使用完全足够

### 2. 启动后端服务

```bash
# 安装依赖
pip install flask flask-cors requests

# 编辑 ai_review_server.py，填入你的 API Key
# 方式1：直接修改文件（第14行）
ZHIPU_API_KEY = 'your-api-key-here'

# 方式2：设置环境变量（推荐，更安全）
set ZHIPU_API_KEY=your-api-key-here  # Windows
export ZHIPU_API_KEY=your-api-key-here  # Linux/Mac

# 启动后端
python ai_review_server.py
```

看到以下输出表示启动成功：
```
==================================================
智谱 AI 评价服务启动中...
API Key: 已配置
服务地址: http://127.0.0.1:5000
测试地址: http://127.0.0.1:5000/api/health
==================================================
```

### 3. 打开前端页面

直接用浏览器打开 `index.html` 文件即可：
```
file:///C:/Users/Administrator/index.html
```

或者使用简单的 HTTP 服务器（避免某些浏览器的 CORS 限制）：
```bash
# Python 3
python -m http.server 8080

# 然后访问 http://localhost:8080
```

## 使用说明

1. 在左侧选择你喜欢的 9 部动画（点击卡片搜索选择）
2. 选择至少 3 部后，右侧「获取 AI 评价」按钮会变为可用
3. 点击按钮，等待 AI 分析完成（约 3-10 秒）
4. 查看 AI 生成的个性化评价！

## 常见问题

### Q: 提示 "获取评价失败"？

检查以下几点：
1. ✅ 后端服务是否已启动（`python ai_review_server.py`）
2. ✅ API Key 是否正确配置
3. ✅ 浏览器控制台（F12）查看具体错误信息
4. ✅ 如果后端部署在服务器上，修改前端代码中的 `API_BASE_URL`

### Q: 如何部署到服务器让其他人使用？

**后端部署：**
```bash
# 使用 gunicorn 部署（Linux）
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:5000 ai_review_server:app
```

**修改前端 API 地址：**
编辑 `index.html`，找到 `getAIReview` 函数，修改：
```javascript
const API_BASE_URL = 'http://你的服务器IP:5000';
// 或部署到域名
const API_BASE_URL = 'https://your-domain.com/api';
```

### Q: 可以用其他模型吗？

可以！修改 `ai_review_server.py` 中的 `payload`：
```python
# 使用更强的模型（费用更高）
'model': 'glm-4'

# 使用轻量级模型（免费）
'model': 'glm-4-flash'
```

### Q: 国内用户能访问吗？

👍 **完全可以！** 智谱 API 服务器在国内，无需梯子即可访问。

## 文件说明

| 文件 | 说明 |
|------|------|
| `index.html` | 前端页面（已包含 AI 评价功能） |
| `ai_review_server.py` | Python Flask 后端代理服务 |
| `README_AI_Review.md` | 本说明文档 |

## 技术栈

- **前端**：HTML5 + CSS3 + Vanilla JS
- **后端**：Python Flask
- **AI 模型**：智谱 GLM-4 / GLM-4-Flash
- **数据存储**：LocalStorage（本地）

## 安全提示

⚠️ **生产环境部署时请注意：**

1. **不要在前端暴露 API Key** - 必须通过后端代理
2. **添加请求限流** - 防止 API 被滥用
3. **使用 HTTPS** - 生产环境必须启用
4. **设置 CORS 白名单** - 只允许特定域名访问

本示例代码为了简化，使用了宽松的 CORS 设置，生产部署时请加强安全配置。

---

🎬 **享受你的动漫品味分析之旅吧！**

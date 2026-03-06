# 🎬 构成我的9部动画

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个精美的网页应用，让你选择构成自己的 9 部动画，并获得 **AI 动漫品味分析**！

![预览](https://via.placeholder.com/800x400/1a1a2e/667eea?text=9+Animes+Preview)

## ✨ 功能特性

- 🎯 **9宫格选择** - 直观选择你喜欢的动画
- 🔍 **智能搜索** - 支持中文直搜，集成 Bangumi 中文数据库
- 🤖 **AI 品味分析** - 基于智谱 GLM-4 大模型分析你的动漫品味
- 💾 **本地存储** - 选择自动保存到浏览器
- 📱 **响应式设计** - 支持手机、平板、电脑

## 🖼️ 界面预览

```
┌─────────────────────────┬──────────────────────┐
│   构成我的9部动画        │   🤖 AI 动漫品味分析师  │
│                         │   ─────────────────  │
│   [1] [2] [3]           │   📖 整体品味画像      │
│   [4] [5] [6]           │   📈 时代偏好分析      │
│   [7] [8] [9]           │   💬 毒舌点评         │
│                         │   ✨ 推荐补番         │
│   已选择 6/9            │                      │
│   ████████░░            │   [获取 AI 评价]      │
└─────────────────────────┴──────────────────────┘
```

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/9-animes.git
cd 9-animes
```

### 2. 配置后端

```bash
# 安装依赖
pip install flask flask-cors requests

# 获取智谱 API Key
# 1. 访问 https://open.bigmodel.cn/
# 2. 注册账号，创建 API Key

# 设置环境变量（推荐）
export ZHIPU_API_KEY="your-api-key-here"  # Linux/Mac
set ZHIPU_API_KEY=your-api-key-here       # Windows

# 或编辑 ai_review_server.py 临时填写（仅本地测试）
```

### 3. 启动服务

```bash
# 启动后端
python ai_review_server.py

# 前端直接用浏览器打开 index.html
# 或使用 Python 简单 HTTP 服务器
python -m http.server 8080
```

然后访问 http://localhost:8080

## 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | HTML5 + CSS3 + Vanilla JS |
| 后端 | Python Flask |
| AI 模型 | 智谱 GLM-4 / GLM-4-Flash |
| 数据存储 | Browser LocalStorage |
| 数据源 | Bangumi API + Jikan API |

## 📁 项目结构

```
.
├── index.html              # 前端页面
├── ai_review_server.py     # Flask 后端服务
├── README.md               # 项目说明
├── README_AI_Review.md     # AI 功能详细说明
└── .gitignore             # Git 忽略文件
```

## 🔧 自定义配置

### 修改 AI 评价风格

编辑 `ai_review_server.py` 中的 `prompt` 变量，可以自定义 AI 的评价风格：

```python
# 更毒舌
"请用犀利毒舌的风格评价..."

# 更专业
"请用专业动漫评论家的角度分析..."

# 更温柔
"请用温柔鼓励的语气分析..."
```

### 修改 API 地址

如果部署到服务器，修改 `index.html` 中的：

```javascript
const API_BASE_URL = 'https://your-domain.com/api';
```

## 🌐 部署到服务器

### 后端部署（Linux + Gunicorn）

```bash
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:5000 ai_review_server:app
```

### 使用 Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV ZHIPU_API_KEY=${ZHIPU_API_KEY}
EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "ai_review_server:app"]
```

## ⚠️ 注意事项

1. **API Key 安全** - 不要把真实 API Key 提交到 Git！
2. **生产环境** - 请添加请求限流和 HTTPS
3. **跨域设置** - 生产环境请配置 CORS 白名单

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [Bangumi](https://bgm.tv/) - 中文动漫数据库
- [Jikan](https://jikan.moe/) - MyAnimeList API
- [智谱 AI](https://open.bigmodel.cn/) - GLM 大模型

---

Made with ❤️ by [Your Name]

# Vercel部署指南

## 步骤1：登录Vercel账户
访问 [Vercel官网](https://vercel.com/) 并登录您的账户。

## 步骤2：导入GitHub仓库
1. 点击"New Project"按钮
2. 选择"Import Git Repository"
3. 输入仓库URL：`https://github.com/olgelin/ai-tech-website`
4. 点击"Import"

## 步骤3：配置项目设置
1. 项目名称：默认为"ai-tech-website"
2. Framework Preset：选择"Other"
3. Build Command：留空（Vercel会自动检测）
4. Output Directory：留空

## 步骤4：设置环境变量
在"Environment Variables"部分添加以下环境变量：

| 环境变量名 | 描述 | 必填项 |
|------------|------|--------|
| SECRET_KEY | Flask应用密钥，应使用强随机字符串 | 是 |
| DATABASE_URL | 数据库连接字符串（生产环境建议使用MySQL或PostgreSQL） | 是 |
| PORT | 服务器端口，建议使用5000 | 否 |
| DEBUG | 调试模式，生产环境应设置为False | 否 |
| DB_TYPE | 数据库类型（sqlite, mysql, postgresql） | 否 |

## 步骤5：部署项目
点击"Deploy"按钮开始部署过程。

## 步骤6：验证部署
1. 部署完成后，Vercel会提供一个URL（如 `https://ai-tech-website.vercel.app`）
2. 访问该URL验证网站是否正常运行

## 注意事项
1. SQLite数据库在Vercel上可能有持久化问题，建议使用外部数据库服务
2. 所有敏感信息（如密钥、密码）必须通过环境变量设置，不要直接写入代码
3. 定期更新依赖包以确保安全性
4. 监控Vercel控制台的部署日志和错误信息

## 常见问题解决
1. **部署失败**：检查构建日志，确认所有依赖包都已在requirements.txt中列出
2. **数据库连接问题**：确保数据库URL格式正确，且数据库服务允许远程连接
3. **静态文件加载失败**：检查Flask应用的static_folder配置是否正确
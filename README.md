## superspider prj
### 技术栈pyhon方向
1. 爬虫模块，采用`scrapy`爬虫框架，可以定时爬取。对数据进行全量、增量爬取。
2. `ORM`采用`sqlalchemy`,数据库暂定
3. 前端采用`vue`，`element UI`
4. 后端采用`tornado`或者`flask`
5. 任务管理采用`celery`

### 项目架构

```
----superspider
        |----README.md
        |----docs
        |----pip
        |----src
              |----settings
              |        |----globalsettings
              |----bankend
              |        |----spiders
              |        |----server
              |        |       |----webservers
              |        |----domain
              |        |       |----modles
              |        |       |----modlefuncs
              |----frontend
              |        |----index.html
              |        |----datashow
              |        |----spidermgt
              |----scripts
              |
              |----env.sh

```

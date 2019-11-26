# Redis email
![https://github.com/CourseOrchestra/redis-email/actions?query=workflow%3A%22Python+application%22](https://github.com/CourseOrchestra/redis-email/workflows/Python%20application/badge.svg)

Common email-worker

Example
```python
q = Queue('email', connection=Redis.from_url(config.REDIS_URL))
with open('test.jpg', 'rb') as f:
    q.enqueue('common.email', system='test', sender='Sender <sender@example.com>', receiver='Receiver <receiver@example.com>',
              subject='Multipart Email Example', content='''Привет как дела''',
              content_html='''<b>Привет</b> как дела''', attachments={'test.jpg': f.read()}
              )
```

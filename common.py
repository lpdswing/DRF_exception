from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        try:
            try:
                response.data['msg'] = response.data['detail']
                response.data['status'] = 'error'
                del response.data['detail']
            except:pass
            # 处理序列化异常,根据官方文档介绍这里处理方式不一样
            try:
                d = exe.__dict__
                list_field = []
                for i,k in d['detail'].items():
                    list_field.append(dict(field=i, message=k[0]))
                response.data.clear()
                response.data['msg'] = list_field
                response.data['status'] = 'error'
            except:pass
        except:pass
    return response

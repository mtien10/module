from django.db import connection

class QueryCountDebugMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)


        total_time = 0

        for query in connection.queries:
            query_time = query_get('time')
            print(str(query))

            if query_time is None:
                query_time =query.get('duration',0) / 1000

            total_time += float(query_time)

        print('%s queries run,total %s seconds' % (len(connection.queries),total_time))
        return response
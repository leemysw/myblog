# coding:utf-8
from django.core.paginator import Paginator


def getPages(request, objectlist , num=3):
    """get the paginator"""
    paginator = Paginator(objectlist, num)
    currentPage = request.GET.get('page', 1)
    object_list = paginator.get_page(currentPage)#Django 2.0下新增了get_page()方法

    page_range = [ ]
    current = object_list.number  # 当前页码
    page_all = paginator.num_pages  # 总页数
    mid_pages = 3  # 中间段显示的页码数
    page_go = 1  # 默认跳转的页码

    # 获取优化显示的页码列表
    if page_all <= 2 + mid_pages:
        # 页码数少于6页就无需分析哪些地方需要隐藏
        page_range = paginator.page_range
    else:
        # 添加应该显示的页码
        page_range += [1, page_all]
        page_range += [current - 1, current, current + 1]

        # 若当前页是头尾，范围拓展多1页
        if current == 1 or current == page_all:
            page_range += [current + 2, current - 2]

        # 去掉超出范围的页码
        page_range = filter(lambda x: x >= 1 and x <= page_all, page_range)

        # 排序去重
        page_range = sorted(list(set(page_range)))

        # 查漏补缺
        # 从第2个开始遍历，查看页码间隔，若间隔为0则是连续的
        # 若间隔为1则补上页码；间隔超过1，则补上省略号
        t = 1
        for i in range(len(page_range) - 1):
            step = page_range[t] - page_range[t - 1]
            if step >= 2:
                if step == 2:
                    page_range.insert(t, page_range[t] - 1)#补页码
                else:
                    page_go = page_range[t - 1] + 1
                    page_range.insert(t, '...')
                t += 1
            t += 1

    # 优化结果之后的页码列表
    paginator.page_range_ex = page_range
    # 默认跳转页的值
    paginator.page_go = page_go

    return paginator, object_list

from django.http import JsonResponse
from django.shortcuts import render
from blog.page import GetPages

from login.models import User
# Create your views here.
from .models import Comment, CommentReply
from .forms import CommentForm


# class CommentView(ListView):
#     '文章评论列表'
#     model = Comment
#     # 前端使用Ajax请求评论数据，故该模板仅包含评论部分
#     template_name = 'comment/comment.html'
#     context_object_name = 'comment_list'
#     # 分页，每页10条评论
#     paginate_by = 10
#
#     # 筛选目标文章的评论，article_id为url中的参数

def comment(request):
    if request.method == 'POST':
        comment = Comment()
        commentreply = CommentReply()
        comment_content = request.POST['comment_content']
        print(comment_content)
        if not request.POST['comment_id']:
            comment.content = comment_content
            comment.user = User.objects.get(name=request.session.get('user_name'))
            comment.save()
            return JsonResponse({'msg': 'success'}, )

        else:
            print('2')
            comment_id = request.POST['comment_id']
            commentreply.content = comment_content
            commentreply.user = User.objects.get(name=request.session.get('user_name'))
            commentreply.comment = Comment.objects.get(id=comment_id)
            if request.POST['reply_to']:
                reply_to = request.POST['reply_to']
                commentreply.reply = CommentReply.objects.get(id=reply_to)
            commentreply.save()
            return JsonResponse({'msg': 'success'}, )

    else:
        print('3')
        form = CommentForm()
        comment_list = Comment.objects.all()
        getPages = GetPages(request, comment_list, num=5)
        pages, comment_list = getPages.getpage()
        commentreply = CommentReply.objects.all()
        return render(request, 'comment/comment.html', locals())


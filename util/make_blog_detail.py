from blog.models import Blog
from comment.models import CommentModel
def make_single_blog(blog):
    """
    构建单篇博客内容
    """
    data = {}
    res = {'code':200,'data':data}
    data['author'] = blog.blogAuthor.username
    data['title'] = blog.blogTitle
    data['content'] = blog.blogContent
    data['cover'] = str(blog.blogCover)
    data['category'] = 1
    data['createTime'] = blog.blogCreateTime
    data['popupNum'] = blog.blogPopupNum
    data['intro'] = blog.blogIntro
    last_topic = Blog.objects.filter(pk__lt=blog.pk).last()
    next_topic = Blog.objects.filter(pk__gt=blog.pk).first()
    if not last_topic:
        last_topic = None
        data['last_id'] = last_topic
        data['last_title'] = last_topic
    else:
        data['last_id'] = last_topic.id
        data['last_title'] = last_topic.blogTitle
        data['last_cover'] = str(last_topic.blogCover)
    if not next_topic:
        next_topic = None
        data['next_id'] = next_topic
        data['next_title'] = next_topic
    else:
        data['next_id'] = next_topic.id
        data['next_title'] = next_topic.blogTitle
        data['next_cover'] = str(next_topic.blogCover)
    first_comments = blog.commentOfblog.filter(parentComment=0)
    comment_set = []
    comment_set = build_comment(blog,first_comments,comment_set)
    data['comment'] = comment_set
    data['commentNumber'] = first_comments.count()
    return res
def build_comment(blog,comments,comment_set):
    for comment in comments:
        each_comment = {}
        each_comment['id'] = comment.id
        each_comment['content'] = comment.commentContent
        each_comment['commentor'] = comment.commentor.username
        each_comment['commentor_avatar'] = str(comment.commentor.avtar)
        each_comment['create_time'] = comment.create_time
        each_comment['commentLikeNum'] = comment.commentLikeNum
        """构建评论及其回复"""
        reply_set = []
        reply = make_reply(comment.id,blog,reply_set)
        each_comment['reply'] = reply
        comment_set.append(each_comment)
    return comment_set

def make_reply(parent_reply,blog,reply_set):

    if not CommentModel.objects.filter(blog=blog.pk,parentComment=parent_reply):
        return reply_set

    else:
        comments = CommentModel.objects.filter(blog=blog.pk,parentComment=parent_reply)
        build_comment(blog,comments,reply_set)




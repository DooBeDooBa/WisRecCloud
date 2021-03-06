from django.conf.urls import url

from .views import RecallData, RecallWeiBo, RecallMovie, RecallItemMovie

urlpatterns = [
    url(r'wisRecCloud/api/zhaopin/recall_jcd', RecallData.as_view(), name="jieCard"),  # 招聘数据召回
    url(r'wisRecCloud/api/wenzhang/recall_jcd', RecallWeiBo.as_view(), name="jieCardWeiBo"),  # 文章咨询召回接口
    url(r'wisRecCloud/api/movie/recall_cf', RecallMovie.as_view(), name="movie"),  # user 电影数据召回接口
    url(r'wisRecCloud/api/movie/recall_item', RecallItemMovie.as_view(), name="itemView"),  # item 电影数据召回接口
]

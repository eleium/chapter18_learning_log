from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry


# Create your views here.
def index(request):
    # 学习笔记的主页
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    # 显示所有的主题：
    # topics = Topic.objects.order_by("date_added")
    # 只向用户显示属于自己的主题：
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    # Topic.objects：是一个查询集，一个容器，内含 owner,text，datetime等
    # filter()过滤，从 Topic 这张表里，找出 owner 字段等于 request.user（当前登录用户）的所有记录。”
    # order_by:“按照 date_added 字段升序（从小到大）排列。”

    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    # 显示单个主题及其所有的条目
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前的用户：
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    # 添加新主题

    if request.method != "POST":
        # 未提交的数据：创建一个新表单
        form = TopicForm()

    else:
        # POST 提交的数据：对数据进行处理：
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            # form.save()
            return redirect("learning_logs:topics")
            # redirect() 不是刷新 new_topic.html，而是直接告诉浏览器：“去访问另一个 URL”

    # 显示空表单，或者指出表单数据无效：
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    # 在特定的主题中添加新的条目
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        # 未提交数据，创建一个空表单
        form = EntryForm()

    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    # 显示空表单或指出表单数据无效：
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    # 编辑现有的条目
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        # 初次请求：使用当前的条目填充表单
        form = EntryForm(instance=entry)

    else:
        # Post提交的数据：对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)
